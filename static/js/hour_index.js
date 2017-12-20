var currentView = 'claim'

var CLAIM_VIEW = 'claim'
var HISTORY_VIEW = 'history'
var GIVE_VIEW = 'give'

views = [CLAIM_VIEW, HISTORY_VIEW, GIVE_VIEW]

$(document).ready(function() {
	$('.link-button').click(function() {
		changeView(this.id);
	})
})

function changeView(newView) {

	$('#' + currentView + '-view').css({
		'opacity':0
	})

	currentView = newView;
	console.log(currentView)

	$('#' + currentView + '-view').css({
		'opacity':1
	})
}