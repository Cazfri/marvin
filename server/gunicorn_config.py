# Gunicorn config file

# Number of workers
workers = 1

# Run gunicorn as a daemon
daemon = True

# Bind to the same unix socket as nginx
bind = 'unix:marvin.sock'
# Socket permissions
umask = 664

# Gunicorn logging
errorlog = '../logs/gunicorn_error.log'
accesslog = '../logs/gunicorn_error.log'
loglevel = 'info'

