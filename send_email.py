import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ses_client = boto3.client(
    "ses",
    region_name="ap-southeast-1",
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY')
)

# Check domain verification status
response = ses_client.get_identity_verification_attributes(
    Identities=['eduvision.live']
)

print("Domain verification status:")
print(response)

# Also verify an email address for testing
email_response = ses_client.verify_email_identity(
    EmailAddress='noreply@eduvision.live'  # or any email from your domain
)
print("Email verification response:")
print(email_response)