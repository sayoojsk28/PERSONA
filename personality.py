def analyze_answers(answers):

    support_map = [
        "Listener",
        "Problem Solver",
        "Motivator",
        "Mood Booster",
        "Calming Presence"
    ]

    honesty_map = [
        "Always Honest",
        "Gentle Honest",
        "Challenge Me",
        "Mostly Agreeable"
    ]

    humor_map = [
        "Wholesome",
        "Sarcastic",
        "Dry",
        "Low Humor"
    ]

    energy_map = [
        "Calm",
        "Balanced",
        "Energetic"
    ]

    talk_map = [
        "Deep Conversations",
        "Casual Chats",
        "Mixed Style"
    ]

    role_map = [
    "Best Friend",
    "Mentor",
    "Study Buddy",
    "Emotional Support",
    "Motivator"
    ]

    profile = {

        "support_style": support_map[answers[0]],
        "honesty_style": honesty_map[answers[1]],
        "humor_style": humor_map[answers[2] % len(humor_map)],
        "energy_style": energy_map[answers[3] % len(energy_map)],
        "talk_style": talk_map[answers[4] % len(talk_map)],
         "role": role_map[answers[5] % len(role_map)]
    }

    return profile