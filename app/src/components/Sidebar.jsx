import React from 'react'
import { Link } from 'react-router-dom'

const Sidebar = () => {
    return (
        <div className="border-end bg-white" id="sidebar-wrapper">
            <div className="sidebar-heading border-bottom bg-light">
                Start Bootstrap
            </div>
            <div className="list-group list-group-flush">
                <Link
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    to="/"
                >
                    Dashboard
                </Link>
                <Link
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    to="/messages"
                >
                    Messages
                </Link>
                <Link
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    to="/profile"
                >
                    Profile
                </Link>
                <a
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    href="#!"
                >
                    Events
                </a>
                <a
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    href="#!"
                >
                    Profile
                </a>
                <a
                    className="list-group-item list-group-item-action list-group-item-light p-3"
                    href="#!"
                >
                    Status
                </a>
            </div>
        </div>
    )
}

export default Sidebar