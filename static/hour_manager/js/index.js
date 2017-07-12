var editting = false;

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
    /*
    $("#editbtn").click(function(){
        if (editting)
            $("#editform").css({"display":"none","opacity":"0"});
        else
            $("#editform").css({"display":"block", "opacity":"1"});
        editting = !editting;
    });
    */
});