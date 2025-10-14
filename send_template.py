import boto3
import os
from dotenv import load_dotenv
from datetime import datetime
from botocore.exceptions import ClientError

load_dotenv()

# SES client
ses_client = boto3.client(
    "ses",
    region_name="ap-southeast-1",
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
)


def send_scholarship_email(
    recipient_list, name, scholarship_name, deadline, apply_link
):
    sender = "noreply@eduvision.live"
    subject = f"Scholarship Opportunity: {scholarship_name}"

    # Convert string deadline to datetime object, then format it
    try:
        if isinstance(deadline, str):
            # Parse the string date (assuming format: "YYYY-MM-DD")
            deadline_obj = datetime.strptime(deadline, "%Y-%m-%d")
        else:
            deadline_obj = deadline
        
        friendly_deadline = deadline_obj.strftime("%B %d, %Y")  # "October 11, 2025"
    except ValueError:
        # If parsing fails, use the original string
        friendly_deadline = deadline

    year = datetime.now().year

    html_body = f"""
    <html>
    <head>
        <style>
            /* Use system fonts + Google Fonts fallback */
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

            body {{
                font-family: 'Roboto', Arial, sans-serif;
                background-color: #f5f6fa;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .container {{
                max-width: 650px;
                margin: 40px auto;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                overflow: hidden;
                border-top: 5px solid #004aad;
            }}
            .header {{
                text-align: center;
                padding: 25px 20px;
                background: #004aad;
                color: white;
            }}
            .header h1 {{
                margin: 0;
                font-size: 30px;
                font-weight: 700;
            }}
            .content {{
                padding: 35px 30px;
            }}
            h2 {{
                color: #004aad;
                margin-top: 0;
                font-size: 24px;
                font-weight: 700;
            }}
            p {{
                font-size: 16px;
                line-height: 1.8;
                margin-bottom: 20px;
            }}
            .deadline-badge {{
                display: inline-block;
                background-color: #d32f2f;
                color: white;
                font-weight: 700;
                padding: 6px 14px;
                border-radius: 6px;
                font-size: 15px;
            }}
            a.button {{
                display: inline-block;
                padding: 16px 28px;
                margin-top: 15px;
                background-color: #004aad;
                color: white;
                text-decoration: none;
                font-weight: 700;
                border-radius: 8px;
                font-size: 17px;
            }}
            a.button:hover {{
                background-color: #00337f;
            }}
            .links {{
                margin-top: 30px;
                font-size: 15px;
                color: #555;
                line-height: 1.7;
            }}
            .links a {{
                color: #004aad;
                text-decoration: none;
                font-weight: 500;
            }}
            .links a:hover {{
                text-decoration: underline;
            }}
            .footer {{
                text-align: center;
                font-size: 13px;
                color: #888;
                padding: 20px;
                border-top: 1px solid #eee;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>EduVision</h1>
            </div>
            <div class="content">
                <h2>{scholarship_name} Scholarship Opportunity</h2>
                <p>Dear {name},</p>

                <p>We are excited to share details about the <strong>{scholarship_name}</strong> scholarship opportunity.</p>

                <p>Application Deadline: <span class="deadline-badge">{friendly_deadline}</span></p>

                <p>To apply, click the button below:</p>

                <a href="{apply_link}" class="button">Apply Now</a>

                <div class="links">
                    <p>If you have any questions, feel free to contact us at 
                    <a href="mailto:support@eduvision.live">support@eduvision.live</a>.</p>

                    <p>Explore other scholarships or contact the university/provider directly for more details:  
                    <a href="https://eduvision.live/scholarships" target="_blank">Main Scholarships Page</a></p>
                </div>

                <p>Best regards,<br>EduVision Team</p>
                <div class="footer">
                    <p>© {year} EduVision. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Plain-text version
    text_body = f"""
    Scholarship Opportunity: {scholarship_name}

    Dear {name},

    We are excited to share details about the {scholarship_name} scholarship opportunity.

    Application Deadline: {deadline}

    Apply here: {apply_link}

    Questions? Email support@eduvision.live or visit https://eduvision.live/scholarships

    Best regards,
    EduVision Team
    """

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

        print("✅ Email sent successfully!")
        print(f"Message ID: {response['MessageId']}")
        return response

    except ClientError as e:
        print(f"❌ Error sending email: {e.response['Error']['Code']}")
        print(f"Error message: {e.response['Error']['Message']}")
        return None


if __name__ == "__main__":
    recipient_emails = ["khievkeanghok@gmail.com"]
    name = "Keanghok"
    scholarship_name = "Techno Digital"
    deadline = "2025-10-11"
    apply_link = "https://www.aupp.edu.kh/scholarships/techno-digital"

    send_scholarship_email(
        recipient_emails, name, scholarship_name, deadline, apply_link
    )
