// changed the url because i was having 301 error
$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
