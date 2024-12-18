const sendMessage = displayMessage;

io.emit('join', Room)

io.on('sendMessage', (msg) => {
  sendMessage({
    data: msg.data,
    id: msg.id
  })
})

io.on('unsendMessage', (data) => {
  $(`#${data.id}`).remove()
})


// random message id
function messageID(count){
  const char = "abcdefghijklmnopqrstuvwxyz1237654098QWERTYUIOPASDFGHJKLZXCVBNM";
  let id = 'MSG-'
  for (let i=0;i<count*2;i++){
    const index = Math.floor(Math.random() * char.length)
    id += char[index-1]
  }
  return id
}

function execute(){
  const input = $('#input');
  const value = input.val().trim()
  if (value){
    const $ID = messageID(20)
    sendMessage({
      data: value,
      id: $ID
    }, true)
    input.val('');
    io.emit('recieveMessage', {
      text: value,
      id: $ID,
      room: Room
    });
  }
}

// change themee color