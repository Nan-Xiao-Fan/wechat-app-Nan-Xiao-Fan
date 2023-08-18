Page({
  data: {
    autoplay: true,
    interval: 3000,
    duration: 500,
    swiperData: []
  },
  onLoad: function () {
    // 发起网络请求获取轮播图数据
    this.getSwiper();
  },
  onClickRight: function () {
    // 用户点击了右侧按钮，执行跳转逻辑
    wx.switchTab({
      url: '/pages/order/order'
    })
  },
  scanCode(){
  wx.scanCode({
    onlyFromCamera: false,
    success: (result) => {},
    fail: (res) => {},
    complete: (res) => {},
  })}
  ,
  showCode(){
    wx.showToast({
      title: '由服务器生成',
    })
  }
,
  getSwiper: function() {
    wx.request({
      url: 'http://127.0.0.1:8000/api/swiper', // 替换为实际的接口地址
      method: 'GET',
      success: (res) => {
        // 请求成功，将数据设置到lunboData中
        this.setData({
          swiperData: res.data
        });
      },
      fail: (err) => {
        // 请求失败的处理逻辑
        console.error('请求失败', err);
      }
    })
  }
});