import axios from 'axios'
import router from '../router'

const DOMAIN = 'https://server-msvml.run.goorm.io'
const UNAUTHORIZED = 401
const onUNAUTHORIZED = () => {
    router.push('/login')
}

const request = (method, url, data) => {
    return axios({
        method,
        url: DOMAIN + url,
        data
    }).then(result => result.data)
    .catch(result => {
        const {status} = result.response
        if (status === UNAUTHORIZED) return onUNAUTHORIZED()
        throw Error(result)
    })
}

export const board = {
    fetch() {
        return request('get', '/boards')
    }
}