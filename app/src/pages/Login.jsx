import React, { useContext } from 'react'
import { Context } from '../store/AppContext'
import Alert from '../components/Alert';
import { Navigate, useNavigate } from 'react-router-dom'

const Login = () => {

    const navigate = useNavigate()

    const { store: { error, currentUser }, actions: { login, handleChange } } = useContext(Context);

    if(currentUser !== null) {
        return <Navigate to="/" replace />
    }

    return (
        <div className="container-fluid">
            <h1 className="mt-4">Login</h1>
            {
                !!error && (
                    <Alert color="danger" message={error.message} className={"w-50 mx-auto my-3"} />
                )
            }
            <form className="m-5 mx-auto w-50" onSubmit={(e) => login(e, navigate)}>
                <div className="form-group mb-3">
                    <label htmlFor="email" className="form-label">Email:</label>
                    <input type="email" name="email" id="email" className="form-control" placeholder='email@domain.x' onChange={handleChange} />
                </div>
                <div className="form-group mb-3">
                    <label htmlFor="password" className="form-label">Password:</label>
                    <input type="password" name="password" id="password" className="form-control" placeholder='xxxxxxxxxxxx' onChange={handleChange} />
                </div>
                <button className="btn btn-primary btn-sm py-2 w-100">LOGIN</button>
            </form>
        </div>
    )
}

export default Login