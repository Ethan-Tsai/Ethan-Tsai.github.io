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

window.onscroll = function() { myFunction() };

function myFunction() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("myBar").style.width = scrolled + "%";
}