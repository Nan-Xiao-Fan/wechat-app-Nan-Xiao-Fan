// components/my-login/my-login.js
import Toast from '@vant/weapp/toast/toast'
Component({
  /**
   * 组件的属性列表
   */
  properties: {

  },

  /**
   * 组件的初始数据
   */

  /**
   * 组件的方法列表
   */
  methods: {
    //用户授权之后获取用户的基本信息
    getUserInfo(e) {
      console.log(e);
      if (e.detail.errMsg === 'getUserProfile:ok') {
        const userInfo = e.detail.userInfo;
        wx.setStorageSync('userInfo', userInfo)
        this.triggerEvent('updateUserInfo', {
          userInfo
        });
        Toast.success({
          message: '授权成功',
          context: this
        })
      } else if (e.detail.errMsg === "getUserProfile:fail auth deny") {
        Toast.fail({
          message: '您取消了授权',
          context: this
        });
      }
    },

  }
})