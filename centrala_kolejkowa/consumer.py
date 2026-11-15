import sys
import time
import json
import pika

QUEUE_NAME = "task_queue"


def callback(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["id"]
    consumer_id = sys.argv[1] if len(sys.argv) > 1 else "1"

    print(
        f"[Consumer {consumer_id}] Pobrano zadanie {task_id}. Wykonywanie" " (30s)..."
    )

    time.sleep(30)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"[Consumer {consumer_id}] Zakończono i potwierdzono zadanie {task_id}.")


def consume_loop(consumer_id: str):
    params = pika.ConnectionParameters(host="localhost", port=8081)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print(
        f"[Consumer {consumer_id}] Nasłuchiwanie na zadania w RabbitMQ... (Ctrl+C"
        " aby zatrzymać)"
    )
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()


if __name__ == "__main__":
    c_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    try:
        consume_loop(c_id)
    except KeyboardInterrupt:
        print(f"\n[Consumer {c_id}] Zatrzymany przez użytkownika.")
