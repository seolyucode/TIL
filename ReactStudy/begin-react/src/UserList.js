import React from 'react';

function User({ user, onRemove, onToggle }) {
    const { username, email, id, active } = user;
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
}

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

export default UserList;