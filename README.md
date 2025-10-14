# Scholarship Email Lambda Function

AWS Lambda webhook to send scholarship emails via Amazon SES.

## Usage

**POST to webhook:**

```json
{
  "data": {
    "recipient_list": ["student@email.com"],
    "name": "Student Name",
    "scholarship_name": "Scholarship Program", 
    "deadline": "2025-12-01",
    "apply_link": "https://apply-url.com"
  }
}
```

## Response

**Success (200):**

```json
{
  "success": true,
  "message": "Email sent successfully",
  "messageId": "ses-message-id"
}
```

**Error (500):**

```json
{
  "success": false,
  "error": "Error type",
  "message": "Error description"
}
```

## Deploy

```bash
zip main.zip main.py
aws lambda create-function \
  --function-name ScholarshipEmailWebhook \
  --runtime python3.9 \
  --handler main.lambda_handler \
  --code fileb://main.zip
```

## Requirements

- SES domain verified (`eduvision.live`)
- Lambda role with SES permissions

**Support:**  `support@eduvision.live`
