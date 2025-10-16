def template(name, scholarship_name, friendly_deadline, apply_link, year):

    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scholarship Opportunity - {scholarship_name}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
                background-color: #f8fafc;
                color: #334155;
                line-height: 1.6;
            }}
            
            .email-container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }}
            
            .header {{
                background: linear-gradient(135deg, #004aad 0%, #0066cc 100%);
                padding: 32px 24px;
                text-align: center;
                color: white;
            }}

            .header img {{
                width: 160px;
                height: auto;
                margin-bottom: 8px;
            }}
            
            .content {{
                padding: 40px 32px;
            }}
            
            .greeting {{
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 24px;
                color: #1e293b;
            }}
            
            .scholarship-info {{
                background-color: #f1f5f9;
                border-radius: 8px;
                padding: 24px;
                margin: 24px 0;
                border-left: 4px solid #004aad;
            }}
            
            .scholarship-name {{
                font-size: 20px;
                font-weight: 700;
                color: #004aad;
                margin-bottom: 12px;
            }}
            
            .deadline {{
                display: inline-flex;
                align-items: center;
                background-color: #dc2626;
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-weight: 600;
                font-size: 14px;
                margin: 16px 0;
            }}
            
            .deadline::before {{
                content: "⏰";
                margin-right: 8px;
            }}
            
            .apply-button {{
                display: inline-block;
                background: linear-gradient(135deg, #004aad 0%, #0066cc 100%);
                color: white;
                text-decoration: none;
                padding: 16px 32px;
                border-radius: 8px;
                font-weight: 600;
                font-size: 16px;
                margin: 24px 0;
                box-shadow: 0 4px 12px rgba(0, 74, 173, 0.3);
                transition: all 0.3s ease;
            }}
            
            .apply-button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0, 74, 173, 0.4);
            }}
            
            .additional-info {{
                background-color: #fefce8;
                border: 1px solid #fde047;
                border-radius: 8px;
                padding: 20px;
                margin: 24px 0;
            }}
            
            .additional-info h3 {{
                color: #a16207;
                font-size: 16px;
                font-weight: 600;
                margin-bottom: 8px;
            }}
            
            .additional-info p {{
                color: #713f12;
                margin-bottom: 8px;
            }}
            
            .additional-info a {{
                color: #004aad;
                text-decoration: none;
                font-weight: 500;
            }}
            
            .footer {{
                background-color: #f8fafc;
                padding: 24px 32px;
                text-align: center;
                border-top: 1px solid #e2e8f0;
            }}
            
            .footer p {{
                color: #64748b;
                font-size: 14px;
                margin-bottom: 8px;
            }}
            
            .footer a {{
                color: #004aad;
                text-decoration: none;
            }}
            
            @media (max-width: 600px) {{
                .email-container {{
                    margin: 0;
                    border-radius: 0;
                }}
                
                .content {{
                    padding: 24px 20px;
                }}
                
                .header {{
                    padding: 24px 20px;
                }}
                
                .scholarship-info {{
                    padding: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <img src="https://pub-19a672e964fd4f28b0edebb5b4c986a9.r2.dev/logo-nobg.png" alt="EduVision Logo" draggable="false" style="user-select:none; -webkit-user-drag:none;">
            </div>
            
            <div class="content">
                <div class="greeting">
                    Greeting {name}! 👋
                </div>
                
                <h3>🚨 Heads up! The deadline for this scholarship’s coming up fast — don’t let this one slip past you.</h3>
                
                <div class="scholarship-info">
                    <div class="scholarship-name">{scholarship_name}</div>
                    <p>This scholarship program offers financial support to deserving students who demonstrate academic excellence and potential.</p>
                    
                    <div class="deadline">
                        Application Deadline: {friendly_deadline}
                    </div>
                </div>
                
                <p>Don't miss this opportunity to invest in your future. Click the button below to learn more and submit your application:</p>
                
                <div style="text-align: center; margin: 32px 0;">
                    <a href="{apply_link}" style="
                        display: inline-block;
                        background-color: #007bff;
                        color: white;
                        padding: 12px 24px;
                        border-radius: 8px;
                        text-decoration: none;
                        font-weight: bold;
                        font-size: 16px;
                    ">🚀 Apply Now</a>
                </div>
                
                <div class="additional-info">
                    <h3>💡 Need Help?</h3>
                    <p>• Questions about the application? Email us at <a href="mailto:support@eduvision.live">support@eduvision.live</a></p>
                    <p>• Browse more scholarships: <a href="https://eduvision.live/scholarships" target="_blank">EduVision Scholarships</a></p>
                    <p>• Application tips and resources available on our website</p>
                </div>
                
                <p style="margin-top: 32px;">Best of luck with your application!</p>
                <p><strong>The EduVision Team</strong></p>
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


def template_plain_text(name, scholarship_name, friendly_deadline, apply_link, year):
    text_body = f"""
    🎓 SCHOLARSHIP OPPORTUNITY: {scholarship_name}

    Hello {name}!

    We're excited to share an amazing scholarship opportunity with you.

    SCHOLARSHIP: {scholarship_name}
    APPLICATION DEADLINE: {friendly_deadline}

    This scholarship program offers financial support to deserving students who demonstrate academic excellence and potential.

    APPLY NOW: {apply_link}

    NEED HELP?
    • Questions? Email: support@eduvision.live
    • More scholarships: https://eduvision.live/scholarships

    Best of luck with your application!

    The EduVision Team
    © {year} EduVision. All rights reserved.
    """

    return text_body
