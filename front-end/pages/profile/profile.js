// pages/profile/profile.js
Page({
  data: {
    userInfo:null
  },
  onLoad: function (options) {
    const userInfo=getApp().globalData.userInfo;
    wx.setStorageSync('userInfo', userInfo)
  },
    // 监听登录组件触发的事件
    onUpdateUserInfo(e) {
      const userInfo = e.detail.userInfo;
      this.setData({
        userInfo: userInfo
      });
    },
})