import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 587
smtp_server = "smtp.gmail.com"
 
email_from =             # ........     #the one who is sending the email
email_list = []   #............... # the ones who are receiving the email.
passkey =       #....................   #passkey from the app paswords

subject = #.............................       #the subject of the email

def send_emails(email_list):
    try:
        # Connect to the server
        print("Connecting to the server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, passkey)
        print("Successfully connected to the server")
        print()

        for person in email_list:
            body = f"""
            #..............................................the body of the email.
            """

            # Make a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            filename = #...............name of the file
            try:
                with open(filename, 'rb') as attachment:
                    # Encode as base64
                    attachment_package = MIMEBase('application', 'octet-stream')
                    attachment_package.set_payload(attachment.read())
                    encoders.encode_base64(attachment_package)
                    attachment_package.add_header('Content-Disposition', f"attachment; filename={filename}")
                    msg.attach(attachment_package)
            except FileNotFoundError:
                print(f"Attachment file {filename} not found")
                continue

            # Cast as string
            text = msg.as_string()

            # Send emails to "person" as list is iterated
            print(f"Sending email to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"Email sent to: {person}")
            print()

        TIE_server.quit()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

send_emails(email_list)
