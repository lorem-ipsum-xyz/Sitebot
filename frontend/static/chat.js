function scroll(){
  const i = document.querySelector('.message_container')
  i.scrollTop = i.scrollHeight;
}

function checkSrc(fuji){
  if (fuji.startsWith('https://')) return fuji;
  return "{{ url_for('static', filename=" + `'${fuji}'` + ") }}"
}

function showImage(img){
  Swal.fire({
    imageUrl: img.src,
    imageAlt: img.alt,
    imageWidth: 300,
    showConfirmButton: false
  })
}

function displayMessage(datos, isUser=false){
  const data = datos.data
  const box = document.createElement('div');
  box.classList.add('message_box');
  box.id = datos.id
  const message = document.createElement('div');
  message.classList.add('message')
  message.classList.add(isUser ? 'me':'bot')
  const $body = document.createElement('div');
  $body.classList.add('body');
  //$body.style.whiteSpace = 'pre';
  const $attachment = document.createElement('div');
  $attachment.classList.add('attachment')
  $attachment.style.display = 'none'
  
  // skeleton loading for image
  const skeleton = document.createElement('div');skeleton.classList.add('skeleton');
  const loading = document.createElement('div');loading.classList.add('skeleton-image');
  skeleton.style.width = '250px'
  skeleton.appendChild(loading);
  
  let hasBody = false;
  let hasAttachment = false;
  
  function text(txt){
    const $texts = txt.split('\n');
    for (const $text of $texts){
      const p = document.createElement('p');
      p.textContent = $text;
      if ($text === ''){
        $body.appendChild(document.createElement('br'))
      }
      $body.appendChild(p);
    }
  }
  function createImage(attachment){
    const img = document.createElement('img');
    img.src = attachment.src.startsWith('https://') || attachment.src.startsWith('http://')
      ? attachment.src
      : `${basePath}${attachment.src}`;
    img.alt = attachment.title;
    attachment.height ? img.height = attachment.height:null
    console.log(img.height)
    img.setAttribute('onclick', 'showImage(this)')
    return img
  }
  function createVideo(attachment){
    const video = document.createElement('video');
    video.setAttribute('controls','');
    video.style.width = '100%';
    const source = document.createElement('source');
    source.src = attachment.src.startsWith('https://') || attachment.src.startsWith('http://')
      ? attachment.src
      : `${basePath}${attachment.src}`;
    video.appendChild(source);
    return video
  }
  
  if (typeof data === 'string'){
    text(data);
    hasBody = true
  }else{
    const { body, attachment } = data;
    hasBody = body?true:hasBody;
    hasAttachment = attachment?true:hasAttachment;
    if (!attachment && !body) return;
    body ? text(body):null// <--
    // Send Attachment method.
    if (hasAttachment){if (attachment.length >= 1){
      for (const attach of attachment){
        if (attach.type === 'image'){
          const image = createImage(attach);
          const ind = attachment.indexOf(attach) + 1;
          if ((ind%2) == 0) image.style.marginLeft = '2%';
          if (attachment.length > 1) image.style.width = '49%';
          image.onload = function(){
            skeleton.style.display = 'none';
            $attachment.style.display = 'block';
          }
          $attachment.appendChild(image)
        }
        if (attach.type === 'video'){
          const video = createVideo(attach);
          video.onloadedmetadata = function(){
            skeleton.style.display = 'none';
            $attachment.style.display = 'block'
          }
          $attachment.appendChild(video)
        }
      }
    }}
  }
  if (hasBody) message.appendChild($body);
  if (hasAttachment) {
    message.appendChild(skeleton);
    message.appendChild($attachment);
  }
  box.appendChild(message);
  const container = document.querySelector('.message_container');
  if (!container.firstChild){
    container.appendChild(box);
  }else{
    container.insertBefore(box, container.firstChild)
  }
  scroll()
}

function removeMessage(id){
  $(`#${id}`).remove()
}