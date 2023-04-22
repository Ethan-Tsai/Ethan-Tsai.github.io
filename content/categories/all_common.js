$(function() {
    var shrinkHeader = 300;
    $(window).scroll(function() {
        var scroll = getCurrentScroll();
        if (scroll >= shrinkHeader) {
            $('.header').addClass('shrink');
            $('#logo_img').addClass('hide');
        } else {
            $('.header').removeClass('shrink');
            $('#logo_img').removeClass('hide');
        }
    });

    function getCurrentScroll() {
        return window.pageYOffset;
    }
});