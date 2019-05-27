import React, { Component } from 'react';
import { Route, NavLink, HashRouter } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars } from '@fortawesome/free-solid-svg-icons'
// import { Sidebar, SidebarToggle } from './Sidebar'
// import logo from './logo.svg';
import './App.css';

import Home from "./Home";
import Lights from "./Lights"

class App extends Component {
  constructor(props) {
    super(props);
    this.toggleSidebar = this.toggleSidebar.bind(this);
    this.state = {
      showSidebar: false
    };
  }

  toggleSidebar() {
    console.log("togling sidebar");
    this.setState({"showSidebar": !this.state.showSidebar});
  }

  // Note: https://bootstrapious.com/p/bootstrap-sidebar this supports submenus

  render() {
    return (
      <div className="App">
        {/* <div className="topbar"> */}
          {/* <SidebarToggle toggleSidebar={this.toggleSidebar}/> */}
          {/* <header> */}
            {/* <h1>Welcome home, Noah</h1> */}
          {/* </header> */}
        {/* </div> */}
        <div className="wrapper">
          <HashRouter>
            {/* Sidebar */}
            <nav id="sidebar" className={this.state.showSidebar ? null : 'hidden'}>
              <div className="sidebar-header">
                <h2>Marvin Web</h2>
              </div>
              <ul className="list-unstyled components">
                {/* <p>Dummy heading</p> */}
                <li><NavLink to="/">Marvin Web UI</NavLink></li>
                <li><NavLink to="/lights">Lights</NavLink></li>
              </ul>
            </nav>
            {/* Content */}
            <div id="content" className={this.state.showSidebar ? "shoved" : null}>
              <nav className="navbar navbar-light bg-light">
                <div className="container-fluid">
                  <button type="button" id="sidebarCollapse" className="navbar-toggler" onClick={this.toggleSidebar}>
                    <span>
                      <FontAwesomeIcon icon={faBars} />
                    </span>
                  </button>
                </div>
              </nav>
              <Route exact path="/" component={Home}/>
              <Route path="/lights" component={Lights}/>
            </div>
          </HashRouter>
        </div>
      </div>
    );
  }
}

export default App;
