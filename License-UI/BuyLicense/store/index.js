import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

var defaultUserInfo = {
			usrId:'',
			password:null,
			num:0,
			data:null
		}

const store = new Vuex.Store({
	state: {
		userInfo: {
			usrId:'',
			password:null,
			num:0,
			data:null
		}
	}
export default store
