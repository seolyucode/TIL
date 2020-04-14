import React, { useEffect } from 'react';

const User = React.memo(function User({ user, onRemove, onToggle }) {
    const { username, email, id, active } = user;

    useEffect(() => {
        // console.log(user);
        return () => {

        }
    }, [user]);

    // useEffect(() => {
    //     console.log('user 값이 설정됨');
    //     console.log(user);
    //     return () => {
    //         console.log('user 값이 바뀌기 전');
    //         console.log(user);
    //     }
    // }, [user]);

    // useEffect(() => {
    //     console.log('컴포넌트가 화면에 나타남');
    //     // props -> state
    //     // REST API
    //     // D3 Video.js
    //     // setInterval, setTimeout
    //     return () => {
    //         // clearInterval, clearTimeout
    //         // 라이브러리 인스턴스 제거
    //         console.log('컴포넌트가 화면에서 사라짐');
    //     }
    // }, []);
    return (
        <div>
            <b style={{
                color: active ? 'dodgerblue' : 'black',
                cursor: 'pointer'
                }}
                onClick={() => onToggle(id)}
            >
                {username}
            </b>
            &nbsp;
            <span>({email})</span>
            <button onClick={() => onRemove(id)}>삭제</button>
        </div>  
    );
});

function UserList({ users, onRemove, onToggle }) {
    // const users = [
    //     {
    //         id: 1,
    //         username: 'Seolyu',
    //         email: 'seolyu.90@gmail.com'
    //     },
    //     {
    //         id: 2,
    //         username: 'tester',
    //         email: 'tester@example.com'
    //     },
    //     {
    //         id: 3,
    //         username: 'liz',
    //         email: 'liz@example.com'
    //     }
    // ];

    return (
        <div>
            {/* <div>
                <b>{users[0].username}</b> <span>({users[0].email})</span>
            </div>
            <div>
                <b>{users[1].username}</b> <span>({users[1].email})</span>
            </div>
            <div>
                <b>{users[2].username}</b> <span>({users[2].email})</span>
            </div> */}

            {/* <User user={users[0]}/>
            <User user={users[1]}/>
            <User user={users[2]}/> */}

            {
                users.map(
                    // (user, index) =>(<User user={user} key={index} />)
                    (user, index) => (
                        <User 
                            user={user} 
                            key={user.id} 
                            onRemove={onRemove}
                            onToggle={onToggle}
                        />
                    )
                )
            }
        </div>
    )
}

// 컴포넌트 리렌더링 방지위해 React.memo
export default React.memo(
    UserList, 
    (prevProps, nextProps) => nextProps.users === prevProps.users
);