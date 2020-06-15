import React from 'react';

// function Hello(props) {
//     console.log(props);
//     return <div style={{
//         color: props.color
//     }}>안녕하세요 {props.name}</div>;
// } 

function Hello({ color, name, isSpecial }) {
    return (
        <div style={{
            color
        }}>
            <b>{isSpecial? '스페셜하다!': '낫스페셜' }</b>
            {/* {isSpecial ? <b>*</b> : null} */}
            {isSpecial && <b>*</b>}
            {null}
            {false}
            {undefined}
            {0}
            안녕하세요 {name}
        </div>
    );
} 

Hello.defaultProps = {
    name: '이름없음'     
};

export default Hello;