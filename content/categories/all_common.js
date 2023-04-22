$(function() {
    var shrinkHeader = 300;
    $(window).scroll(function() {
        var scroll = getCurrentScroll();
        if (scroll >= shrinkHeader) {
            $('.header').addClass('shrink');
            $('#logo_img').addClass('hide');
            $('#title').addClass('change');
            $('#h1').addClass('change');
        } else {
            $('.header').removeClass('shrink');
            $('#logo_img').removeClass('hide');
            $('#title').removeClass('change');
            $('#h1').removeClass('change');
        }
    });

    function getCurrentScroll() {
        return window.pageYOffset;
    }
});