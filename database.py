import sqlite3

DATABASE = "memory.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =====================================================
# MEMORY TABLE
# =====================================================

def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT NOT NULL,

            memory_text TEXT NOT NULL,

            importance REAL NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            last_used TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            times_used INTEGER DEFAULT 0,

            UNIQUE(user_id, memory_text)

        )

    """)

    conn.commit()
    conn.close()


# =====================================================
# SAVE MEMORY
# =====================================================

def save_memory(user_id, memory_text, importance):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO memories(

            user_id,
            memory_text,
            importance

        )

        VALUES(?,?,?)

        ON CONFLICT(user_id,memory_text)

        DO UPDATE SET

            importance=excluded.importance

    """, (

        user_id,
        memory_text,
        importance

    ))

    conn.commit()
    conn.close()


# =====================================================
# LOAD MEMORIES
# =====================================================

def get_all_memories(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM memories

        WHERE user_id=?

        ORDER BY importance DESC,
                 created_at DESC

    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# =====================================================
# SEARCH MEMORY
# =====================================================

def search_memory(user_id, memory_text):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM memories

        WHERE

        user_id=?

        AND lower(memory_text)=lower(?)

    """, (

        user_id,
        memory_text

    ))

    row = cursor.fetchone()

    conn.close()

    return row


# =====================================================
# UPDATE MEMORY USAGE
# =====================================================

def mark_memory_used(memory_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE memories

        SET

            times_used = times_used + 1,

            last_used = CURRENT_TIMESTAMP

        WHERE id=?

    """, (memory_id,))

    conn.commit()
    conn.close()


# =====================================================
# DELETE MEMORY
# =====================================================

def delete_memory(memory_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM memories

        WHERE id=?

    """, (memory_id,))

    conn.commit()
    conn.close()


# =====================================================
# CHAT TABLES
# =====================================================

def init_chat_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS conversations(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS messages(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER,
            sender TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()
    conn.close()


# =====================================================
# CREATE CHAT
# =====================================================

def create_conversation(user_id, title="New Chat"):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO conversations(

            user_id,
            title

        )

        VALUES(?,?)

    """, (

        user_id,
        title

    ))

    conn.commit()

    conv_id = cursor.lastrowid

    conn.close()

    return conv_id


# =====================================================
# CHAT LIST
# =====================================================

def get_conversations(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            id,
            title

        FROM conversations

        WHERE user_id=?

        ORDER BY created_at DESC

    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


# =====================================================
# SAVE MESSAGE
# =====================================================

def save_message(conversation_id, sender, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO messages(

            conversation_id,
            sender,
            message

        )

        VALUES(?,?,?)

    """, (

        conversation_id,
        sender,
        message

    ))

    conn.commit()
    conn.close()


# =====================================================
# LOAD CHAT
# =====================================================

def get_messages(conversation_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            sender,
            message

        FROM messages

        WHERE conversation_id=?

        ORDER BY id ASC

    """, (conversation_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


# =====================================================
# UPDATE TITLE
# =====================================================

def update_conversation_title(conversation_id, title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE conversations

        SET title=?

        WHERE id=?

    """, (

        title,
        conversation_id

    ))

    conn.commit()
    conn.close()

def update_memory(memory_id, memory_text):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE memories

        SET memory_text = ?

        WHERE id = ?

    """, (

        memory_text,
        memory_id

    ))

    conn.commit()
    conn.close()