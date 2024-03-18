from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://avnadmin: AVNS_pw9PoJOC1YqTZpD6nsX@apex-real-estate-apex-real-estate.a.aivencloud.com/defaultdb?charset=utf8mb4'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
      return f"User('{self.username}', '{self.email}', '{self.image_file}')"

@app.route('/')
def home():
    return render_template('layout.html')

@app.route("/agents/register", methods=['GET', 'POST'])
def register():
      form = RegistrationForm()
      if form.validate_on_submit():
          flash(f'Account created for {form.username.data}!', 'success')
          return redirect(url_for('home'))
      return render_template('register.html', title='Register', form=form)


@app.route("/agents/login", methods=['GET', 'POST'])
def login():
      form = LoginForm()
      if form.validate_on_submit():
          if form.email.data == 'admin@blog.com' and form.password.data == 'password':
              flash('You have been logged in!', 'success')
              return redirect(url_for('home'))
          else:
              flash('Login Unsuccessful. Please check username and password', 'danger')
      return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)