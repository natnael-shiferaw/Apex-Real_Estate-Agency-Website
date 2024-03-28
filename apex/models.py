from datetime import datetime
from apex import db,login_manager
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_agent(agent_id):
    return Agent.query.get(int(agent_id))

class Agent(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  profile_pic = db.Column(db.String(255), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  description = db.Column(db.Text, nullable=False, default='some description')
  phone_number = db.Column(db.String(20), nullable=False)
  full_name = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"Agent('{self.username}', '{self.email}', '{self.profile_pic}')"


class Property(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String(255), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  property_size = db.Column(db.Integer, nullable=False)
  num_bedrooms = db.Column(db.Integer, nullable=False)
  num_bathrooms = db.Column(db.Integer, nullable=False)
  num_carspaces = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=True)
  image_link = db.Column(db.String(255), nullable=True)
  price = db.Column(db.Integer, nullable=False)
  created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  listing_status = db.Column(db.String(50), nullable=False)
  listing_type = db.Column(db.String(50), nullable=False)

  agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
  agent = db.relationship('Agent', backref='properties')

  def __repr__(self):
    return f"Property('{self.address}', '{self.city}')"
