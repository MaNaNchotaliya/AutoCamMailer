import cv2
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes
import os

def capture_and_send_email():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Specify the new location for storing the image
    image_folder = r" file location "
    image_name = "captured_image.jpg"
    image_path = os.path.join(image_folder, image_name)

    # Capture an image and save it to the new location
    cv2.imwrite(image_path, frame)

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

    # Email configuration
    sender_email = "   "
    receiver_email = "   "
    password = " generated password from google's app password "
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Automated Email with Photo Attachment"

    # Attach image
    ctype, encoding = mimetypes.guess_type(image_path)
    maintype, subtype = ctype.split('/', 1)
    with open(image_path, 'rb') as fp:
        img = MIMEImage(fp.read(), _subtype=subtype)
        img.add_header('Content-Disposition', 'attachment', filename=image_name)
        msg.attach(img)

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Call the function to capture image and send email
capture_and_send_email()
