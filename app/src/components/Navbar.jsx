import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Context } from '../store/AppContext'
import Timer from './Timer';

const Navbar = () => {

    const { store: { currentUser }, actions: { logout } } = useContext(Context);
    const navigate = useNavigate();

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light border-bottom">
            <div className="container-fluid">
                <Timer className={"btn btn-primary"} duration={currentUser?.data?.expire || 0 } />
                {/* <button className="btn btn-primary" id="sidebarToggle">
                    Toggle Menu
                </button> */}
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon" />
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav ms-auto mt-2 mt-lg-0">
                        {
                            !!currentUser ?
                                (
                                    <>
                                        <li className="nav-item dropdown">
                                            <a
                                                className="nav-link dropdown-toggle"
                                                id="navbarDropdown"
                                                href="#"
                                                role="button"
                                                data-bs-toggle="dropdown"
                                                aria-haspopup="true"
                                                aria-expanded="false"
                                            >
                                                {currentUser?.data?.user?.email}
                                            </a>
                                            <div
                                                className="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="navbarDropdown"
                                            >
                                                <a className="dropdown-item" href="#!">
                                                    Action
                                                </a>
                                                <a className="dropdown-item" href="#!">
                                                    Another action
                                                </a>
                                                <div className="dropdown-divider" />
                                                <button className="dropdown-item" onClick={() => logout(navigate)}>
                                                    Logout
                                                </button>
                                            </div>
                                        </li>

                                    </>
                                ) : (
                                    <>
                                        <li className="nav-item active">
                                            <Link className="nav-link" to="/login">
                                                Login
                                            </Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link className="nav-link" to="/register">
                                                Register
                                            </Link>
                                        </li>
                                    </>
                                )
                        }


                    </ul>
                </div>
            </div>
        </nav >
    )
}

export default Navbar