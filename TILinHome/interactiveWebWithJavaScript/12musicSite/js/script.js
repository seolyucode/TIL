function scrollHandler() {
    var o = $(window).scrollTop() + $(window).height();
    $(".playlist").each(function () {
        var t = $(this);
        t.position().top + t.outerHeight() / 2 < o && t.animate({
            opacity: "1"
        }, 1500)
    }), console.log($(document).height()), console.log(o), o == $(document).height() ? $(".to-top-btn").fadeIn() : $(".to-top-btn").fadeOut()
}
$(window).on("scroll", scrollHandler), scrollHandler(), $(".to-top-btn").on("click", function () {
    $("html, body").animate({
        scrollTop: 0
    }, 1e3)
});