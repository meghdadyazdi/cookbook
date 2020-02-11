$(document).ready(function () {
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.modal').modal();
    $('.sidenav').sidenav();


    // INITIATE THE FOOTER
    siteFooter();
    // COULD BE SIMPLIFIED FOR THIS PEN BUT I WANT TO MAKE IT AS EASY TO PUT INTO YOUR SITE AS POSSIBLE
    $(window).resize(function () {
        siteFooter();
    });

    function siteFooter() {
        var siteContent = $('#site-content');
        var siteContentHeight = siteContent.height();
        var siteContentWidth = siteContent.width();

        var siteFooter = $('#site-footer');
        var siteFooterHeight = siteFooter.height();
        var siteFooterWidth = siteFooter.width();

        // console.log('Content Height = ' + siteContentHeight + 'px');
        // console.log('Content Width = ' + siteContentWidth + 'px');
        // console.log('Footer Height = ' + siteFooterHeight + 'px');
        // console.log('Footer Width = ' + siteFooterWidth + 'px');

        siteContent.css({
            "margin-bottom": siteFooterHeight + 50
        });
    };


    $("#signinDrop").click(function () {
        if ($('#signinBox').is(':visible')) {
            $("#signinBox").css("display", "none");
        } else {
            $("#signinBox").css("display", "block");
        };
        // $("#signinBox").css( "transform", "translateY(0)");
        // $("#signinBox").css( "z-index", "9999");
    });




    var fullDate = new Date()
    // console.log(fullDate);
    //Thu May 19 2011 17:25:38 GMT+1000 {}

    //convert month to 2 digits
    var twoDigitMonth = ((fullDate.getMonth().length + 1) === 1) ? (fullDate.getMonth() + 1) : '0' + (fullDate.getMonth() + 1);

    // console.log(fullDate.getMonth());

    var currentDate = fullDate.getDate() + "/" + twoDigitMonth + "/" + fullDate.getFullYear();
    // console.log(fullDate[1]);

    // $("#recipe_date").val(currentDate)
    $("#recipe_date").val(fullDate)







    $(".star-1").mouseenter(function () {
        $(this).addClass("rate1"); 
    });

    $(".star-2").mouseenter(function () {
        $(this).addClass("rate2"); 
        $(".star-1").addClass("rate2");
        // return false;
    });

    $(".star-3").mouseenter(function () {
        $(this).addClass("rate3");
        $('.star-2').addClass("rate3");
        $('.star-1').addClass("rate3");
        // return false;
    });

    $(".star-4").mouseenter(function () {
        $(this).addClass("rate4");
        $('.star-3').addClass("rate4");
        $('.star-2').addClass("rate4");
        $('.star-1').addClass("rate4");
        // return false;
    });

    $(".star-5").mouseenter(function () {
        $(this).addClass("rate5");
        $('.star-4').addClass("rate5");
        $('.star-3').addClass("rate5");
        $('.star-2').addClass("rate5");
        $('.star-1').addClass("rate5");
        // return false;
    });

// __________mouse leave___________

    $(".star-1").mouseleave(function () {
        $(this).removeClass("rate1"); 
    });

    $(".star-2").mouseleave(function () {
        $(this).removeClass("rate2"); 
        $(".star-1").removeClass("rate2");
        // return false;
    });

    $(".star-3").mouseleave(function () {
        $(this).removeClass("rate3");
        $('.star-2').removeClass("rate3");
        $('.star-1').removeClass("rate3");
        // return false;
    });

    $(".star-4").mouseleave(function () {
        $(this).removeClass("rate4");
        $('.star-3').removeClass("rate4");
        $('.star-2').removeClass("rate4");
        $('.star-1').removeClass("rate4");
        // return false;
    });

    $(".star-5").mouseleave(function () {
        $(this).removeClass("rate5");
        $('.star-4').removeClass("rate5");
        $('.star-3').removeClass("rate5");
        $('.star-2').removeClass("rate5");
        $('.star-1').removeClass("rate5");
        // return false;
    });


    // __________mouse click___________

    $(".star-1").click(function () {
        $(this).addClass("rate11");
        $("#recipe_rate11").val(1)



        // var str = $("#recipe_rate11").val(1);
        // console.log(str);
        // var rate1 = parseInt("str");
        // console.log(rate1);
        // rate1 += 1;
        // console.log(rate1);
        // rate1.toString();
        // console.log(rate1);
        // $("#recipe_rate1").val(rate1)
    });















    // Or use this to Open link in same window (similar to target=_blank)
    $(".boxxx").click(function () {
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
