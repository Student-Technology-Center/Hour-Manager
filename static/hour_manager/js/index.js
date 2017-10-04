$(document).ready(function(){
    $("tr").mouseover(function() {
        $(this).find('.reasontd').css({
            "opacity":"1",
        });
    })
    $("tr").mouseout(function(){
        $(this).find('.reasontd').css({
            "opacity":"0"
        });
    })
    $("#menu ul li").click(function() {
        window.location = $(this).children()[0].href;
    })
});