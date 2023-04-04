import { createContext, useEffect, useState } from "react";
import getState from "./flux";

export const Context = createContext(null);

const injectContext = (PassedComponent) => {
    const StoreWrapper = (props) => {

        const [state, setState] = useState(getState({
            getStore: () => state.store,
            getActions: () => state.actions,
            setStore: (updateStore) => setState({
                store: Object.assign(state.store, updateStore),
                actions: { ...state.actions }
            })
        }))

        useEffect(() => {
            /* Llamadas a funciones al momento de cargar la pagina */
            state.actions.checkCurrentUser();
            if(state.store.currentUser !== null){
                state.actions.getMessages()
            }
        }, [])

        useEffect(() => {
            if(state.store.currentUser !== null){
                state.actions.getMessages()
            }
        }, [state.store.currentUser])

        return (
            <Context.Provider value={state}>
                <PassedComponent />
            </Context.Provider>
        )
    }

    return StoreWrapper;
}

export default injectContext;
