import React, { useRef, useReducer, useState, useMemo, useCallback, createContext } from 'react';
import produce from 'immer';
import Hello from './Hello';
import Wrapper from './Wrapper';
import Counter from './Counter';
import InputSample from './InputSample';
import InputSample2 from './InputSample2';
import UserList from './UserList';
import CreateUser from './CreateUser';
import useInputs from './useInputs';

window.produce = produce;

function countActiveUsers(users) {
  console.log('활성 사용자 수를 세는 중...');
  return users.filter(user => user.active).length;
};

const initialState = {
  // inputs: {
  //   username: '',
  //   email:'',
  // },
  users: [
    {
        id: 1,
        username: 'Seolyu',
        email: 'seolyu.90@gmail.com',
        active: true,
    },
    {
        id: 2,
        username: 'tester',
        email: 'tester@example.com',
        active: false,
    },
    {
        id: 3,
        username: 'liz',
        email: 'liz@example.com',
        active: false,
    }
  ]
}

function reducer(state, action) {
  // return state;
  switch (action.type) {
  //   case 'CHANGE_INPUT':
  //     return {
  //       ...state,
  //       inputs: {
  //         ...state.inputs,
  //         [action.name]: action.value
  //       }
  //     };
    
    case 'CREATE_USER':
      return produce(state, draft => {
        draft.users.push(action.user);
      });
      // return {
      //   inputs: initialState.inputs,
      //   users: state.users.concat(action.user)
      // }
    
    case 'TOGGLE_USER':
      return produce(state, draft => {
        const user = draft.users.find(user => user.id === action.id);
        user.active = !user.active;
      });
      // return {
      //   ...state,
      //   users: state.users.map(user =>
      //     user.id === action.id
      //       ? { ...user, active: !user.active }
      //       : user
      //     )
      // }
      
    case 'REMOVE_USER':
      return produce(state, draft => {
        const index = draft.users.findIndex(user => user.id === action.id);
        draft.users.splice(index, 1);
      });
      // return {
      //   ...state,
      //   users: state.users.filter(user => user.id !== action.id)
      // }

    default:
      throw new Error('Unhandled action');
  }
}

export const UserDispatch = createContext(null);

function App() {
  // const [inputs, setInputs] = useState({
  //   username: '',
  //   email: '',
  // });

  // const { username, email } = inputs;
  // const onChange = useCallback(e => {
  //   const { name, value } = e.target;
  //   setInputs({
  //     ...inputs,
  //     [name]: value
  //   });
  // }, [inputs]);

  // const [users, setUsers] = useState([
  //   {
  //       id: 1,
  //       username: 'Seolyu',
  //       email: 'seolyu.90@gmail.com',
  //       active: true,
  //   },
  //   {
  //       id: 2,
  //       username: 'tester',
  //       email: 'tester@example.com',
  //       active: false,
  //   },
  //   {
  //       id: 3,
  //       username: 'liz',
  //       email: 'liz@example.com',
  //       active: false,
  //   }
  // ]);

  // const nextId = useRef(4);

  // const onCreate = useCallback(() => {
  //   const user = {
  //     id: nextId.current,
  //     username,
  //     email,
  //   };
  //   // setUsers([...users, user]);
  //   setUsers(users => users.concat(user));
  //   setInputs({
  //     username: '',
  //     email: ''
  //   });

  //   console.log(nextId.current);  // 4
  //   nextId.current += 1;
  // }, [username, email]);

  // const onRemove = useCallback(id => {
  //   setUsers(users => users.filter(user => user.id !== id));
  // }, []);

  // // 특정 함수를 재사용하기 위해 useCallback
  // const onToggle = useCallback(id => {
  //   setUsers(users => users.map(
  //     user => user.id === id
  //       ? { ...user, active: !user.active }
  //       : user
  //   ));
  // }, []);

  // // 연산된 값을 재사용하기 위해 useMemo
  // const count = useMemo(() => countActiveUsers(users), [users]);

  const [state, dispatch] = useReducer(reducer, initialState);
  // const [form, onChange, reset] = useInputs({
  //   username: '',
  //   email: '',
  // });
  // const { username, email } = form;
  // const nextId = useRef(4);
  const { users } = state;
  // const { username, email } = state.inputs;

  // const onChange = useCallback(e => {
  //   const { name, value } = e.target;
  //   dispatch({
  //     type: 'CHANGE_INPUT',
  //     name,
  //     value
  //   })
  // }, []);

  // const onCreate = useCallback(() => {
    // dispatch({
  //     type: 'CREATE_USER',
  //     user: {
  //       id: nextId.current,
  //       username,
  //       email,
  //     }
    // });
    // nextId.current += 1;
    // reset();
  // }, [username, email, reset]);

  // const onToggle = useCallback(id => {
  //   dispatch({
  //     type: 'TOGGLE_USER',
  //     id
  //   });
  // }, []);

  // const onRemove = useCallback(id => {
  //   dispatch({
  //     type: 'REMOVE_USER',
  //     id
  //   });
  // }, []);

  const count = useMemo(() => countActiveUsers(users), [users])

  return (
    <UserDispatch.Provider value={dispatch}>
    {/* <Wrapper> */}
      {/* <Hello name="react" color="red" isSpecial={true} /> */}
      {/* <Hello name="react" color="red" isSpecial />
      <Hello color="pink" />

      <Counter />
      <InputSample />
      <InputSample2 /> */}

      <CreateUser 
        // username={username} 
        // email={email} 
        // onChange={onChange} 
        // onCreate={onCreate} 

        // username={username}
        // email={email}
        // onChange={onChange}
        // onCreate={onCreate}
      />
      {/* <UserList users={users} onRemove={onRemove} onToggle={onToggle} /> */}
      <UserList users={users} 
        // onToggle={onToggle} 
        // onRemove={onRemove} 
      />
      {/* <div>활성 사용자 수: {count}</div> */}
      <div>활성 사용자 수: {count}</div>
    {/* </Wrapper> */}
    </UserDispatch.Provider>
  )
};

export default App;
