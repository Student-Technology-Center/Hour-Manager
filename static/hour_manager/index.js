$(document).ready(function() {
    $(".menu").animate({width:"200px"});
    $(".menu a").delay(800).animate({opacity:"1"});
    $(".reasontd").hide();
});

$(document).ready(function() {
    $("tr").mouseover(function() {
        $(this).find('.reasontd').css({
            "z-index":"1",
            "position":"relative",
            "overflow-x":"visible",
            "overflow-y":"hidden",
            "color":"white",
        });
    }).mouseout(function() {
        $(this).find('.reasontd').hide()
    })
});