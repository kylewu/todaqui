$(document).ready(function(){
  $(window).resize(function(){
    var top_in_digits = ($(window).height() - $("div.content").outerHeight())/4;
    top_in_digits = (top_in_digits > 0)?top_in_digits:0;
    $("div.content").css({
      position:"relative",
      top:top_in_digits,
      margin:"0 auto",
      float:"none",
      display:"inherit"
    });
  });
  $(window).resize();
  $("a.website").attr("target","_blank");
  $("a.website").hover(
    function(){
      $(this).addClass("hover");
    }, function(){
      $(this).removeClass("hover");
    }
  );
  $("a.website").click(function(){
    $(this).removeClass("hover");
  });
  var temp_building;
  var temp_category_name;
  $("div.block-name").click(function(){
    temp_building = $(this).parents("div.building");
    temp_category_name = $(this).find("a.block-name").text();
    $('#categoryConfirmModal').modal('show');
  });
  $('#categoryConfirmModal').on('show.bs.modal', function (event) {
    var modal = $(this);
    modal.find('#varText').text('打开' + temp_category_name + '下所有站点？');
  })
  $("#categoryConfirmButton").click(function(){
    temp_building.find("a.website").each(function(){
      var evt = document.createEvent("MouseEvents");
      evt.initMouseEvent("click", true, true, window, 0, 0, 0, 0, 0,
                          true, false, false, true, 0, null);
      $(this).get(0).dispatchEvent(evt);
    });
    $('#categoryConfirmModal').modal('hide');
  });
  $("a#chrome_extension").click(function(){
    $("#browserIndexModal").modal('hide');
    chrome.webstore.install("https://chrome.google.com/webstore/detail/aaaekojmfgkdoliidgddnefhnoibjbpi",successCallBack);
  });
  $(document).bind("keydown", function(event){
    //event.preventDefault();
    var k = event.which || event.keyCode;
    for(var i = 32; i < 91; i++){
      if (i == k){
        var obj = $("a.hotkey" + k);
        if(obj.attr("href") != undefined){
          obj.addClass("hover");
          setTimeout(function(){
            window.open(obj.attr("href"));
            obj.removeClass("hover");
          },500);
        }
      }
    }
    return false;
  });
});
var prefix = "index_tips_";
var div_id = prefix + getBrowserOS();
$("div#"+div_id).css("display","inherit");
function successCallBack(){
  window.location.reload();
}
function getBrowserOS(){
  var OsObject = "";
  if(navigator.userAgent.toLowerCase().indexOf("msie")!=-1) {
      return "ie";
  }
  if(navigator.userAgent.toLowerCase().indexOf("metasr")!=-1){
      return "sougou";
  }
  if(navigator.userAgent.toLowerCase().indexOf("lbbrowser")!=-1){
      return "liebao";
  }
  if(navigator.userAgent.toLowerCase().indexOf("firefox")!=-1){
      return "firefox";
  }
  if(navigator.userAgent.toLowerCase().indexOf("chrome")!=-1){
      return "chrome";
  }
  if(navigator.userAgent.toLowerCase().indexOf("safari")!=-1) {
      return "safari";
  }
  if(navigator.userAgent.toLowerCase().indexOf("opera")!=-1){
      return "opera";
  }
}
