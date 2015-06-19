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

  //
/*
  $('#bookmark').click(function(e) {
    var bookmarkURL = window.location.href;
    var bookmarkTitle = document.title;
    var triggerDefault = false;

    if (window.sidebar && window.sidebar.addPanel) {
        // Firefox version < 23
        window.sidebar.addPanel(bookmarkTitle, bookmarkURL, '');
    } else if ((window.sidebar && (navigator.userAgent.toLowerCase().indexOf('firefox') > -1)) || (window.opera && window.print)) {
        // Firefox version >= 23 and Opera Hotlist
        var $this = $(this);
        $this.attr('href', bookmarkURL);
        $this.attr('title', bookmarkTitle);
        $this.attr('rel', 'sidebar');
        $this.off(e);
        triggerDefault = true;
    } else if (window.external && ('AddFavorite' in window.external)) {
        // IE Favorite
        window.external.AddFavorite(bookmarkURL, bookmarkTitle);
    } else {
        // WebKit - Safari/Chrome
        alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Cmd' : 'Ctrl') + '+D to bookmark this page.');
    }

    return triggerDefault;
  });
*/
});
