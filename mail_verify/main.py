import boto3
import os
from dotenv import load_dotenv
from datetime import datetime
from botocore.exceptions import ClientError
from templates import verify_email_template, template_plain_text

load_dotenv()

# SES client setup
ses_client = boto3.client(
    "ses",
    region_name="ap-southeast-1",
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
)


def send_verification_email(recipient_list, name, verify_link):
    sender = "no-reply@eduvision.live"
    subject = "Verify Your Email Address - EduVision"
    year = datetime.now().year

    # HTML email body
    html_body = verify_email_template(name, verify_link, year)

    # Plain-text version
    text_body = template_plain_text(name, verify_link)

    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={"ToAddresses": recipient_list},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {
                    "Text": {"Data": text_body, "Charset": "UTF-8"},
                    "Html": {"Data": html_body, "Charset": "UTF-8"},
                },
            },
        )

        print("✅ Verification email sent successfully!")
        print(f"Message ID: {response['MessageId']}")
        return response

    except ClientError as e:
        print(f"❌ Error sending email: {e.response['Error']['Code']}")
        print(f"Error message: {e.response['Error']['Message']}")
        return None


if __name__ == "__main__":
    recipient_emails = ["khievkeanghok@gmail.com"]
    name = "Keanghok"
    verify_link = "https://eduvision.live/verify?token=abc123"

    send_verification_email(recipient_emails, name, verify_link)
