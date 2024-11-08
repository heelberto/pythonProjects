import flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return flask.redirect('/success')
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
