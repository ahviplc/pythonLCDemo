$(document).ready(function () {
    var login = $("#login");
    var register = $('#register');
    var denglu = $('#denglu');
    var zhuche = $('#zhuche');
    login.css('display', 'block');
    register.css('display', 'none');
    denglu.click(function () {
        zhuche.removeClass('active');
        denglu.addClass('active');
        register.css('z-index', '1');
        login.css('z-index', '2');
        register.hide();
        login.show();
    });
    zhuche.click(function () {
        denglu.removeClass('active');
        zhuche.addClass('active');
        register.css('z-index', '2');
        login.css('z-index', '1');
        register.show();
        login.hide();
    });

    $("#video1").click(function () {

        $.ajax({
            url: "static/json/json1.json", success: function (result) {
                $("#json1").html(result.title);
                $("#json2").html(result.content);
            }
        });

        var myPlayer = videojs("my-video");  //初始化视频-
        // myPlayer.src("/static/video/video1.mp4");  //重置video的src
        myPlayer.src("http://183.60.197.31/18/h/s/f/x/hsfxcvlpdyekwvmfviojesomfaejdp/hd.yinyuetai.com/8E2901681184AA884ED516806665AC75.mp4");  //重置video的src


    });

    $("#video2").click(function () {

        $.ajax({
            url: "static/json/json2.json", success: function (result) {
                $("#json1").html(result.title);
                $("#json2").html(result.content);
            }
        });


        var myPlayer = videojs("my-video");  //初始化视频
        // myPlayer.src("/static/video/video2.mp4");  //重置video的src
        myPlayer.src("http://221.228.226.18/6/w/m/k/j/wmkjorsxqehaqpnidchewdpwrczepl/hd.yinyuetai.com/B5B4015B8FDBD4CC82E32F491D41DA00.mp4");  //重置video的src
    });
    $("#video3").click(function () {

        $.ajax({
            url: "static/json/json3.json", success: function (result) {
                $("#json1").html(result.title);
                $("#json2").html(result.content);
            }
        });
        var myPlayer = videojs("my-video");  //初始化视频
        // myPlayer.src("/static/video/video3.mp4");  //重置video的src
        myPlayer.src("http://221.228.226.13/13/a/p/l/f/aplfwflvchflloswzdrdojkgcqkzod/hd.yinyuetai.com/B4A601617437EE2E5E301E2CC1214A75.mp4");

    });

    $("#video4").click(function () {

        $.ajax({
            url: "static/json/json4.json", success: function (result) {
                $("#json1").html(result.title);
                $("#json2").html(result.content);
            }
        });
        var myPlayer = videojs("my-video");  //初始化视频
        // myPlayer.src("/static/video/video4.mp4");  //重置video的src
        myPlayer.src("http://183.60.197.29/16/z/a/g/u/zaguxbrdvfydqxbrtfjdvuclzvwnys/hd.yinyuetai.com/F45C01641DFB08B90FE1575A49923EE0.mp4");  //重置video的src

    });

    $("#video5").click(function () {

        $.ajax({
            url: "static/json/json5.json", success: function (result) {
                $("#json1").html(result.title);
                $("#json2").html(result.content);
            }
        });

        var myPlayer = videojs("my-video");  //初始化视频
        // myPlayer.src("/static/video/video5.mp4");  //重置video的src
        myPlayer.src("http://112.253.22.165/28/x/j/v/e/xjvefbxiewvdxpbhgaukfzthyxknrs/hc.yinyuetai.com/1AB801636BF1BF4F4A9D327A6596E510.mp4");  //重置video的src

    });
});
