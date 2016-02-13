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