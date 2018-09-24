$(document).ready(function() {

	$('.ui.accordion').accordion('setting', { animateChildren: false, duration: 0});
	$('.ui.dropdown').dropdown();


	// Setup CSRF authentication for the POST methods
    // Ripped straight from Django docs
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $('.claim-shift').click(function() {
    	
    	shift_pk = $(this).attr('value');

    	start_time = $("#claim_start_" + shift_pk).text();
    	end_time = $("#claim_end_" + shift_pk).text();

    	claim_data = {'pk':shift_pk, 'start_time':start_time, 'end_time':end_time}
    	
    	$.ajax({
    		type: 'POST',
    		url: '/hourmanager/api/claim/',
    		data: claim_data,
    		success: function(data){
    			location.reload();
    		}
    	});

    });

    $('.delete-shift').click(function() {
    	shift_pk = $(this).parents('tbody').attr('value');
    	
    	$.ajax({
    		type: 'GET',
    		url: '/hourmanager/api/delete/' + shift_pk + '/',
    		success: function(data){
    			location.reload();
    		}
    	});
    });
});