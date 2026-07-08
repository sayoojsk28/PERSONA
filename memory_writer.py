import json
import ollama

MODEL = "llama3.2:latest"


def write_memory(user_message, existing_memories):

    prompt = f"""
You are an AI memory writer.

Your job is to decide whether the user's latest message should become a long-term memory.

Existing memories:
{json.dumps(existing_memories, indent=2)}

Rules:

Only save information that will probably still be useful weeks or months later.

Rewrite memories as clear third-person facts.

Examples:

User:
"My pet cat is Lilly."

Memory:
"The user has a pet cat named Lilly."

Importance:
0.95

-------------------------

User:
"I want to call you Chattie."

Memory:
"The user calls me Chattie."

Importance:
0.80

-------------------------

User:
"I study BCA at Kannur University."

Memory:
"The user is studying BCA at Kannur University."

Importance:
0.92


Examples:

User:
"My name is Sayooj."

Memory:
"The user's name is Sayooj."

Importance:
0.98

-------------------------

User:
"Everyone calls me SK."

Memory:
"The user prefers to be called SK."

Importance:
0.96

-------------------------

User:
"I am 22 years old."

Memory:
"The user is 22 years old."

Importance:
0.90

-------------------------

User:
"I study BCA at Kannur University."

Memory:
"The user is studying BCA at Kannur University."

Importance:
0.92

-------------------------

User:
"I studied at GHSS Kannur."

Memory:
"The user studied at GHSS Kannur."

Importance:
0.85

-------------------------

User:
"I work as a software developer."

Memory:
"The user works as a software developer."

Importance:
0.94

-------------------------

User:
"My dream is to become a clinical psychologist."

Memory:
"The user's goal is to become a clinical psychologist."

Importance:
0.95

-------------------------

User:
"I love football."

Memory:
"The user loves football."

Importance:
0.85

-------------------------

User:
"My favourite movie is Interstellar."

Memory:
"The user's favourite movie is Interstellar."

Importance:
0.83

-------------------------

User:
"My pet cat is Lilly."

Memory:
"The user has a pet cat named Lilly."

Importance:
0.95

-------------------------

User:
"I have a younger sister."

Memory:
"The user has a younger sister."

Importance:
0.88

-------------------------

User:
"I'm married."

Memory:
"The user is married."

Importance:
0.95

-------------------------

User:
"My birthday is on August 15."

Memory:
"The user's birthday is on August 15."

Importance:
0.92

-------------------------

User:
"I am allergic to peanuts."

Memory:
"The user is allergic to peanuts."

Importance:
0.96

-------------------------

User:
"I prefer dark mode."

Memory:
"The user prefers dark mode."

Importance:
0.82

-------------------------

User:
"I don't like horror movies."

Memory:
"The user dislikes horror movies."

Importance:
0.82

-------------------------

User:
"I want to call you Chattie."

Memory:
"The user calls me Chattie."

Importance:
0.80

-------------------------

User:
"We met on Discord."

Memory:
"The user and I first met on Discord."

Importance:
0.70

-------------------------

User:
"I moved to Kochi in 2025."

Memory:
"The user moved to Kochi in 2025."

Importance:
0.90

-------------------------

User:
"I bought my first laptop today."

Memory:
"The user bought their first laptop."

Importance:
0.78


Return ONLY valid JSON.



If nothing should be saved:

{{
"save": false
}}

If memory should be saved:

{{
"save": true,
"memory": "...",
"importance": 0.85
}}

User message:

{user_message}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response["message"]["content"].strip()

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return {
            "save": False
        }

    try:
        return json.loads(text[start:end + 1])

    except Exception:

        return {
            "save": False
        }