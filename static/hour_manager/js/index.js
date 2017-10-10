var claimLink;
var selectedTr;

function standardToMilitary(time) {
    if (time == "noon") {
        return "12:00";
    }

    console.log(time);

    var num;

    if (num != '0') {
        num = time.slice(0, 2);

        if (num.slice(1, 2) == ' '){
            var newNum = parseInt(num);
            newNum += 12;
            var num = newNum.toString();
            num += ":00";
        } else {
            num += ":00";
            return num;
        }
    }

    return num;
}

$(document).ready(function(){
    $('tr').click(function(data) {
        claimLink = data.currentTarget.children[5].children[0].getAttribute('href');
        selectedTr = $(this);

        $('#info-reason').css('display', 'block');
        $('#info-time').css('display', 'block');
        $('#info-reason p').text(data.currentTarget.children[6].innerHTML)

        var start = standardToMilitary(data.currentTarget.children[7].children[0].innerHTML);
        var end = standardToMilitary(data.currentTarget.children[7].children[1].innerHTML);

        $('#start_time').val(start);
        $('#end_time').val(end);
    })

    $('#claim-button').click(function () {
        var start = $('#start_time').val();
        var end = $('#end_time').val();

        if (start == "" || end == "") {
            $('#info-warning').text("Please enter a valid time")
            return;
        }

        $.ajax({
            url: claimLink,
            type: 'GET',
            data: {
                'start':start,
                'end':end,
            },
            success: function(data) {
                if (data.status == "success"){
                    selectedTr.remove();
                    $("#info-warning").text(data.reason);
                } else {
                    $('#info-warning').text(data.reason)
                }
            }
        })
    });
});