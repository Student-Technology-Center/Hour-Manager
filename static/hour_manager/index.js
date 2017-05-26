$(document).ready(function(){
    $(".menu a").hide(),
    $(".menu").animate({width: "10%" },
    function() {
        $(".menu a").show()
    });
});

$(document).ready(function() {
    $("tr").mouseover(function() {
        $(this).find('.reasontd').show().css({
            "position":"fixed",
            "color":"white",
        });
    }).mouseout(function() {
        $(this).find('.reasontd').hide()
    })
});