window.onload = function() {
    $('.chinese_text').addClass('show');
    $('.section-title h2.chi').addClass('emph');
    $('.section-title span.eng').addClass('nor');
    $(".eng").click(function() {
        $('.english_text').addClass('show');
        $('.chinese_text').removeClass('show');
        $('.section-title span.eng').removeClass('nor');
        $('.section-title span.eng').addClass('emph');
        $('.section-title h2.chi').removeClass('emph');
        $('.section-title h2.chi').addClass('nor');
    });
    $(".chi").click(function() {
        $('.english_text').removeClass('show');
        $('.chinese_text').addClass('show');
        $('.section-title span.eng').removeClass('emph');
        $('.section-title span.eng').addClass('nor');
        $('.section-title h2.chi').removeClass('nor');
        $('.section-title h2.chi').addClass('emph');
    });


}