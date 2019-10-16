import argparse
import sys
import requests

# Global constants
DESCRIPTION = 'Command line interface to control some aspects of the Marvin API'
VERSION = 0.1
QUIT_OPTIONS = ['quit', 'exit', 'q']
HELP_OPTIONS = ['-h', '--help', 'help', 'h', '?']

def make_server_url(base_address='http://noahpi1', port=5000, url_base='/'):
    return base_address + ':' + str(port) + url_base

# Lights constants
# Examples: "marvin lights on", "marvin lights off"
LIGHTS_CMD_OPTIONS = ['on', 'off', 'scenes', 'day', 'night']
LIGHTS_CMD_NAME = 'lights_cmd'

LIGHTS_COLOR_CMD_OPTIONS = ['lcolor']
LIGHTS_COLOR_CMD_NAME = 'lights_color_cmd'

# Hack to have ArgumentParser throw an exception rather than sys.exit() when it
# encounters bad input
class ArgumentParserError(Exception):
    pass

class ExceptionArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        raise ArgumentParserError(message)

# HTTP request helper functions
def get(endpoint):
    resp = requests.get(endpoint)
    if resp.status_code != 200:
        error_response(resp)
        return None
    return resp.json()

def post(endpoint, data={}):
    resp = requests.post(endpoint, json=data)
    if resp.status_code != 200:
        error_response(resp)
        return None
    return resp.json()
    
def error_response(resp):
    resp_body = resp.json()
    error = resp_body['error'] if 'error' in resp_body else 'Unknown error, see server logs'
    print("Error ({}) handling request: {}".format(resp.status_code, error))

# Command interpretation logic
def run(args, server_url):
    try:
        lights_endpoint = server_url + 'lights/'
        # Make request to lights endpoint
        if LIGHTS_CMD_NAME in args:
            cmd_val = args[LIGHTS_CMD_NAME]
            print('lights command (' + LIGHTS_CMD_NAME + '): ' + cmd_val)
            if cmd_val == 'on':
                post(lights_endpoint + 'on')
            elif cmd_val == 'off':
                post(lights_endpoint + 'off')
            elif cmd_val == 'scenes':
                scenes = get(lights_endpoint + 'scenes')
                print('Possible scenes are:')
                for scene in scenes:
                    print(scene['name'])
            elif cmd_val == 'day':
                post(lights_endpoint + 'scenes', data={'sceneName': 'Read'})
            elif cmd_val == 'night':
                post(lights_endpoint + 'scenes', data={'sceneName': 'Relax'})
        # Lights color needs to be separate from lights. I guess using the
        # argparser like this really is a hack.
        elif LIGHTS_COLOR_CMD_NAME in args:
            rgb = args[LIGHTS_COLOR_CMD_NAME]
            post(lights_endpoint + 'color',
                data={ 'rgb': {
                    'r': rgb[0],
                    'g': rgb[1],
                    'b': rgb[2],
                }}
            )
        else:
            print('Error: command "{}" not found. Try "help" to see list of commands')
            return
    except requests.exceptions.ConnectionError as err:
        print('Error making request: {}\nIs the server running and accepting conections?'.format(err))

def main():
    # Set up argument parser
    parser = ExceptionArgumentParser(description=DESCRIPTION, prog='marvin')
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + str(VERSION))
    parser.add_argument('--url')
    subparsers = parser.add_subparsers()

    # Set up lights subparser
    lights_parser = subparsers.add_parser('lights')
    lights_parser.add_argument(LIGHTS_CMD_NAME,
                               action='store',
                               type=str,
                               choices=LIGHTS_CMD_OPTIONS)

    lights_parser = subparsers.add_parser('lcolor')
    lights_parser.add_argument(LIGHTS_COLOR_CMD_NAME,
                               nargs=3,
                               action='store',
                               type=int)

    # Interpret arguments given
    args = vars(parser.parse_args())
    server_url = make_server_url(args['url']) if args['url'] else make_server_url()
    args.pop('url')

    if len(args) == 0: # Interactive mode
        print("Marvin v{} started in interactive mode".format(str(VERSION)))
        while True:
            cmd = None
            exit_inter = False # Indicates that user has chosen to exit program

            # Get input, exit upon KeyboardInterrupt (SIGINT)
            try:
                cmd = input('> ')
            except KeyboardInterrupt:
                print() # print newline to match behavior of input()
                exit_inter = True

            if cmd in QUIT_OPTIONS:
                exit_inter = True
            
            if exit_inter:
                print('Goodbye')
                break
            
            # Print help if indicated
            if cmd in HELP_OPTIONS:
                parser.print_help()
                continue

            try:
                # HACK: I don't think the ArgumenParser is supposed to be used
                # for interactive commands, but hey it's easier than writing the
                # parsing logic myself
                inter_args = vars(parser.parse_args(cmd.split()))
                run(inter_args, server_url)
            except ArgumentParserError as error:
                print(error)
                continue
    else:
        run(args, server_url)

if __name__ == '__main__':
    main()
