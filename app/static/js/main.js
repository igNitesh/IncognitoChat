let name = prompt("Enter the nickname");
while (name === null || name.trim() === "") {
  name = prompt("Please enter a valid nickname");
}

const liElements = document.querySelectorAll("#myList li");
const selected_room = document.getElementById("selected-room");

liElements.forEach((li) => {
  li.addEventListener("click", () => {
    const groupname = li.innerText;
    selected_room.innerText = groupname;

    let ws = new WebSocket(
      "ws://" + window.location.host + "/ws/sc/" + groupname + "/"
    );

    ws.onopen = function () {
      console.log("Websocket connection open");
    };

    ws.onmessage = function (event) {
      data = JSON.parse(event.data);

      if (data.name == "Invalid name") {
        alert("Invalid name");
      }

      const messagesContainer = document.querySelector(".messages");
      const newMessage = document.createElement("div");
      newMessage.classList.add("message");

      const senderName = document.createElement("span");
      senderName.classList.add(data.name === name ? "receiver-name" : "sender-name");
      senderName.innerHTML = data.name === name ? "&#x1F47D; " + data.name : "&#128128;" + data.name;

      const messageContent = document.createElement("span");
      messageContent.textContent = data.msg;

      newMessage.appendChild(senderName);
      newMessage.appendChild(messageContent);

      messagesContainer.prepend(newMessage);
    };

    ws.onerror = function (event) {
      console.log(event);
      console.log("onerror from server....", event.data);
    };

    ws.onclose = function (event) {
      console.log("Websocket connection close..", event);
    };

    document.getElementById("send-btn").onclick = sendMessage;
    document.getElementById("chat-message-input").addEventListener("keypress", function (event) {
      if (event.key === "Enter") {
        sendMessage();
      }
    });

    function sendMessage() {
      const messageInputDom = document.getElementById("chat-message-input");
      const message = messageInputDom.value;

      if (message.trim() !== "") {
        ws.send(JSON.stringify({
          msg: message,
          name: name,
        }));

        messageInputDom.value = "";
      }
    }
  });
});
