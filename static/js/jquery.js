$(document).ready(function () {
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.modal').modal();
    $('.sidenav').sidenav();
    $("#signinDrop").click(function () {
        if ($('#signinBox').is(':visible')) {
            $("#signinBox").css("display", "none");
        } else {
            $("#signinBox").css("display", "block");
        };
    });

    var fullDate = new Date()

    //convert month to 2 digits
    var twoDigitMonth = ((fullDate.getMonth().length + 1) === 1) ? (fullDate.getMonth() + 1) : '0' + (fullDate.getMonth() + 1);
    var currentDate = fullDate.getDate() + "/" + twoDigitMonth + "/" + fullDate.getFullYear();
    $("#recipe_date").val(fullDate)




    // ____________________________rating stars_______________________________

    // __________mouse enter___________    
    $(".star-1").mouseenter(function () {
        $(this).addClass("rate1");
    });

    $(".star-2").mouseenter(function () {
        $(this).addClass("rate2");
        $(".star-1").addClass("rate2");
    });

    $(".star-3").mouseenter(function () {
        $(this).addClass("rate3");
        $('.star-2').addClass("rate3");
        $('.star-1').addClass("rate3");
    });

    $(".star-4").mouseenter(function () {
        $(this).addClass("rate4");
        $('.star-3').addClass("rate4");
        $('.star-2').addClass("rate4");
        $('.star-1').addClass("rate4");
    });

    $(".star-5").mouseenter(function () {
        $(this).addClass("rate5");
        $('.star-4').addClass("rate5");
        $('.star-3').addClass("rate5");
        $('.star-2').addClass("rate5");
        $('.star-1').addClass("rate5");
    });

    // __________mouse leave___________

    $(".star-1").mouseleave(function () {
        $(this).removeClass("rate1");
    });

    $(".star-2").mouseleave(function () {
        $(this).removeClass("rate2");
        $(".star-1").removeClass("rate2");
    });

    $(".star-3").mouseleave(function () {
        $(this).removeClass("rate3");
        $('.star-2').removeClass("rate3");
        $('.star-1').removeClass("rate3");
    });

    $(".star-4").mouseleave(function () {
        $(this).removeClass("rate4");
        $('.star-3').removeClass("rate4");
        $('.star-2').removeClass("rate4");
        $('.star-1').removeClass("rate4");
    });

    $(".star-5").mouseleave(function () {
        $(this).removeClass("rate5");
        $('.star-4').removeClass("rate5");
        $('.star-3').removeClass("rate5");
        $('.star-2').removeClass("rate5");
        $('.star-1').removeClass("rate5");
    });


    // __________mouse click___________

    $(".star-1").click(function () {
        $(this).removeClass("rate11 rate22 rate33 rate44 rate55");
        $(".star-2").removeClass("rate22 rate33 rate44 rate55");
        $(".star-3").removeClass("rate33 rate44 rate55");
        $(".star-4").removeClass("rate44 rate55");
        $(".star-5").removeClass("rate55");
        $(this).addClass("rate11");
        $("#recipe_rate11").val("1")
        $("#recipe_rate22").val("")
        $("#recipe_rate33").val("")
        $("#recipe_rate44").val("")
        $("#recipe_rate55").val("")
    });

    $(".star-2").click(function () {
        $(".star-1").removeClass("rate33 rate44 rate55");
        $(this).removeClass("rate22 rate33 rate44 rate55");
        $(".star-3").removeClass("rate33 rate44 rate55");
        $(".star-4").removeClass("rate44 rate55");
        $(".star-5").removeClass("rate55");
        $(".star-1").addClass("rate22");
        $(this).addClass("rate22");
        $("#recipe_rate11").val("")
        $("#recipe_rate22").val("2")
        $("#recipe_rate33").val("")
        $("#recipe_rate44").val("")
        $("#recipe_rate55").val("")
    });

    $(".star-3").click(function () {
        $(".star-1").removeClass("rate44 rate55");
        $(".star-2").removeClass("rate44 rate55");
        $(this).removeClass("rate33 rate44 rate55");
        $(".star-4").removeClass("rate44 rate55");
        $(".star-5").removeClass("rate55");
        $(this).addClass("rate33");
        $(".star-1").addClass("rate33");
        $(".star-2").addClass("rate33");
        $("#recipe_rate11").val("")
        $("#recipe_rate22").val("")
        $("#recipe_rate33").val("3")
        $("#recipe_rate44").val("")
        $("#recipe_rate55").val("")
    });

    $(".star-4").click(function () {
        $(".star-1").removeClass("rate55");
        $(".star-2").removeClass("rate55");
        $(".star-3").removeClass("rate55");
        $(this).removeClass("rate44 rate55");
        $(".star-5").removeClass("rate55");
        $(this).addClass("rate44");
        $(".star-1").addClass("rate44");
        $(".star-2").addClass("rate44");
        $(".star-3").addClass("rate44");
        $("#recipe_rate11").val("")
        $("#recipe_rate22").val("")
        $("#recipe_rate33").val("")
        $("#recipe_rate44").val("4")
        $("#recipe_rate55").val("")
    });

    $(".star-5").click(function () {
        $(".star-1").addClass("rate55");
        $(".star-2").addClass("rate55");
        $(".star-3").addClass("rate55");
        $(".star-4").addClass("rate55");
        $(this).addClass("rate55");
        $("#recipe_rate11").val("")
        $("#recipe_rate22").val("")
        $("#recipe_rate33").val("")
        $("#recipe_rate44").val("")
        $("#recipe_rate55").val("5")
    });

    // Open link in same window (similar to target=_blank)
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
