<template>
	<view>
	
			<!-- 头部logo -->
			<view class="person-head main" v-if="num!=0">
			  <!-- <cmd-avatar src="https://avatar.bbs.miui.com/images/noavatar_small.gif" @click="fnInfoWin" size="lg" :make="{'background-color': '#fff'}"></cmd-avatar> -->
			  <view class="person-head-box">
			    <view class="person-head-nickname">
					
						<view>用户您好！</view>
						<view>您目前可用许可证为:9836482746</view>
						<view>可用数量：50</view>
				</view>
			 
				<wButton
								text="退出登录"
								:rotate="isRotate" 
								@click.native="gologin"
								class="wbutton"
							></wButton>
			  </view>
			</view>
			
			<!-- 主体表单 -->
		<view v-else>
			<view class="person-head main">
			  <!-- <cmd-avatar src="https://avatar.bbs.miui.com/images/noavatar_small.gif" @click="fnInfoWin" size="lg" :make="{'background-color': '#fff'}"></cmd-avatar> -->
			  <view class="person-head-box">
			    <view class="person-head-nickname">
					
						<view>用户您好！</view>
						<view>您目前没有可用许可证，请购买</view>
				</view>
			 
				<wButton
								text="退出登录"
								:rotate="isRotate" 
								@click.native="gologin"
								class="wbutton"
				></wButton>
			  </view>
			</view>
			
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
				@click.native="getLicense()"
				class="wbutton"
			></wButton>
			</view>
			
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
		onLoad(option){
			console.log(option)
			this.usrID=option.usrID
			this.num=option.num
			this.data=option.data
		},
		data() {
			return {
				num:0,
				data:null,
				usrID:null
				
			};
		},
		components:{
			wInput,
			wButton,
		},
		computed: mapState(['userInfo']),
		
		mounted() {
			_this= this;
			//this.isLogin();
		},
		methods: {
			getLicense:function(){
				
			},
			ratioChange: function(evt){
				console.log(evt.detail.value)
			},
			gologin:function(){
							uni.reLaunch({
								url:"../login/login"
							})
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
	    height: 1000px;
	    padding-left: 20px;
	    background: linear-gradient(to bottom, #c9ffe6, #eefffa);
	  }
	
	  .person-head-box {
	    display: flex;
	    flex-direction: column;
	    justify-content: center;
	    align-items: flex-start;
	    margin-left: 10px;
	  }
	
	  .person-head-nickname {
	    font-size: 40px;
	    font-weight: 500;
	    color: #000069;
	  }
	
	  .person-head-username {
	    font-size: 30px;
	    font-weight: 500;
	    color: #000069;
	  }
	
	  .person-list {
	    line-height: 0;
	  }
	
</style>