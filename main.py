import json
import boto3
from datetime import datetime
from botocore.exceptions import ClientError
from template import template_plain_text, template


def lambda_handler(event, context):
    # Initialize SES client
    ses_client = boto3.client("ses", region_name="ap-southeast-1")

    try:
        body = event.get("body", event)  # fallback to entire event if 'body' missing
        if isinstance(body, str):
            body = json.loads(body)

        # Extract data array
        data = body.get("data", [])

        # Validate data is a list and not empty
        if not isinstance(data, list) or len(data) == 0:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                },
                "body": json.dumps(
                    {
                        "success": False,
                        "error": "Bad Request",
                        "message": "data must be a non-empty array of objects",
                    }
                ),
            }

        # Process each recipient in the data array
        results = []
        successful_sends = 0
        failed_sends = 0

        for i, recipient_data in enumerate(data):
            try:
                # Extract individual recipient data with defaults
                name = recipient_data.get("name", f"Student {i+1}")
                email = recipient_data.get("email")
                scholarship_name = recipient_data.get(
                    "scholarship_name", "Scholarship Program"
                )
                deadline = recipient_data.get("deadline", "2025-12-31")
                apply_link = recipient_data.get("apply_link", "https://eduvision.live")

                # Validate email is provided
                if not email:
                    results.append(
                        {
                            "index": i,
                            "name": name,
                            "status": "failed",
                            "error": "Email address is required",
                        }
                    )
                    failed_sends += 1
                    continue

                # Send email to individual recipient
                response = send_scholarship_email(
                    ses_client, [email], name, scholarship_name, deadline, apply_link
                )

                if response:
                    results.append(
                        {
                            "index": i,
                            "name": name,
                            "email": email,
                            "status": "success",
                            "messageId": response["MessageId"],
                        }
                    )
                    successful_sends += 1
                else:
                    results.append(
                        {
                            "index": i,
                            "name": name,
                            "email": email,
                            "status": "failed",
                            "error": "Failed to send email",
                        }
                    )
                    failed_sends += 1

            except Exception as e:
                results.append(
                    {
                        "index": i,
                        "name": recipient_data.get("name", f"Student {i+1}"),
                        "email": recipient_data.get("email", "unknown"),
                        "status": "failed",
                        "error": str(e),
                    }
                )
                failed_sends += 1

        # Return summary response
        return {
            "statusCode": 200 if successful_sends > 0 else 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {
                    "success": successful_sends > 0,
                    "message": f"Processed {len(data)} recipients",
                    "summary": {
                        "total": len(data),
                        "successful": successful_sends,
                        "failed": failed_sends,
                    },
                    "results": results,
                }
            ),
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {
                    "success": False,
                    "error": "Invalid JSON",
                    "message": "Request body must be valid JSON",
                }
            ),
        }

    except ClientError as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {
                    "success": False,
                    "error": f'SES Error: {e.response["Error"]["Code"]}',
                    "message": e.response["Error"]["Message"],
                }
            ),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {"success": False, "error": "Internal server error", "message": str(e)}
            ),
        }


def send_scholarship_email(
    ses_client, recipient_list, name, scholarship_name, deadline, apply_link
):
    sender = "no-reply@eduvision.live"
    subject = f"🚨 URGENT: {scholarship_name} - Deadline in 3 Days"

    # Convert string deadline to datetime object, then format it
    try:
        if isinstance(deadline, str):
            deadline_obj = datetime.strptime(deadline, "%Y-%m-%d")
        else:
            deadline_obj = deadline

        friendly_deadline = deadline_obj.strftime("%B %d, %Y")
    except ValueError:
        friendly_deadline = deadline

    year = datetime.now().year

    html_body_content = template(
        name, scholarship_name, friendly_deadline, apply_link, year
    )

    # Plain-text version
    text_body_content = template_plain_text(
        name, scholarship_name, friendly_deadline, apply_link, year
    )

    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={"ToAddresses": recipient_list},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {
                    "Text": {"Data": text_body_content, "Charset": "UTF-8"},
                    "Html": {"Data": html_body_content, "Charset": "UTF-8"},
                },
            },
        )

        print(f"✅ Email sent successfully to {len(recipient_list)} recipients")
        print(f"Message ID: {response['MessageId']}")
        return response

    except ClientError as e:
        print(f"❌ Error sending email: {e.response['Error']['Code']}")
        print(f"Error message: {e.response['Error']['Message']}")
        return None
