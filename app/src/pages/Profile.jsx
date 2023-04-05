import React, { useContext } from 'react'
import { Context } from '../store/AppContext'
import avatar from './../img/avatar_sin_foto.png'

const Profile = () => {

    const { store: { currentUser }, actions: { uploadAvatar, handleChangeFile } } = useContext(Context);

    return (
        <div className="container-fluid">
            <h1 className="mt-4">Profile</h1>
            <div className="row">
                <div className="col-md-12">
                    <div className="card w-75">
                        <div className="card-header">
                            <h3 className="card-title">User Avatar</h3>
                        </div>
                        <div className="card-body">
                            <div className="row">
                                <div className="col-md-6">
                                    {currentUser?.data?.user?.profile?.avatar !== null ? (
                                        <img src={currentUser?.data?.user?.profile?.avatar} alt="avatar" className='img-fluid rounded-circle mx-2' />
                                    ) : (
                                        <img src={avatar} alt="avatar" className='img-fluid rounded-circle mx-2' />
                                    )}
                                </div>
                                <div className="col-md-6">
                                    <form onSubmit={uploadAvatar}>
                                        <div className="form-group mb-3">
                                            <label htmlFor="file" className="form-label">Avatar</label>
                                            <input type="file" id="file" name="file" className="form-control" onChange={handleChangeFile} />
                                        </div>
                                        <button className="btn btn-primary btn-sm w-100">Upload</button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">

            </div>
        </div>
    )
}

export default Profile