const sendMessage = displayMessage;

io.emit('join', {
  data: `Welcome! This sitebot was created by Greegmon. You can interact with it using various commands. Type '/help' to view a list of available commands.`,
  id: 'MSG-Welcome',
  room: Room
})

io.on('sendMessage', (msg) => {
  sendMessage({
    data: msg.data,
    id: msg.id
  })
})
io.on('unsendMessage', (data) => {
  removeMessage(data.id)
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
    sendMessage({
      data: value,
      id: messageID(20)
    }, true)
    input.val('');
    io.emit('recieveMessage', {
      text: value,
      room: Room
    });
  }
}