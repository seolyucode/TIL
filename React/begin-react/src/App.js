import React from 'react';
import Hello from './Hello';
import './App.css';
import Wrapper from './Wrapper';
import Counter from './Counter';
import InputSample from './inputSample';
import InputSample2 from './inputSample2';

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

      <Counter />
      <InputSample />
      <InputSample2 />
    </Wrapper>
  );
}

export default App;
