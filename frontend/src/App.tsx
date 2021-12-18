import React, {FC, useReducer, createContext} from 'react';
import './App.css';
import axios, {AxiosError, AxiosResponse} from "axios";
import Screen from "./Screen";

// axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'https://etude-gae.an.r.appspot.com/';

interface StateProps {
    result: AxiosResponse;
    isLoading: boolean;
    error?: AxiosError | null;
}

interface ActionProps {
    type: string;
    payload?: any;
    error?: boolean;
}

const initialState: StateProps = {
    result: {} as AxiosResponse,
    isLoading: false,
};

const reducer = (state: StateProps = initialState, action: ActionProps) => {
    switch (action.type) {
        case 'start':
            return {
                ...state,
                isLoading: true,
            };
        case 'succeed':
            return {
                ...state,
                result: action.payload?.result,
                isLoading: false,
            };
        case 'error':
            return {
                ...state,
                result: action.payload?.error,
                isLoading: false,
            };
        default:
            throw new Error();
    }
};

interface StoreContextProps {
    state: StateProps;
    dispatch: ({type}: ActionProps) => void;
}

// Store
export const StoreContext = createContext({} as StoreContextProps);

// Render
const App: FC = () => {
    const [state, dispatch] = useReducer(reducer, initialState)
    console.log(state)

    return (
        <div className="App">
            <StoreContext.Provider value={{state, dispatch}}>
                <Screen/>
            </StoreContext.Provider>
        </div>
    );
}

export default App;