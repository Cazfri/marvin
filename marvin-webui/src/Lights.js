import React, { Component } from "react";
import RequestButton from "./marvin-requests/RequestButton";
import './Lights.css';

let payloadDay = {
    sceneName: "Read"
}

let payloadNight = {
    sceneName: "Relax"
}
class Lights extends Component {
  render() {
    return (
      <div className="container h-100">
        <h2>Lights</h2>
        <p>You can control lights from here. How cool is that? So cool.</p>
        {/* <div className="buttonsContainer container-fluid fill"> */}
          <div className="row my-2">
            <div className="col">
              <RequestButton endpoint="lights/on" payload={{}} buttonContent="On"/>
            </div>
            <div className="col">
              <RequestButton endpoint="lights/off" payload={{}} buttonContent="Off"/>
            </div>
          </div>
          <div className="row my-2">
            <div className="col">
              <RequestButton endpoint="lights/scenes" payload={payloadDay} buttonContent="Day"/>
            </div>
            <div className="col">
              <RequestButton endpoint="lights/scenes" payload={payloadNight} buttonContent="Night"/>
            </div>
          </div>
        {/* </div> */}
      </div>
    )
  }
}

export default Lights;