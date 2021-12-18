import React, {FC, useContext} from 'react';
import axios from 'axios';
import {StoreContext} from './App';


// 表示するための子コンポーネント
const Screen: FC = () => {
    const {state, dispatch} = useContext(StoreContext);
    const clickHandler = async () => {
        dispatch({type: 'start'});
        try {
            const result = await axios.get('/api_server');
            if (result.status !== 200) {
                throw new Error('The request has failed');
            }
            dispatch({type: 'succeed', payload: {result}, error: true});
        } catch (error) {
            dispatch({type: 'error', payload: {error}, error: true});
        }
    }
    console.log("Status: ", state)
    return (
        <div>
            <div>Result: {JSON.stringify(state.result.data)}</div>
            {/*<div>Status: {state.result.data.status}</div>*/}
            {/*<div>Method: {state.result.data.method}</div>*/}
            {/*<div>Status_code: {state.result.data.status_code}</div>*/}
            <div>
                <button onClick={clickHandler}>データの取得</button>
            </div>
        </div>
    );
};

export default Screen;