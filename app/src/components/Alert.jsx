import React from 'react'

const Alert = ({ color, message, className }) => {
    return (
        <div className={`alert alert-${color} ${className} alert-dismissible fade show`} role="alert">
            {message}
            <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    )
}

export default Alert