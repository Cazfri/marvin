import React from 'react';

import axios from 'axios';

const marvinURLBase = "http://noahpi1:5000/";

class RequestButton extends React.Component {
    constructor(props) {
        super(props);

        this.makeRequest = this.makeRequest.bind(this);
    }

    async makeRequest() {
        console.log(`Making request to ${this.props.endpoint} with data ${JSON.stringify(this.props.payload)}`)
        const response = await axios.post(marvinURLBase + this.props.endpoint, this.props.payload);
        console.log(response);
    }

    render() {
        return (
            <div className='RequestButtonContainer'>
                <button className="btn btn-primary btn-md btn-block" onClick={this.makeRequest}>{this.props.buttonContent}</button>
            </div>
        )
    }
}

export default RequestButton