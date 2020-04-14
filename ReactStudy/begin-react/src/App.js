import React from 'react';
import Hello from './Hello';
import Wrapper from './Wrapper';
import Counter from './Counter';
import InputSample from './InputSample';
import InputSample2 from './InputSample2';


function App() {
  return (
    <Wrapper>
      {/* <Hello name="react" color="red" isSpecial={true} /> */}
      <Hello name="react" color="red" isSpecial />
      <Hello color="pink" />

      <Counter />
      <InputSample />
      <InputSample2 />
    </Wrapper>
  )
}

export default App;
