  /*global $*/
  /*global jQuery*/
  $(function() {
    $(".card").show(); 
    $( ".month-search" ).click(function(){
      $( ".card" ).hide();
    });
    $( ".month-search1" ).click(function(){
      $( ".mon1" ).show(); 
    });
    $( ".month-search2" ).click(function(){
      $( ".mon2" ).show(); 
    });
    $( ".month-search3" ).click(function(){
      $( ".mon3" ).show(); 
    });
    $( ".month-search4" ).click(function(){
      $( ".mon4" ).show(); 
    });
    $( ".month-search5" ).click(function(){
      $( ".mon5" ).show(); 
    });
    $( ".month-search6" ).click(function(){
      $( ".mon6" ).show(); 
    });
    $( ".month-search7" ).click(function(){
      $( ".mon7" ).show(); 
    });
    $( ".month-search8" ).click(function(){
      $( ".mon8" ).show(); 
    });
    $( ".month-search9" ).click(function(){
      $( ".mon9" ).show();  
    });
    $( ".month-search10" ).click(function(){
      $( ".mon10" ).show(); 
    });
    $( ".month-search11" ).click(function(){
      $( ".mon11" ).show(); 
    });
    $( ".month-search12" ).click(function(){
      $( ".mon12" ).show(); 
    });
    $(".show-all").click(function(){
      $(".card").show(); 
    });
    $(".show-mine").click(function(){
      $(".card").hide();
      $(".mine").show();
    });
    $(".showbutton").click(function(){
      $(".highlighted").removeClass("highlighted");
      $(this).addClass('highlighted');
    });
  });
  
  $(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});