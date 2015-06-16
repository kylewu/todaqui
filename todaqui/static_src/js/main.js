$(function() {
  $(".search-tabs li").each(function() {
    $(this).click(function() {
      $(".search-tabs li").removeClass("active");
      $(this).addClass("active");

      var action = "";
      if ($(this).hasClass("web")) {
        action = "http://google.com/search?";
        $("#search-input").attr("name", "q");

      } else if ($(this).hasClass("video")){
        action = "http://google.com/search?";
        $("#search-input").attr("name", "q");

      } else if ($(this).hasClass("image")) {
        action = "http://google.com/search?";
        $("#search-input").attr("name", "q");

      } else if ($(this).hasClass("map")) {
        action = "http://google.com/search?";
        $("#search-input").attr("name", "q");

      } else if ($(this).hasClass("wiki")) {
        action = "http://google.com/search?";
        $("#search-input").attr("name", "q");

      } else if ($(this).hasClass("translate")) {
        action = "http://translate.google.com/?";
        $("#search-input").attr("name", "q");
      }

      $("#search-form").attr("action", action);
    });
  });
});
