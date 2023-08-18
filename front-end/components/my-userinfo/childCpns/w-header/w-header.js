// pages/profile/childCpns/w-header/w-header.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {

  },

  /**
   * 组件的初始数据
   */
  data: {

  },
  lifetimes:{
    attached:function(){
      const userInfo=wx.getStorageSync('userInfo')
      this.setData({userInfo:userInfo})
    }
  },
  /**
   * 组件的方法列表
   */
  methods: {

  }
})
