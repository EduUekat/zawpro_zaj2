import sys
import time
from queue_manager import claim_next_pending_task, update_task_status


def consume_loop(consumer_id: str):
    print(f"[Consumer {consumer_id}] Uruchomiony. Nasłuchiwanie na zadania (co 5s)...")
    while True:
        task = claim_next_pending_task(consumer_id)
        if task:
            task_id = task["id"]
            print(
                f"[Consumer {consumer_id}] Pobrano zadanie {task_id}. Status:"
                " in_progress. Wykonywanie (30s)..."
            )

            time.sleep(30)

            update_task_status(task_id, "done")
            print(
                f"[Consumer {consumer_id}] Zakończono zadanie {task_id}. Status: done."
            )
        else:
            time.sleep(5)


if __name__ == "__main__":
    c_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    try:
        consume_loop(c_id)
    except KeyboardInterrupt:
        print(f"\n[Consumer {c_id}] Zatrzymany przez użytkownika.")
