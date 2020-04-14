// import React, { useState } from 'react';
import React, { useReducer } from 'react';

function reducer(state, action) {
    switch (action.type) {
        case 'INCREMENT':
            return state + 1;
        case 'DECREMENT':
            return state -1;
        default:
            throw new Error('Unhandled action');
    }
}

function Counter() {
    // 비구조화 할당, 구조 분해
    // const [number, setNumber] = useState(0);
    // const number = numberState[0];
    // const setNumber = numberState[1];

    const [number, dispatch] = useReducer(reducer, 0);

    const onIncrease = () => {
        // 업데이트 함수. 최적화. 함수형 업데이트.
        // setNumber((prevNumber => prevNumber + 1));
        dispatch({
            type: 'INCREMENT'
        })
    };
    
    const onDecrease = () => {
        // setNumber(number - 1);
        // setNumber((prevNumber => prevNumber - 1));
        dispatch({
            type: 'DECREMENT'
        })
    };

    return (
        <div>
            <h1>{number}</h1>
            <button onClick={onIncrease}>+1</button>
            <button onClick={onDecrease}>-1</button>
        </div>
    )
}

export default Counter;