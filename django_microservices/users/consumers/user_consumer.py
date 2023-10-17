import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_welcome_email(username, email):
    # Create an instance of SMTP
    server = smtplib.SMTP('your-smtp-server.com', 587)
    server.starttls()
    server.login('your-email@example.com', 'your-password')

    # Create the email message
    subject = "Welcome to Your App"
    message = MIMEMultipart()
    message['From'] = 'your-email@example.com'
    message['To'] = email
    message['Subject'] = subject
    body = f"Dear {username},\n\nWelcome to App! We're excited to have you on board."
    message.attach(MIMEText(body, 'plain'))
    # Send the email
    server.sendmail('your-email@example.com', email, message.as_string())
    server.quit()

# Usage example within the Kafka consumer
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

    if key == "user_signup":
        # Handle user signup event
        username = value.get('username')
        email = value.get('email')
        send_welcome_email(username, email)
        print('User signed up: Username={}, Email={}'.format(username, email))
        # Implement other signup handling logic here
