$(function() {
    var shrinkHeader = 300;
    $(window).scroll(function() {
        var scroll = getCurrentScroll();
        if (scroll >= shrinkHeader) {
            $('.header').addClass('shrink');
            $('#logo_img').addClass('hide');
            $('.test').addClass('hide');
            $('#title').addClass('change');
            $('#h1').addClass('change');
        } else {
            $('.header').removeClass('shrink');
            $('#logo_img').removeClass('hide');
            $('#title').removeClass('change');
            $('#h1').removeClass('change');
            $('.test').removeClass('hide');
        }
    });

    function getCurrentScroll() {
        return window.pageYOffset;
    }
});