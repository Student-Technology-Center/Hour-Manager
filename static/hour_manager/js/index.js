$(document).ready(function(){
    $('tr').click(function(data) {
        //Gives the reason 
        console.log(data.currentTarget.children[6].innerHTML);

        //Gives claim link
        console.log(data.currentTarget.children[5].children[0].getAttribute('href'))
    })
});