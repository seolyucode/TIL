import React from 'react';
import Hello from './Hello';
import './App.css';
import Wrapper from './Wrapper';

function App() {
  const name = 'react';
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSize: 24,
    padding: '1rem'
  }
  return (
    <Wrapper>
      {/* 주석 */}
      <Hello name="react" color="red" isSpecial={true}
        // 주석
      />
      <Hello name="react" color="red" isSpecial />
      <Hello color="pink" />
      <div>안녕히계세요.</div>
      <div
        // 주석
      style={style}>{name}</div>
      <div className="gray-box"></div>
    </Wrapper>
  );
}

export default App;
