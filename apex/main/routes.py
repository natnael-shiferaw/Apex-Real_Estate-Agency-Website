from flask import render_template, Blueprint,request,redirect,url_for,flash
from apex.models import Property, Agent
from apex import mail
from flask_mail import Message
import os

main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def home():
    # Fetches the latest 3 properties
    latest_properties = Property.query.order_by(Property.id.desc()).limit(3).all()
  # Fetch all the Agents in the database.
    agents = Agent.query.all()

  
    return render_template('home.html', latest_properties=latest_properties, agents=agents, title='Home')

@main.route("/buy")
def buy():
    # Pagination Query to get the properties for sale
    page = request.args.get('page', 1, type=int)
    for_sale = Property.query.filter_by(listing_type='sale').paginate(page=page, per_page=5)
    # Query to get the total number of properties for sale
    total_properties_for_sale = Property.query.filter_by(listing_type='sale').count()
    return render_template('buy.html', for_sale=for_sale, total_properties_for_sale=total_properties_for_sale, title='Buy')

@main.route("/rent")
def rent():
    # Pagination Query to get the properties for rent
    page = request.args.get('page', 1, type=int)
    for_rent = Property.query.filter_by(listing_type='rent').paginate(page=page, per_page=5)
    # Query to get the total number of properties for rent
    total_properties_for_rent = Property.query.filter_by(listing_type='rent').count()
    return render_template('rent.html', for_rent=for_rent, total_properties_for_rent=total_properties_for_rent, title='Rent')

@main.route("/listings")
def listings():
    # pagination Query
    page = request.args.get('page', 1, type=int)
    all_properties = Property.query.paginate(page=page, per_page=5)
    # Query to get the total number of properties for rent
    total_properties = Property.query.count()
    return render_template('listings.html', all_properties=all_properties, total_properties=total_properties, title='Listings')

@main.route("/property_details/<property_id>", methods=['GET', 'POST'])
def property_details(property_id):
    property_details = Property.query.filter_by(id=property_id).first()

    if request.method == 'POST':
      # Get form data
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      phone = request.form['phone']
      address = request.form['address']
      zip_code = request.form['zip_code']
      message = request.form['message']

      # The recipients email address
      EMAIL_USER = os.environ.get('EMAIL_USER')

      # Send email
      msg = Message(subject='Contact Form Submission',
                    sender= 'noreply@demo.com',
                    recipients=[EMAIL_USER])
      msg.body = f"""
      First Name: {first_name}
      Last Name: {last_name}
      Email: {email}
      Phone: {phone}
      address: {address}
      zip_code: {zip_code}
      Message:
      {message}
      """
      mail.send(msg)

      flash('Your message has been sent successfully!', 'success')
      return redirect(url_for('main.propery_details', property_id=property_id))


    return render_template('home_property_details.html', property_details=property_details, title='Property Details')


@main.route("/sell", methods=['GET', 'POST'])
def sell():

    if request.method == 'POST':
      # Get form data
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      phone = request.form['phone']
      address = request.form['address']
      zip_code = request.form['zip_code']
      property_address = request.form['property_address']
      bathrooms = request.form['bathrooms']
      bedrooms = request.form['bedrooms']
      property_message = request.form['property_message']
      
      # The recipients email address
      EMAIL_USER = os.environ.get('EMAIL_USER')

      # Send email
      msg = Message(subject='Contact Form Submission',
                    sender= 'noreply@demo.com',
                    recipients=[EMAIL_USER])
      msg.body = f"""
      CONTACT DETAILS:
      First Name: {first_name}
      Last Name: {last_name}
      Email: {email}
      Phone: {phone}
      address: {address}
      zip_code: {zip_code}
      
      PROPERTY DETAILS:
      property_address: {property_address}
      bathrooms: {bathrooms}
      bedrooms: {bedrooms}
      Message:
      {property_message}
      """
      mail.send(msg)

      flash('Your message has been sent successfully!', 'success')
      return redirect(url_for('main.sell'))
  
    return render_template('sell.html', title='Sell')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/agent_details/<agent_id>", methods=['GET', 'POST'])
def agent_details(agent_id):
    agent_details = Agent.query.filter_by(id=agent_id).first()

    if request.method == 'POST':
      # Get form data
      full_name = request.form['full_name']
      email = request.form['email']
      phone = request.form['phone']
      message = request.form['message']
      EMAIL_USER = agent_details.email

      # Send email
      msg = Message(subject='Contact Form Submission',
                    sender= 'noreply@demo.com',
                    recipients=[EMAIL_USER])
      msg.body = f"""
      Full Name: {full_name}
      Email: {email}
      Phone: {phone}
      Message:
      {message}
      """
      mail.send(msg)

      flash('Your message has been sent successfully!', 'success')
      return redirect(url_for('main.agent_details', agent_id=agent_id))
  
    return render_template('agent_details.html', agent_details=agent_details, title='Agent Details')


@main.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        EMAIL_USER = os.environ.get('EMAIL_USER')

        # Send email
        msg = Message(subject='Contact Form Submission',
                      sender= 'noreply@demo.com',
                      recipients=[EMAIL_USER])
        msg.body = f"""
        First Name: {first_name}
        Last Name: {last_name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """
        mail.send(msg)

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))

    return render_template('contact.html', title='Contact')