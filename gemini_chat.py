import ollama

MODEL = "llama3.2:latest"


def build_memory_text(memories):

    if not memories:
        return "No memories."

    lines = []

    for memory in memories[:15]:

        lines.append(

            "- " + memory["memory_text"]

        )

    return "\n".join(lines)


def generate_reply(profile, memories, user_message):

    memory_text = build_memory_text(memories)

    prompt = f"""
You are Persona, a warm, intelligent and emotionally supportive AI friend.

Personality:

Support Style: {profile['support_style']}
Honesty Style: {profile['honesty_style']}
Humor Style: {profile['humor_style']}
Energy Style: {profile['energy_style']}
Talk Style: {profile['talk_style']}
Role: {profile['role']}

Long-term Memories:

{memory_text}

Rules:

- Use the memories naturally.
- Never dump memories unless relevant.
- If a preferred way of addressing the user exists, always use it.
- Behave like a real long-term friend.
- Never mention the memory database.
- Reply naturally.
- Use the memories naturally.
- Never dump memories unless relevant.
- If a preferred way of addressing the user exists, always use it.
- Behave like a real long-term friend.
- Never mention the memory database.
- Keep replies concise.
- Usually reply in 1–4 short sentences.
- Only give long detailed explanations if the user specifically asks for them.
- Talk naturally like a real friend, not like an article or essay.
- Avoid unnecessary introductions and conclusions.

User:

{user_message}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()


def generate_welcome(profile):

    prompt = f"""
You are Persona, an AI friend.

Generate ONLY the first message of a brand new conversation.

Personality:

Support Style: {profile['support_style']}
Honesty Style: {profile['honesty_style']}
Humor Style: {profile['humor_style']}
Energy Style: {profile['energy_style']}
Talk Style: {profile['talk_style']}
Role: {profile['role']}

Requirements:

- Introduce yourself as Persona.
- Sound warm, natural and human.
- Ask the user to introduce themselves.
- Mention you'll remember important things.
- Keep under 90 words.
- No markdown.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()


def generate_chat_title(user_message):

    prompt = f"""
Convert this user message into a short chat title.

Rules:
- Max 4 to 6 words
- No punctuation
- Meaningful title only

User message:
{user_message}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()