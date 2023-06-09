const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            API_URL: 'https://5000-ljavierrodr-apirestflas-a5t3f39zb0o.ws-us93.gitpod.io',
            email: '',
            password: '',
            file: null,
            error: null,
            success: null,
            currentUser: null,
            favorites: [],
            messages: null,
            to_name: 'Luis J.',
            from_name: '',
            from_email: '',
            from_message: '',
            SERVICES_ID: '',
            TEMPLATE_ID: '',
            PUBLIC_KEY: '',
        },
        actions: {
            handleChange: e => {
                const { name, value } = e.target;
                setStore({
                    [name]: value
                })
            },
            handleChangeFile: e => {
                const { name, files } = e.target;
                setStore({
                    [name]: files[0]
                })
            },
            login: async (e, navigate) => {
                e.preventDefault()
                try {
                    const { email, password, API_URL } = getStore();

                    const options = {
                        method: 'POST',
                        body: JSON.stringify({ email, password }),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }

                    const response = await fetch(`${API_URL}/api/login`, options)

                    const data = await response.json()

                    console.log(data)

                    if (data.status === 200) {
                        setStore({ currentUser: data, error: null })
                        sessionStorage.setItem('currentUser', JSON.stringify(data))
                        navigate('/')
                    } else {
                        setStore({ error: data, currentUser: null })
                        navigate('/login')
                    }

                } catch (error) {
                    console.log(error);
                }
            },
            logout: (navigate) => {
                if (sessionStorage.getItem('currentUser')) {
                    setStore({
                        currentUser: null,
                        error: null
                    })
                    sessionStorage.removeItem('currentUser')
                }
                navigate('/login')
            },
            register: () => {

            },
            checkCurrentUser: () => {
                if (sessionStorage.getItem('currentUser')) {
                    const currentUser = JSON.parse(sessionStorage.getItem('currentUser'))
                    setStore({
                        currentUser
                    })
                }
            },
            getMessages: async () => {
                try {
                    const { currentUser, API_URL } = getStore();
                    const options = {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${currentUser?.data?.access_token}`
                        }
                    }

                    const response = await fetch(`${API_URL}/api/messages`, options)
                    const data = await response.json()

                    if (data.status === 200) {
                        setStore({ messages: data, error: null })
                    } else {
                        console.log(data)
                        setStore({ error: data, messages: null })
                    }

                } catch (error) {

                }
            },
            uploadAvatar: async e => {
                e.preventDefault()
                try {
                    const { file, currentUser, API_URL } = getStore();

                    const formData = new FormData();
                    formData.append('avatar', file);

                    const options = {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'Authorization': `Bearer ${currentUser?.data?.access_token}`
                        }
                    }

                    const response = await fetch(`${API_URL}/api/avatar`, options)

                    const data = await response.json()

                    const { result } = data;

                    console.log(result)
                    console.log(currentUser)

                    currentUser.data.user = result // actualizamos currentUser con la nueva informacion del usuario
                    setStore({ currentUser }); // guardamos la informacion en el store
                    sessionStorage.setItem('currentUser', JSON.stringify(currentUser)); // actualizamos la informacion en el sessionStorage

                } catch (error) {
                    console.log(error);
                }


            },
            sendEmail: (e, emailjs) => {
                e.preventDefault();
                const { SERVICES_ID, TEMPLATE_ID, PUBLIC_KEY } = getStore();

                emailjs.sendForm(SERVICES_ID, TEMPLATE_ID, e.target, PUBLIC_KEY)
                    .then((result) => {
                        console.log(result.text)
                        setStore({ success: { message: 'Email sent successfully' }, error: null })
                        e.target.reset();
                    }, (error) => {
                        console.log(error.text)
                        setStore({ error: { message: 'Error, try again later' }, success: null })
                        e.target.reset();
                    })

            }
        }
    }
}

export default getState;