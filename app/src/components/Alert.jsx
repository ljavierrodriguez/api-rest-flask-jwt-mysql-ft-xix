import React from 'react'

const Alert = ({ color, message, className }) => {
    return (
        <div className={`alert alert-${color} ${className}`} role="alert">
            {message}
        </div>
    )
}

export default Alert