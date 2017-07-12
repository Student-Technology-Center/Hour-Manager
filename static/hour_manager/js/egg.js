function randRGB() {
    var first = Math.ceil((Math.random() * 255)).toString();
    var second = Math.ceil((Math.random() * 255)).toString();
    var third = Math.ceil((Math.random() * 255)).toString();

    return "rgb(" + first + "," + second + "," + third + ")";
}

function changeColor() {
    $("body").css({
            "background-color": randRGB(),
    });
}

setInterval(function() { changeColor() }, 1000)