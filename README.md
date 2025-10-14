# Scholarship Email Lambda Function

Serverless AWS Lambda function to send HTML-formatted scholarship emails via Amazon SES.

---

## Features

- 📧 HTML & plain-text email templates  
- 📱 Mobile-friendly layout  
- 🔧 Dynamic scholarship details  
- ⚡ Serverless & scalable  
- 🛡️ Error handling & SES delivery  

---

## API Usage

**POST JSON payload:**

```json
{
  "recipient_list": ["student@email.com"],
  "name": "Student Name",
  "scholarship_name": "Scholarship Program Name", 
  "deadline": "2025-10-11",
  "apply_link": "https://application-url.com"
}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `recipient_list` | Array | No | Email addresses (default test email) |
| `name` | String | No | Student's name (default "Student") |
| `scholarship_name` | String | No | Scholarship name (default "Scholarship Program") |
| `deadline` | String | No | Application deadline YYYY-MM-DD |
| `apply_link` | String | No | Application URL |

## Response

### Success (200)

```json
{
  "message": "Email sent successfully",
  "messageId": "ses-message-id"
}
```

### Error (500)

```json
{
  "error": "Error type",
  "message": "Error description"
}
```

## Configuration

- **Runtime:** Python 3.9
- **Memory:** 128 MB  
- **Timeout:** 30s
- **Region:** ap-southeast-1

## Dependencies

- `boto3`, `datetime`, `json`

## Prerequisites

- Verified SES domain (`eduvision.live`)
- Lambda execution role with SES permissions

---

**Support:** `support@eduvision.live`
