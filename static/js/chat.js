async function loadConversations() {

    let res = await fetch("/conversations");
    let data = await res.json();

    let list = document.getElementById("conversation-list");
    list.innerHTML = "";

    data.forEach(chat => {

        let div = document.createElement("div");
        div.className = "chat-item";
        div.innerText = chat.title || "New Chat";

        div.onclick = async function () {

            let res = await fetch("/load_chat/" + chat.id);
            let messages = await res.json();

            let box = document.getElementById("chat-box");
            box.innerHTML = "";

            messages.forEach(m => {

                if (m.sender === "ai") {

                    box.innerHTML += `
                        <div class="msg ai">
                            ${m.message}
                            <button class="speak-btn"
                                onclick='speakText(${JSON.stringify(m.message)})'>
                                🔊
                            </button>
                        </div>
                    `;

                } else {

                    box.innerHTML += `
                        <div class="msg user">
                            ${m.message}
                        </div>
                    `;

                }

            });

            box.scrollTop = box.scrollHeight;
        };

        list.appendChild(div);
    });
}


async function sendMessage() {

    let input = document.getElementById("message");
    let message = input.value;

    if (!message.trim()) return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="msg user">${message}</div>`;
    input.value = "";

    showTyping();

    let res = await fetch("/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    let data = await res.json();

    removeTyping();

    const msgDiv = document.createElement("div");
    msgDiv.className = "msg ai";

    const text = document.createElement("span");
    text.innerText = data.reply;

    const btn = document.createElement("button");
    btn.className = "speak-btn";
    btn.innerHTML = "🔊";

    btn.onclick = function () {
    speakText(data.reply);
    };

    msgDiv.appendChild(text);
    msgDiv.appendChild(btn);

    chatBox.appendChild(msgDiv);
    await loadConversations();

    if (data.memory_saved) {
        chatBox.innerHTML += `
            <div class="memory-note">
                🧠 I'll remember that.
            </div>
        `;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}


function showTyping() {

    let chatBox = document.getElementById("chat-box");

    if (document.getElementById("typing")) return;

    let typingDiv = document.createElement("div");
    typingDiv.className = "msg ai";
    typingDiv.id = "typing";
    typingDiv.innerHTML = "AI is typing...";

    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function removeTyping() {

    let t = document.getElementById("typing");
    if (t) t.remove();
}


async function newChat() {

    let res = await fetch("/new_chat", {
        method: "POST"
    });

    await res.json();

    document.getElementById("chat-box").innerHTML = "";

    loadConversations();
}


async function loadWelcome() {

    let res = await fetch("/welcome");
    let data = await res.json();

    if (!data.show)
        return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML = `
        <div class="msg ai">
            ${data.message.replace(/\n/g,"<br>")}
        </div>
    `;

}

async function loadCurrentChat(){

    let res = await fetch("/current_chat");
    let messages = await res.json();

    let box = document.getElementById("chat-box");

    box.innerHTML = "";

    messages.forEach(m => {

    const msgDiv = document.createElement("div");
    msgDiv.className = "msg " + m.sender;

    const text = document.createElement("span");
    text.innerText = m.message;

    msgDiv.appendChild(text);

    if (m.sender === "ai") {

        const btn = document.createElement("button");
        btn.className = "speak-btn";
        btn.innerHTML = "🔊";

        btn.onclick = function () {
            speakText(m.message);
        };

        msgDiv.appendChild(btn);

    }

    box.appendChild(msgDiv);

});

    if(messages.length===0){
        loadWelcome();
    }

}

window.onload = function(){

    loadConversations();

    loadCurrentChat();

    document.getElementById("new-chat-btn").onclick = newChat;

};

function speakText(text) {

    

    speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);

    speechSynthesis.speak(utterance);
}

