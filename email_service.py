from flask_mailman import Mail, EmailMessage
import os

# Initialize Mail without attaching it to an app yet
mail = Mail()

def init_email_service(app):
    """Configures the email system for the Flask app instance."""
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    
    # Securely pulling credentials or falling back to hardcoded strings
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'josephkidenye@gmail.com')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'qhkrccmsuhkzpcph')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'josephkidenye@gmail.com')
    
    mail.init_app(app)

def send_contact_email(name, email, phone, county, location, case_type, message_body):
    """Handles the structural compilation and dispatch of the contact form email."""
    subject = f"New Contact Form Submission from {name}"
    body = f"""
You received a new message from your website contact form.

Name:           {name}
Email:          {email}
Phone:          {phone if phone else 'Not provided'}
County:         {county if county else 'Not provided'}
Location:       {location if location else 'Not provided'}
Case Type:      {case_type if case_type else 'Not specified'}

Message:
{message_body}
    """
    
    # Setup and trigger the email dispatch
    msg = EmailMessage(
        subject=subject,
        body=body,
        from_email=os.environ.get('MAIL_DEFAULT_SENDER', 'josephkidenye@gmail.com'),
        to=[os.environ.get('MAIL_USERNAME', 'josephkidenye@gmail.com')]
    )
    msg.send()
