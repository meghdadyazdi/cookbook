$(document).ready(function() {
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.modal').modal();
    $('.sidenav').sidenav();
  
	
	// INITIATE THE FOOTER
  siteFooter();
	// COULD BE SIMPLIFIED FOR THIS PEN BUT I WANT TO MAKE IT AS EASY TO PUT INTO YOUR SITE AS POSSIBLE
	$(window).resize(function() {
		siteFooter();
	});
	
	function siteFooter() {
		var siteContent = $('#site-content');
		var siteContentHeight = siteContent.height();
		var siteContentWidth = siteContent.width();

		var siteFooter = $('#site-footer');
		var siteFooterHeight = siteFooter.height();
		var siteFooterWidth = siteFooter.width();

		console.log('Content Height = ' + siteContentHeight + 'px');
		console.log('Content Width = ' + siteContentWidth + 'px');
		console.log('Footer Height = ' + siteFooterHeight + 'px');
		console.log('Footer Width = ' + siteFooterWidth + 'px');

		siteContent.css({
			"margin-bottom" : siteFooterHeight + 50
		});
    };
    

    

    // Or use this to Open link in same window (similar to target=_blank)
    $(".boxxx").click(function(){
        window.location = $(this).find("a:first").attr("href");
        return false;
    });

    // Show URL on Mouse Hover
    $(".boxxx").hover(function () {
        window.status = $(this).find("a:first").attr("href");
    }, function () {
        window.status = "";
    });
});
