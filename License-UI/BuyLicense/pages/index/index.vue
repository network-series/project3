<template>
	<view>
	
			<!-- 头部logo -->
			<view class="person-head">
			  <!-- <cmd-avatar src="https://avatar.bbs.miui.com/images/noavatar_small.gif" @click="fnInfoWin" size="lg" :make="{'background-color': '#fff'}"></cmd-avatar> -->
			  <view class="person-head-box">
			    <view class="person-head-nickname">
					
						<view>用户您好！</view>
						
					
				</view>
			 
				<button class="btn-logout" @click="logout">退出登录</button>
				
			  </view>
			</view>
			
			<!-- 主体表单 -->
		
			
			
			<view class="uni-padding-wrap" style="text-align: center; margin-top: 10%;">
			        <radio-group @change="ratioChange">
			            <view>
			                <label class="radio"><radio value='10' />10人</label>
			                <label class="radio"><radio value='50' />50人</label>
			            </view>
			       </radio-group> 
			</view>
			
			<wButton 
				text="获取许可证"
				:rotate="isRotate" 
				@click.native="startLogin()"
				class="wbutton"
			></wButton>
			
	</view>
</template>

<script>
	
	
	var _this;
	import wInput from '../../components/watch-login/watch-input.vue' //input
	import wButton from '../../components/watch-login/watch-button.vue' //button
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	
	import {
	    mapState,
		mapMutations
	} from 'vuex'
	export default {
		components: {uniNavBar},
		data() {
			return {
				usrID
				
			};
		},
		components:{
			wInput,
			wButton,
		},
		computed: mapState(['userName', 'baseURL', 'loginPage', 'userInfo', 'hasLogin', 'cookie']),
		
		mounted() {
			_this= this;
			//this.isLogin();
		},
		methods: {
			...mapMutations(['loginNeeded','setLogin','onworking','logout']),
			
			ratioChange: function(evt){
				console.log(evt.detail.value)
			}
		}
	}
</script>

<style>
	@import url("../../components/watch-login/css/icon.css");
	@import url("../../pages/login/css/main.css");
	
	  .person-head {
	    display: flex;
	    flex-direction: row;
	    align-items: center;
	    height: 260px;
	    padding-left: 20px;
	    background: linear-gradient(to bottom, #75ffd8, #c6ffe0);
	  }
	
	  .person-head-box {
	    display: flex;
	    flex-direction: column;
	    justify-content: center;
	    align-items: flex-start;
	    margin-left: 10px;
	  }
	
	  .person-head-nickname {
	    font-size: 18px;
	    font-weight: 500;
	    color: #000069;
	  }
	
	  .person-head-username {
	    font-size: 14px;
	    font-weight: 500;
	    color: #000069;
	  }
	
	  .person-list {
	    line-height: 0;
	  }
	  .btn-logout {
	  	margin-top: 20%;
	  	width: 100%;
	  	border-radius: 50upx;
	  	font-size: 15px;
	  	color: #005500;
	  	background: linear-gradient(to right, #ffdc5e, #ffff7f);
	  }
</style>
