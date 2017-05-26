$(document).ready(function(){
    $(".menu a").hide(),
    $(".menu").animate({width: "10%" },
    function() {
        $(".menu a").show()
    });
    $(".reasontd").hide();
});

$(document).ready(function() {
    $("tr").mouseover(function() {
        $(this).find('.reasontd').show().css({
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