// Auto scroll to the bottom message
function scroll(){
  window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
  })
  const msg = document.getElementById('msg-cont');
  msg.scrollTop = msg.scrollHeight;
  //document.querySelector('.message_box:nth-last-child(1)').style.marginBottom = '2em'
}

// check if link or path
function attachCheck(src){
  if (src.includes('https://')){
    return src
  }else{
    return basePath + src
  }
}

// Create an attachemnt imagee
function createImage(attachment){
  const image = $('<img />', {
    src: attachCheck(attachment.src),
    alt: attachment?.title ?? 'No title!',
    height: attachment?.height ?? null
  })
  return image
}

// Creste video
function createVideo(video){
  return $("<video>")
    .attr('height', video?.height ?? null)
    .attr('controls', '')
    .append($("<source />").attr('src', attachCheck(video.src)))
}

// Format the text
function text(text, $body){
  const span = (t) => `${t==='>'?'&gt':'&lt'}`;
  text = text.replace(/</g, span('<')).replace(/>/g, span('>'));
  text = text.replace(/\n/g, '<br>')
  
  const linkRegex = /!\[([^\]]+)\]\(([^\)]+)\)/g
  let links = text.match(linkRegex);
  if (links){
    for (const link of links){
      let [_XA, _XB] = link.split('](');
      let $text = _XA.slice(2);
      let $link = _XB.slice(0,_XB.length-1)
      text = text.replace(link, `<a target="_blank" href="${$link}">${$text}</a>`)
    }
  }
  $body.append($('<p>').html(text));
}

function displayMessage({ id, data }, isUser=false){
  if (!data) return;
  const $messageBox = $('<div>')
    .addClass(`message_box ${isUser?'me':'other'}`)
    .attr('id', id);
  const $message = $('<div>')
    .addClass('message')
  const $label = $('<div>')
    .addClass('label').text(isUser ? 'You':'BOT');
  const $mainMessage = $('<div>')
    .addClass('main-message');
  
  const $body = $('<div>').addClass('body');
  const $attachment = $('<div>').addClass('attachment').hide();
  const $skeleton = $('<div>').addClass('skeleton').append($('<div>').addClass('skeleton-image'));
  
  let hasBody = false;
  let hasAttach = false;
  
  if ($('.message_box:nth-last-child(1)').hasClass(isUser?'me':'other')){
    $('.message_box:nth-last-child(1)').css('margin-bottom', '3px')
    $($label).hide()
  }
  
  if (typeof data === 'string'){text(data, $body);hasBody=true}
  else {
    const { body, attachment } = data;
    
    body ? hasBody=true:hasBody;
    if (attachment) attachment.length >= 1 ? hasAttach=true:hasAttach;
    
    // send Text
    hasBody ? text(body, $body):null
    
    // Send Attachment
    if (attachment){
      for (const attach of attachment){
        if (attach?.type === 'image'){
          const img = createImage(attach);
          img.attr('width', '49%')
          if ((attachment.indexOf(attach)%2)!==0) img.css('margin-left', '2%')
          if (attachment.length === 1) img.css('width','100%');
          img.on('load', () => {
            $skeleton.hide();
            $attachment.show()
          })
          $attachment.append(img)
        }else if(attach?.type === 'video'){
          const video = createVideo(attach);
          video.css('width', '100%')
          video.css('border-radius', '11px')
          video[0].onloadedmetadata = function(){
            $skeleton.hide();
            $attachment.show()
          }
          $attachment.append(video)
        }else{
          $skeleton.hide()
          $attachment.show()
          $attachment.append(
            $('<div>').addClass('invalidType').append(
              $('<div>')
              .addClass('text')
              .text('Invalid attachment type')
            )
          )
        }
      }
    }
  }
  
  if (hasBody) $mainMessage.append($body);
  if (hasAttach) $mainMessage.append($skeleton).append($attachment);
  $message.append($label).append($mainMessage);
  $messageBox.append($message);
  
  $('.messages').append($messageBox)
  
  $('.other .main-message').css('border-color', isDarkmode?'var(--semiDark)':'#c5c5c4');
  $('.other .body p').css('color', isDarkmode?'var(--text)':'#1f1f1d')

  scroll()
}

$(document).ready(function(){
  scroll();
  
  // View Image
  $('.attachment img').click(function(){
    const me = $(this)[0]
    Swal.fire({
      text: me.alt,
      imageUrl: me.src,
      imageAlt: me.alt,
      showConfirmButton: false
    })
  })
})


/* [ NEXT UPDATE ]
//$('#cancel-btn').click(() => $('.messageMenu').hide())

// when a user hold a message
let hold_sec = 0;
let isHolding = false;
messages.forEach(message => {
  // Mobile
  message.addEventListener('touchend', () => isHolding = false)
  message.addEventListener('touchcancel', () => isHolding = false)
  message.addEventListener('touchstart',()=>{
    isHolding = true;
    const checking = setInterval(() => {
      if (isHolding){
        if (hold_sec === 3){
          showOtherClicks(message)
          hold_sec = 0;
          clearInterval(checking)
        }else{
          hold_sec++
        }
      }else{
        hold_sec = 0;
        clearInterval(checking)
      }
    },100)
  })
})
function showOtherClicks(data){
  $('.messageMenu').hide()
  setTimeout(()=>$('.messageMenu').show(),100)
}
*/