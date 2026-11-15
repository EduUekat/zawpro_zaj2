import sys
import json
import uuid
import pika
from datetime import datetime

QUEUE_NAME = "task_queue"


def get_rabbitmq_connection():
    params = pika.ConnectionParameters(host="localhost", port=8081)
    return pika.BlockingConnection(params)


def produce_task():
    """Generuje 1 rekord pracy i wysyła go do kolejki RabbitMQ."""
    task_id = str(uuid.uuid4())[:8]
    task_data = {
        "id": task_id,
        "type": "phone_call",
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(task_data),
        properties=pika.BasicProperties(
            delivery_mode=2,
        ),
    )
    connection.close()
    print(f"[Producer] Wysłano zadanie do RabbitMQ: ID {task_id}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--batch":
        print("[Producer] Generowanie 100 zadań do RabbitMQ...")
        for _ in range(100):
            produce_task()
        print("[Producer] Pomyślnie wysłano 100 zadań!")
    else:
        produce_task()
