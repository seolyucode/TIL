import React from 'react';

function Hello({ color, name, isSpecial }) {
    return (
        <div style={{
            color
        }}>
            {/* {isSpecial ? <b>*</b> : null} */}
            {/* {undefined} */}
            {/* {0} */}
            {isSpecial && <b>^_^</b>}
            <b>{isSpecial ? '스페셜하다!': '낫스페셜'}</b>
            안녕하세요 {name}
        </div>
    );
}

Hello.defaultProps = {
    name: '이름없음'
};
export default Hello;