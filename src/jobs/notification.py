def send_email(email: str, message: str) -> None:
    with open(f"notifications/emails.md", "a") as file:
        file.write(f"- Notification for {email}:\n\t{message}")