// Change mode
$('#mode').click(function(){
  isDarkmode = isDarkmode ? false:true;
  $(this).css({background: isDarkmode?'#323549':'white',color:isDarkmode?'var(--text)':'#e67919'});
  $(this).html(`<i class="fa-solid ${isDarkmode?'fa-moon':'fa-sun'}"></i>`);
  if (window.innerWidth <= 768) $('body').css('background', isDarkmode?'var(--dark)':'var(--text)');
  $('.container').css('background', isDarkmode?'var(--dark)':'var(--text)');
  $('.messages').css('background', isDarkmode?'var(--dark)':'var(--text)');
  $('.input_container').css('background', isDarkmode?'var(--dark)':'var(--text)');
  $('.input_container').css('border-top', isDarkmode?'2px solid var(--semiDark)':'2px solid #949493');
  $('.other .main-message').css('border-color', isDarkmode?'var(--semiDark)':'#c5c5c4');
  $('.inner-spacer').css('border-color', isDarkmode?'var(--semiDark)':'#c5c5c4');
  $('.other .body p').css('color', isDarkmode?'var(--text)':'#1f1f1d');
  $('#input').css('color', isDarkmode?'var(--text)':'#1f1f1d');
  $('.spacer .text p').css('color', isDarkmode?'var(--text)':'#1f1f1d');
})