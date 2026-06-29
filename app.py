from flask import Flask, render_template, request, flash, redirect, url_for
from email_service import init_email_service, send_contact_email  # <-- Import your new email module
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'replace-with-a-random-secret-key')

# Initialize the email configurations securely
init_email_service(app)

# ---------- Blog data ----------
blog_posts = [
    {
        'title': 'What to Do Immediately After a Car Accident',
        'date': 'March 22, 2025',
        'excerpt': 'Our personal injury team outlines the critical steps that protect your claim.',
        'link': '#'
    },
    {
        'title': 'High‑Net‑Worth Divorce: Protecting Your Assets',
        'date': 'March 10, 2025',
        'excerpt': 'Complex property division demands experienced legal guidance.',
        'link': '#'
    },
    {
        'title': '2025 Corporate Compliance Checklist',
        'date': 'February 28, 2025',
        'excerpt': 'Stay ahead of new regulations affecting your business.',
        'link': '#'
    }
]

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/practice-areas')
def practice_areas():
    return render_template('practice_areas.html')

@app.route('/attorneys')
def attorneys():
    return render_template('attorneys.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        county = request.form.get('county', '').strip()
        location = request.form.get('location', '').strip()
        case_type = request.form.get('case_type', '').strip()
        message_body = request.form.get('message', '').strip()

        if not name or not email or not message_body:
            flash('Please fill in all required fields (Name, Email, Message).', 'danger')
            return redirect(url_for('contact'))

        try:
            # Simply call your clean standalone email function here!
            send_contact_email(name, email, phone, county, location, case_type, message_body)
            
            flash('Thank you! We will respond within 24 hours.', 'success')
            return redirect(url_for('thank_you'))
        except Exception as e:
            flash(f'Error sending message: {str(e)}. Please try again later.', 'danger')
            return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
