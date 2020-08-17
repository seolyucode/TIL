import axios from 'axios'
import router from '../router'

const DOMAIN = 'https://server-msvml.run.goorm.io'
const UNAUTHORIZED = 401
const onUNAUTHORIZED = () => {
    router.push(`/login?rPath=${encodeURIComponent(location.pathname)}`)
}

const request = (method, url, data) => {
    return axios({
        method,
        url: DOMAIN + url,
        data
    }).then(result => result.data)
    .catch(result => {
        const {status} = result.response
        if (status === UNAUTHORIZED) onUNAUTHORIZED()
        throw result.response
    })
}

export const setAuthInHeader = token => {
    axios.defaults.headers.common['Authorization'] = token ? `Bearer ${token}` : null;
}

export const board = {
    fetch() {
        return request('get', '/boards')
    }
}

export const auth = {
    login(email, password) {
        return request('post', '/login', {email, password})
    }
}