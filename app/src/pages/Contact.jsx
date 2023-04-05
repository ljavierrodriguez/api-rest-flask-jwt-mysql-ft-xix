import React, { useContext } from 'react'
import { Context } from '../store/AppContext';
import emailjs from '@emailjs/browser';
import Alert from '../components/Alert';

const Contact = () => {

    const { store: { error, success }, actions: { handleChange, sendEmail } } = useContext(Context);

    return (
        <div className="container-fluid">
            <h1 className="mt-4">Contact</h1>
            {
                !!error && (
                    <Alert color="danger" message={error.message} className={"w-50 mx-auto my-3"} />
                )
            }
            {
                !!success && (
                    <Alert color="success" message={success.message} className={"w-50 mx-auto my-3"} />
                )
            }
            <form className="m-5 mx-auto w-50" onSubmit={(e) => sendEmail(e, emailjs)}>
                <div className="form-group mb-3">
                    <label htmlFor="name" className="form-label">Fullname:</label>
                    <input type="text" name="from_name" id="name" className="form-control" placeholder='Fullname' onChange={handleChange} />
                </div>
                <div className="form-group mb-3">
                    <label htmlFor="email" className="form-label">Email:</label>
                    <input type="email" name="from_email" id="email" className="form-control" placeholder='email@domain.x' onChange={handleChange} />
                </div>
                <div className="form-group mb-3">
                    <label htmlFor="password" className="form-label">Message:</label>
                    <textarea name="from_message" id="message" cols="30" rows="5" className="form-control" placeholder='Your message here' onChange={handleChange}></textarea>
                </div>
                <button className="btn btn-success btn-sm py-2 w-100">Send Message</button>
            </form>
        </div>
    )
}

export default Contact