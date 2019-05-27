import React, { Component } from 'react';
import { NavLink } from "react-router-dom";
import './Sidebar.css';

class Sidebar extends Component {
  constructor(props) {
    super(props)
    this.state = {toggledOn: false};
  }

  toggleSidebar() {
    console.log("sidebar: toggling sidebar")
  }

  render() {
    return (
      <div id="sidebar-wrapper">
        <ul className="sidebar-nav">
          <li className="sidebar-brand"><NavLink to="/">Marvin Web UI</NavLink></li>
          <li><NavLink to="/lights">Lights</NavLink></li>
          {/* <!-- <li>
            <a href="#">Shortcuts</a>
          </li> --> */}
        </ul>
      </div>
    );
  }
}

class SidebarToggle extends Component {
  render() {
    return (
      // <button className="btn btn-secondary" id="menu-toggle" onClick={this.props.toggleSidebar}>Toggle</button>
      <button className="navbar-toggler" id="menu-toggle"
              onClick={this.props.toggleSidebar}>
        <span class="navbar-toggler-icon"></span>
      </button>
    );
  }
}

export { Sidebar, SidebarToggle };
