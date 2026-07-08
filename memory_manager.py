from memory_writer import write_memory

from database import (
    get_all_memories,
    save_memory,
    search_memory
)


def process_memory(user_id, user_message):

    existing_memories = get_all_memories(user_id)

    result = write_memory(

        user_message,

        existing_memories

    )

    if not result.get("save"):

        return existing_memories, False

    memory = result["memory"].strip()

    importance = float(result["importance"])

    # Duplicate prevention

    already_exists = search_memory(

        user_id,

        memory

    )

    if already_exists:

        return existing_memories, False

    save_memory(

        user_id,

        memory,

        importance

    )

    updated_memories = get_all_memories(user_id)

    print("\n🧠 Memory Saved")
    print(memory)
    print("Importance:", importance)

    return updated_memories, True