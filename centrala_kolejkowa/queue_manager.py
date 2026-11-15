import sqlite3
import os

DB_FILE = "queue.db"


def init_db():
    """Inicjalizuje bazę danych SQLite oraz tabelę tasks, jeśli nie istnieją."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            type TEXT,
            status TEXT,
            created_at TEXT,
            consumer_id TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_task(task_data):
    """Dodaje nowe zadanie ze statusem 'pending' do bazy SQLite."""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO tasks (id, type, status, created_at, consumer_id)
        VALUES (?, ?, ?, ?, ?)
    """,
        (
            task_data["id"],
            task_data["type"],
            task_data["status"],
            task_data["created_at"],
            task_data.get("consumer_id"),
        ),
    )
    conn.commit()
    conn.close()


def claim_next_pending_task(consumer_id: str):
    """Wyszukuje pierwsze zadanie ze statusem 'pending', zmienia jego status na

    'in_progress' i przypisuje konsumenta w ramach bezpiecznej transakcji.
    """
    init_db()
    conn = sqlite3.connect(DB_FILE)
    conn.isolation_level = "IMMEDIATE"
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id FROM tasks WHERE status = 'pending' LIMIT 1")
        row = cursor.fetchone()

        if row:
            task_id = row[0]
            cursor.execute(
                """
                UPDATE tasks
                SET status = 'in_progress', consumer_id = ?
                WHERE id = ?
            """,
                (consumer_id, task_id),
            )

            cursor.execute(
                """
                SELECT id, type, status, created_at, consumer_id
                FROM tasks WHERE id = ?
            """,
                (task_id,),
            )
            updated_row = cursor.fetchone()
            conn.commit()

            return {
                "id": updated_row[0],
                "type": updated_row[1],
                "status": updated_row[2],
                "created_at": updated_row[3],
                "consumer_id": updated_row[4],
            }
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

    return None


def update_task_status(task_id: str, new_status: str):
    """Aktualizuje status zadania w bazie SQLite (np. na 'done')."""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """,
        (new_status, task_id),
    )
    conn.commit()
    conn.close()
