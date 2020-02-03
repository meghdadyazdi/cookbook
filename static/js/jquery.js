$(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.modal').modal();
    $('.sidenav').sidenav();
  });
$('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));

//   $(document).ready(function(){
//     $('input.autocomplete').autocomplete({
//       data: {
//         "Apple": null,
//         "Microsoft": null,
//         "Google": 'https://placehold.it/250x250'
//       },
//     });
//   });