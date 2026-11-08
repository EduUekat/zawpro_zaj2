import sys
import uuid
from datetime import datetime
from queue_manager import add_task


def produce_task():
    """Generuje 1 rekord pracy ze statusem 'pending'."""
    task_id = str(uuid.uuid4())[:8]
    task = {
        "id": task_id,
        "type": "phone_call",
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "consumer_id": "",
    }
    add_task(task)
    print(f"[Producer] Dodano zadanie do pliku txt: ID {task_id}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--batch":
        print("[Producer] Generowanie 100 zadań do pliku txt...")
        for _ in range(100):
            produce_task()
        print("[Producer] Pomyślnie dodano 100 zadań!")
    else:
        produce_task()
