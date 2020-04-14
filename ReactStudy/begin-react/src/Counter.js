import React, { useState } from 'react';

function Counter() {
    // 비구조화 할당, 구조 분해
    const [number, setNumber] = useState(0);
    // const number = numberState[0];
    // const setNumber = numberState[1];

    const onIncrease = () => {
        // 업데이트 함수. 최적화. 함수형 업데이트.
        setNumber((prevNumber => prevNumber + 1));
    }
    
    const onDecrease = () => {
        // setNumber(number - 1);
        setNumber((prevNumber => prevNumber - 1));
    }

    return (
        <div>
            <h1>{number}</h1>
            <button onClick={onIncrease}>+1</button>
            <button onClick={onDecrease}>-1</button>
        </div>
    )
}

export default Counter;