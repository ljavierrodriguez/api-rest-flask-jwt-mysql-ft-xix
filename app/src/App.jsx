import React, { useContext } from 'react'
import './styles/global.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import Sidebar from './components/Sidebar'
import Navbar from './components/Navbar'
import injectContext, { Context } from './store/AppContext'
import Login from './pages/Login'
import ProtectedRoute from './pages/ProtectedRoute'
import Message from './pages/Message'
import Profile from './pages/Profile'
import Contact from './pages/Contact'

const App = () => {
  const { store: { currentUser } } = useContext(Context);
  return (
    <BrowserRouter>
      <div className="d-flex" id="wrapper">
        {/* Sidebar*/}
        {!!currentUser && <Sidebar />}
        {/* Page content wrapper*/}
        <div id="page-content-wrapper">
          {/* Top navigation*/}
          <Navbar />
          {/* Page content*/}
          <Routes>
            <Route path='/contact' element={<Contact />} />
            <Route path='/login' element={<Login />} />
            <Route path='/profile' element={<ProtectedRoute currentUser={currentUser}><Profile /></ProtectedRoute>} />
            <Route path='/messages' element={<ProtectedRoute currentUser={currentUser}><Message /></ProtectedRoute>} />
            <Route path='/' element={<ProtectedRoute currentUser={currentUser}><Home /></ProtectedRoute>} />
            <Route path='*' element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  )
}

export default injectContext(App)