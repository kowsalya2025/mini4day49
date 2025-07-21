# app.py
from flask import Flask, render_template, flash
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy credentials
DUMMY_EMAIL = "user@example.com"
DUMMY_PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            flash("Login successful", "success")
        else:
            flash("Invalid credentials", "error")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
