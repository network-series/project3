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
		hasLogin: false,
		userName: "未登录",
		//baseURL: "https://api.exceeding.xyz/api-v1",
		baseURL: "http://127.0.0.1:8000",
		userInfo: {
			usrId:'',
			password:null,
			num:0,
			data:null
		},
		loginPage: "/pages/login/login",
		uid:'', 
		
		cookie:'',
		blankStr:'   ',
	},
	mutations: {
		setLogin(state) {
			state.userName = state.userInfo.name || '新用户';
			state.uid = state.userInfo.id;
			state.hasLogin = true;
			state.jon=state.userInfo.job;
			// console.log(state.cookie)
		},
		logout(state) {
			state.userInfo = defaultUserInfo;
			state.userName = state.userInfo.name;
			state.uid = state.userInfo.id;
			state.hasLogin = false;
			uni.request({
			    url: state.baseURL + '/logout',
				method:'GET',
			    success: (res) => {
			        uni.showToast({
			        	icon:'none',
						title:"登出成功"
			        });
					uni.switchTab({
						url:"/pages/profile/profile"
					})
					}
			    })
		},
		loginNeeded(state, forcedLogin = true){
			if (!state.hasLogin) {
				uni.showModal({
					title: '未登录',
					content: '您未登录，需要登录后才能继续',
					/**
					 * 如果需要强制登录，不显示取消按钮
					 */
					showCancel: !forcedLogin,
					success: (res) => {
						if (res.confirm) {
							/**
							 * 如果需要强制登录，使用reLaunch方式
							 */
							if (forcedLogin) {
								uni.navigateBack();
							} else {
								uni.navigateTo({
									url: state.loginPage
								});
							}
						}
					}
				});
			}
		},
		onworking(){
			uni.showToast({
				icon:'none',
				title:'功能施工中~~~'
			})
		},
		setCookie(state, cookie){
			state.cookie = cookie
		}
	}
})

export default store
