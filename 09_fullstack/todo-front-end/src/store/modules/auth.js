// auth.js  인증관련 모든 State 를 작성.
// State 에 접근/변경 하는 모든 로직은 여기로.
const state = {
    token: null,
};

// Vuex 에서는 Arrow Function
const getters = {
    isLoggedIn: state => !! state.token,  // 특정 값을 true/false 로 바꾸는 구문

};

const mutations = {
    setToken: (state, token) => state.token = token,
};

const actions = {
    logout: (options) => {
        // mutations.setToken(state, null)  === Very Bad
        options.commit('setToken', null)  // GREAT
    },
    // logout: ({ commit, a, b, c }) => {
    //     commit('setToken', null)
    // },

    login: ({ commit }, token) => {
        commit('setToken', token)
    }
};

export default {
    state, getters, mutations, actions
}