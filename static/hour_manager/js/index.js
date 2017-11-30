var claimLink;
var selectedTr;

$(document).ready(function(){
    $('tr').click(function(data) {
        claimLink = data.currentTarget.children[5].children[0].getAttribute('href');
        selectedTr = $(this);

        $('#info-reason').css('display', 'block');
        $('#info-time').css('display', 'block');
        $('#info-reason p').text(data.currentTarget.children[6].innerHTML)

        var start = moment(data.currentTarget.children[7].children[0].innerHTML, 'h:mm a').format('HH:mm');
        var end = moment(data.currentTarget.children[7].children[1].innerHTML, 'h:mm a').format('HH:mm')

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