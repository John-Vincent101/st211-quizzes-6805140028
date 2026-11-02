import smtplib

def send_email(to, subjects):
    server = smtplib.SMTP("smtp.gmail.com")
    server.sendmail("noreply@app.com", to, subject)
    server.quit()
    return True

def notify_user(user_email):
    send_email(user_email, "Welcome!")
    return f"Notified {user_email}"