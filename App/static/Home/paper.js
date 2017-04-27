$(document).on('click', '.folder', function() {
  $('.folder').toggleClass('opened');
  
  if($(".opened").length>0) {
  	
  	setTimeout(function() {
  		$(".showPaper").css("visibility","visible")
  		$(".showPaper").html($(".paper").html())
  	},500)
  } else {
  	$(".showPaper").css("visibility","hidden")
  	$(".showPaper").html("")
  }
});