import axios from 'axios';

function registerUser(userData) {
    const url = 'https://vue-server.run.goorm.io/signup'
    return axios.post(url, userData);
}

export { registerUser };