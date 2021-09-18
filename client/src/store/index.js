import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    user: null,
    selectedClassroom: null,
  },
  mutations: {
    SET_USER_DATA(state, userData) {
      localStorage.setItem("user", JSON.stringify(userData));
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${userData.token}`;
      state.user = userData;
    },
    CLEAR_USER_DATA() {
      localStorage.removeItem("user");
      location.reload();
    },
    SET_CLASSROOM(state, classroom) {
      state.classroom = classroom;
    },
  },
  actions: {
    register({ commit }, credentials) {
      return axios
        .post("//localhost:3000/register", credentials)
        .then(({ data }) => {
          commit("SET_USER_DATA", data);
        });
    },
    login({ commit }, credentials) {
      return axios
        .post(`http://127.0.0.1:8000/api/auth/login/`, credentials)
        .then(({ data }) => {
          console.log(data);
          commit("SET_USER_DATA", data);
        });
    },
    logout({ commit }) {
      commit("CLEAR_USER_DATA");
    },
    selectClassroom({ commit }, classroom) {
      commit("SET_CLASSROOM", classroom);
    },
  },
  modules: {},
  getters: {
    loggedIn(state) {
      return !!state.user;
    },
    classroom_id(state) {
      return state.selectClassroom.id;
    },
  },
});
