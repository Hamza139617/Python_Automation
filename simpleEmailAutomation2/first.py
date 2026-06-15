import email
import imaplib
import os

def checkEmail(searchEmail : str):
    EMAIL = "hamza139617@gmail.com"
    PASSWORD = os.environ.get("API_KEY")

    bot = imaplib.IMAP4_SSL("imap.gmail.com")
    bot.login(EMAIL, PASSWORD)
    bot.select("inbox")

    status, messages = bot.search(None, "ALL")
    email_ids = messages[0].split()



    for e_id in email_ids[-40:]:
        status, msg_data = bot.fetch(e_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        sender = msg["From"]
        subject = msg["Subject"]
        date = msg["Date"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type == "text/plain":
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        body = ""
        else:
            try:
                body = msg.get_payload(decode=True).decode()
            except:
                body = ""

        

        if(searchEmail in sender):
            print(sender)
            print(subject)
            print(date)
            print(body[:200])



if __name__ == "__main__":
    checkEmail("orwellian1396@gmail.com")
        
        


