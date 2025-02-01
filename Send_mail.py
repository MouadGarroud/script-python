# Mouad Garroud
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

sender_email = "your@gmail.com"
receiver_email = "reciever@gmail.com"
password = "password"
start_date = datetime(2025, 1, 1)
end_date = datetime.now()
delta = end_date - start_date
days = delta.days
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60
seconds = delta.seconds % 60
subject = "Anythings"
body = f"{days} days, {hours} hours, {minutes} min, {seconds} sec"
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))
try:
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  
        server.login(sender_email, password)
        server.send_message(msg)  
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

