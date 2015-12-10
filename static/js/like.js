var main = function() {
  $(".like-button").click(function() {
    $(this).toggleClass("liked");
  });
};

$(document).ready(main);
