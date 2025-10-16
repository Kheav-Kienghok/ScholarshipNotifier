def verify_email_template(name, verify_link, year):
    html_body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Verification - EduVision</title>
        <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, Helvetica, sans-serif;
            background-color: #ffffff;
            color: #333333;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            border: 1px solid #e0e0e0;
            background-color: #ffffff;
        }}

        .header {{
            background: linear-gradient(135deg, #004aad 0%, #0066cc 100%);
            padding: 24px 20px;
            text-align: center;
            color: white;
        }}

        .header img {{
            width: 160px;
            height: auto;
            margin-bottom: 8px;
        }}

        .header h1 {{
            font-size: 16px;
            opacity: 0.9;
            margin: 0;
        }}

        .content {{
            padding: 30px;
        }}

        .content p {{
            font-size: 15px;
            line-height: 1.6;
            color: #333333;
        }}

        .button {{
            display: inline-block;
            background-color: #0b66c3;
            color: #ffffff !important;
            text-decoration: none;
            padding: 12px 22px;
            border-radius: 4px;
            margin: 20px 0;
            font-weight: bold;
        }}
        .link {{
            word-break: break-all;
            color: #0b66c3;
            text-decoration: none;
        }}
        .small-text {{
            font-size: 13px;
            color: #666666;
            margin-top: 20px;
        }}
        .logo-image {{
            max-width: 120px;
            width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }}
        @media screen and (max-width: 480px) {{
            .logo-image {{
                max-width: 100px;
            }}
        }}
        @media screen and (max-width: 320px) {{
            .logo-image {{
                max-width: 80px;
            }}
        }}
        .footer {{
            border-top: 1px solid #e0e0e0;
            padding: 20px 30px;
            font-size: 13px;
            color: #555555;
            text-align: center;
        }}
        .footer a {{
            color: #0b66c3;
            text-decoration: none;
        }}
        </style>
    </head>
    <body>
        <span style="display:none!important;color:#fff;max-height:0;max-width:0;opacity:0;overflow:hidden;">
            Verify your email address to activate your EduVision account.
        </span>

        <div class="container">
            <div class="content">

                <div class="header">
                    <img src="https://pub-19a672e964fd4f28b0edebb5b4c986a9.r2.dev/logo-nobg.png" alt="EduVision Logo" draggable="false" style="user-select:none; -webkit-user-drag:none;">
                </div>

                <p>Dear <strong>{name}</strong>,</p>

                <p>Thank you for signing up with <strong>EduVision</strong>! Before we can activate your account, we need to verify your email address.</p>

                <a href="{verify_link}" class="button" style="color: #ffffff; background-color: #0b66c3;" target="_blank" rel="noopener">Verify Email Address →</a>

                <p>If the button above doesn’t work, copy and paste the link below into your browser:</p>
                <p><a href="{verify_link}" class="link" target="_blank" rel="noopener">{verify_link}</a></p>

                <p class="small-text">
                    This link will expire in 24 hours. If you didn’t create an account with EduVision, please ignore this message.
                </p>

                <p>Thank you,<br><strong>The EduVision Team</strong></p>
            </div>

            <div class="footer">
                <p>© {year} EduVision. All rights reserved.</p>
                <p>Helping students find and secure educational funding worldwide.</p>
                <p><a href="https://eduvision.live">Visit our website</a> | <a href="mailto:support@eduvision.live">Contact support</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_body


def template_plain_text(name, verify_link):
    html_body = f"""
    Verify Your Email Address - EduVision

    Dear {name},

    Thank you for creating an account with EduVision! Please verify your email address to activate your account.

    Verification link: {verify_link}

    This link will expire in 24 hours. If you didn’t create an account with EduVision, please ignore this message.

    Best regards,
    The EduVision Team
    """

    return html_body
