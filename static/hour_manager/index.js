$(document).ready(function() {
    $("tr").mouseover(function() {
        $(this).find('.reasontd').css({
            "opacity":"1",
        });
    })
    $("tr").mouseout(function() {
        $(this).find('.reasontd').css({
            "opacity":"0"
        });
    })
});