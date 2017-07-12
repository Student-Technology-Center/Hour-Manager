$(document).ready(function() {
    if (sessionStorage.getItem('menu-state') !== 'open') {
        $(".menu").animate({width:"200px"});
        $(".menu a").delay(800).animate({opacity:"1"});
        sessionStorage.setItem('menu-state','open');
    } else {
        $(".menu").css({"transition":"0s","width":"200px"});
        $(".menu a").css({"transition":"0s","opacity":"1"});
    }
});