var main = function(){
    $(".item").click(function(){
        $(".item").removeClass.(".current");
        $(".description").hide();
        $(this).addClass('.current')
        $(this).children('.description').show();
    });
    $('.item').click((function(){
        $('item').removeClass.('.current');
        $('.current').children('.description').toggle();
    });
};
$(document).ready(main);
