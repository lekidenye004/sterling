from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'replace-with-a-random-secret-key'

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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In production: send email or save to database
        flash('Thank you! We will respond within 24 hours.', 'success')
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)