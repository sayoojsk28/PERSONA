from flask import Flask, render_template, request, jsonify, session
from personality import analyze_answers
from gemini_chat import generate_reply, generate_welcome,generate_chat_title
from memory_manager import process_memory

import os
from dotenv import load_dotenv
from database import (
    initialize_database,
    get_all_memories,
    save_memory,
    update_memory,
    delete_memory,
    init_chat_tables,
    create_conversation,
    get_conversations,
    save_message,
    get_messages,
    update_conversation_title
)

load_dotenv()



app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

initialize_database()
init_chat_tables()

CURRENT_USER = "demo_user"




@app.route("/")
def home():
    return render_template("home.html")


@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")



@app.route("/friend")
def friend():

    if "profile" not in session:
        return "Please complete the questionnaire first."

    return render_template("friend.html")


@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/welcome")
def welcome():

    conversation_id = session.get("conversation_id")

    if conversation_id:

        messages = get_messages(conversation_id)

        if messages:
            return jsonify({
                "show": False
            })

    memories = get_all_memories(CURRENT_USER)

    if memories:

        return jsonify({
            "show": False
        })

    return jsonify({

        "show": True,

        "message": session.get(
            "welcome",
            "Hi! I'm Persona."
        )

    })


@app.route("/send", methods=["POST"])
def send():

    data = request.json
    user_message = data.get("message", "")

    profile = session.get("profile")

    if not profile:
        return jsonify({
            "reply": "Profile not found."
        })

    conversation_id = session.get("conversation_id")

    if not conversation_id:

        conversation_id = create_conversation(
            CURRENT_USER,
            "New Chat"
        )

        session["conversation_id"] = conversation_id

    save_message(
        conversation_id,
        "user",
        user_message
    )

    messages = get_messages(conversation_id)

    if len(messages) == 1:

        title = generate_chat_title(user_message)

        update_conversation_title(
            conversation_id,
            title
        )

    memories, saved = process_memory(
        CURRENT_USER,
        user_message
    )

    reply = generate_reply(
        profile,
        memories,
        user_message
    )

    save_message(
        conversation_id,
        "ai",
        reply
    )

    return jsonify({

        "reply": reply,

        "memory_saved": saved

    })


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    answers = data["answers"]

    profile = analyze_answers(answers)

    session["profile"] = profile

    welcome_message = generate_welcome(profile)

    session["welcome"] = welcome_message

    return jsonify({

        "status": "success"

    })

@app.route("/persona")
def persona():
    return render_template("persona.html")

@app.route("/memories")
def memories():

    memories = get_all_memories(CURRENT_USER)

    return render_template(

        "memories.html",

        memories=memories

    )

@app.route("/edit_memory", methods=["POST"])
def edit_memory():

    data = request.json

    memory_id = data["id"]
    memory_text = data["memory"]

    update_memory(

        memory_id,
        memory_text

    )

    return jsonify({

        "status": "success"

    })
@app.route("/delete_memory", methods=["POST"])
def remove_memory():

    data = request.json

    memory_id = data["id"]

    delete_memory(

        memory_id

    )

    return jsonify({

        "status": "success"

    })

@app.route("/new_chat", methods=["POST"])
def new_chat():

    user_id = CURRENT_USER

    conv_id = create_conversation(user_id, "New Chat")

    session["conversation_id"] = conv_id

    return jsonify({
        "conversation_id": conv_id
    })

@app.route("/current_chat")
def current_chat():

    conversation_id = session.get("conversation_id")

    if not conversation_id:

        return jsonify([])

    messages = get_messages(conversation_id)

    return jsonify([
        {
            "sender": m[0],
            "message": m[1]
        }
        for m in messages
    ])

@app.route("/conversations")
def conversations():

    user_id = CURRENT_USER

    chats = get_conversations(user_id)

    return jsonify([
        {
            "id": c[0],
            "title": c[1]
        }
        for c in chats
        if c[1] != "New Chat"
    ])

@app.route("/load_chat/<int:chat_id>")
def load_chat(chat_id):

    session["conversation_id"] = chat_id

    messages = get_messages(chat_id)

    return jsonify([
        {
            "sender": m[0],
            "message": m[1]
        }
        for m in messages
    ])

@app.route("/clear")
def clear():

    session.clear()

    return "Session Cleared"

if __name__ == "__main__":
    app.run(debug=True)


