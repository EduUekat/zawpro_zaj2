import csv
import os

QUEUE_FILE = "queue.txt"
FIELDNAMES = ["id", "type", "status", "created_at", "consumer_id"]


def init_queue():
    """Inicjalizuje plik tekstowy kolejki wraz z nagłówkiem, jeśli nie istnieje."""
    if not os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_task(task_data):
    """Dodaje nowe zadanie ze statusem 'pending' do pliku txt."""
    init_queue()
    with open(QUEUE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(task_data)


def claim_next_pending_task(consumer_id: str):
    """Wyszukuje pierwsze zadanie ze statusem 'pending', zmienia status na

    'in_progress' i przypisuje konsumenta (operacja atomowa).
    """
    init_queue()
    rows = []
    claimed_task = None

    with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["status"] == "pending" and not claimed_task:
                row["status"] = "in_progress"
                row["consumer_id"] = consumer_id
                claimed_task = dict(row)
            rows.append(row)

    if claimed_task:
        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        return claimed_task

    return None


def update_task_status(task_id: str, new_status: str):
    """Aktualizuje status zadania w pliku txt."""
    init_queue()
    rows = []
    updated = False

    with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == task_id:
                row["status"] = new_status
                updated = True
            rows.append(row)

    if updated:
        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
