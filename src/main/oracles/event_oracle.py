import requests
from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

class EventOracle:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback_url):
        self.subscribers.append(callback_url)

    def notify_subscribers(self, event_data):
        for subscriber in self.subscribers:
            try:
                requests.post(subscriber, json=event_data)
            except Exception as e:
                print(f"Error notifying subscriber {subscriber}: {e}")

    @app.route('/event', methods=['POST'])
    def handle_event():
        event_data = request.json
        print(f"Received event: {event_data}")
        event_oracle.notify_subscribers(event_data)
        return jsonify({"status": "success"}), 200

    def start(self):
        app.run(port=5000)

# Example usage
if __name__ == "__main__":
    event_oracle = EventOracle()
    event_oracle.subscribe('http://localhost:6000/handle_event')  # Example subscriber
    event_thread = Thread(target=event_oracle.start)
    event_thread.start()
