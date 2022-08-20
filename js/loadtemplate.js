$(function () {
    var includes = $('[data-include]')
    $.each(includes, function () {
      var file = '../templates/' + $(this).data('include') + '.html'
      $(this).load(file)
    })
  })


function load(addr, newPage){
  if(newPage){
    window.open('https://' + linaddrk, '_blank').focus();
  }else{
    window.location=addr
  }
}