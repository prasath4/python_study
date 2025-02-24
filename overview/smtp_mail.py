# import smtplib

# smtp = smtplib.SMTP('smtp.gmail.com',587)
# smtp.starttls()
# smtp.login('prasath3428@gmail.com','jyls ugfp erlm gekv')
# message='this mail from smtp project'
# smtp.sendmail('prasath3428@gmail.com','aadhiprasath3@gmail.com',message)
# print('send successfully')


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "prasath3428@gmail.com"
SENDER_PASSWORD = "jyls ugfp erlm gekv"  # Use App Password if 2FA is enabled
RECEIVER_EMAIL = "aadhiprasath3@gmail.com"

# Create email message
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "Test Email from Python"

# Email body
body = "Hello, this is a test email sent using Python's smtplib."
msg.attach(MIMEText(body, "plain"))

try:
    # Set up the SMTP connection
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Upgrade the connection to secure
    server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login to email account
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())  # Send email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
