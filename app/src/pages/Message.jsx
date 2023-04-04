import React, { useContext } from 'react'
import { Context } from '../store/AppContext'
import Alert from '../components/Alert';
import { useNavigate } from 'react-router-dom';

const Message = () => {
  const { store: { messages, error, currentUser }, actions: { logout } } = useContext(Context); 
  const navigate = useNavigate();
  return (
    <div className='container-fluid'>
      <h1>Messages</h1>
      {
        !!error && (
          <span>
          <Alert color="warning" message={error.msg} className={"w-50 mx-auto my-3"} />
          <button className='btn btn-danger btn-sm mx-auto w-50' onClick={(e) => logout(e, navigate)}>Por favor haga click para iniciar session nuevamente...</button>
          </span>
        )
      }
      <ul className="list-group my-5">
        {
          !!messages &&
            messages.results.length > 0 ?
            messages.results.map((msg) => {
              console.log(msg)
              return (
                <li className={'list-group-item ' + (currentUser?.data?.user?.id === msg.user_from.id ? "bg-secondary" : "bg-light")} key={msg.id}>
                  <h5>{currentUser?.data?.user?.id === msg.user_from.id ? "me" : msg.user_from.email}</h5>
                  <p> {msg.message}</p>
                </li>
              )
            })
            : (
              <li className='list-group-item text-center'>Empty</li>
            )
        }
      </ul>
    </div>
  )
}

export default Message