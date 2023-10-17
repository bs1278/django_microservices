from confluent_kafka import Consumer, KafkaError
import json

# Configure Kafka consumer settings
consumer = Consumer({
    'bootstrap.servers': 'your-kafka-broker',
    'group.id': 'order-events-consumer',
    'auto.offset.reset': 'earliest'
})

# Subscribe to the ORDER_EVENTS_TOPIC
consumer.subscribe(['ORDER_EVENTS_TOPIC'])

def process_order(order_data):
    order_id = order_data.get('order_id')
    # Process the order, update the database, or trigger related actions
    print(f'Order processed: Order ID={order_id}')

def send_order_notification(order_data):
    # Add your order notification logic here
    order_id = order_data.get('order_id')
    user_email = order_data.get('user_email')
    # Send notifications, e.g., order confirmation email
    print(f'Order notification sent for Order ID={order_id} to {user_email}')

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached the end of the partition')
        else:
            print('Error while receiving message: {}'.format(msg.error()))
    else:
        # Process the message based on its key and value
        key = msg.key()
        value = json.loads(msg.value())

        if key == "order_created":
            # Handle order creation event
            order_id = value.get('order_id')
            print('Order created: Order ID={}'.format(order_id))            
            # Process the order
            process_order(value)
            # Send order notifications
            send_order_notification(value)
