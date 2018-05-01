var currentView;

var START_VIEW 		= 'give';
var CLAIM_VIEW 		= 'claim';
var HISTORY_VIEW 	= 'history';
var GIVE_VIEW 		= 'give';
var DASH_VIEW 		= 'dash';

views = [CLAIM_VIEW, HISTORY_VIEW, GIVE_VIEW]

$(document).ready(function() {
	//Opens first view..
	changeView(START_VIEW);

	$('.link-button').click(function() {
		if (this.id == 'home') {
			window.location = '/';
			return;
		}

		changeView(this.id);
	})
})

function changeView(newView) {

	$('#' + currentView + '-view').css({
		'opacity':0,
		'z-index':0
	})

	currentView = newView;

	$('#' + currentView + '-view').css({
		'opacity':1,
		'z-index':1000
	})
}