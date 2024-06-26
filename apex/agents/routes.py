from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from apex import db, bcrypt
from apex.models import Agent,Property
from apex.agents.forms import RegistrationForm, LoginForm, PropertyForm
from apex.agents.utils import save_profile_picture


agents = Blueprint('agents', __name__)

@agents.route("/admin/agents", methods=['GET', 'POST'])
def home_agent():
  # Fetch all properties for sale
  for_sale = Property.query.filter_by(listing_type='sale').all()

  # Fetch all properties for rent
  for_rent = Property.query.filter_by(listing_type='rent').all()

  return render_template("home_agent.html", for_sale=for_sale, for_rent=for_rent)

@agents.route("/admin/agents/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('agents.home_agent'))
  form = RegistrationForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      agent = Agent(username=form.username.data, email=form.email.data, full_name=form.full_name.data, phone_number=form.phone_number.data, password=hashed_password)
      db.session.add(agent)
      db.session.commit()
      flash('Your account has been created! You are now able to log in', 'success')
      return redirect(url_for('agents.login'))
  return render_template('register.html', title='Register', form=form)

@agents.route("/admin/agents/login", methods=['GET', 'POST'])
def login():
      if current_user.is_authenticated:
          return redirect(url_for('agents.home_agent'))
      form = LoginForm()
      if form.validate_on_submit():
          agent = Agent.query.filter_by(email=form.email.data).first()
          if agent and bcrypt.check_password_hash(agent.password, form.password.data):
              login_user(agent, remember=form.remember.data)
              next_page = request.args.get('next')
              return redirect(next_page) if next_page else redirect(url_for('agents.home_agent'))
          else:
              flash('Login Unsuccessful. Please check email and password', 'danger')
      return render_template('login.html', title='Login', form=form)


@agents.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('agents.home_agent'))

# Route to add a new property
@agents.route("/admin/agents/add_property", methods=['GET', 'POST'])
@login_required
def add_property():
    form = PropertyForm()
    if form.validate_on_submit():
        # Extracting data from the form
        address = form.address.data
        city = form.city.data
        property_size = form.property_size.data
        num_bedrooms = form.num_bedrooms.data
        num_bathrooms = form.num_bathrooms.data
        num_carspaces = form.num_carspaces.data
        description = form.description.data
        image_link = form.image_link.data
        agent_id = current_user.id
        price = form.price.data
        listing_status = form.listing_status.data
        listing_type = form.listing_type.data

        # Creating a new Property object and adding it to the database
        property = Property(
            address=address,
            city=city,
            property_size=property_size,
            num_bedrooms=num_bedrooms,
            num_bathrooms=num_bathrooms,
            num_carspaces=num_carspaces,
            description=description,
            image_link=image_link,
            agent_id=agent_id,
            price=price,
            listing_status=listing_status,
            listing_type=listing_type
        )
        db.session.add(property)
        db.session.commit()

        flash('Property has been added successfully!', 'success')
        return redirect(url_for('agents.home_agent'))
    return render_template("add_property.html", title='Add Property', form=form)

@agents.route("/admin/agents/profile", methods=['GET', 'POST'])
@login_required
def view_profile():
    """
    This function is used to view the profile of the logged in agent."""
    return render_template('view_profile.html', title='My Profile')

@agents.route("/admin/agents/change_photo", methods=["POST"])
@login_required
def change_photo():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            picture_file = save_profile_picture(photo)
            current_user.profile_pic = picture_file
            db.session.commit()
            flash("Profile photo updated successfully", "success")
            return redirect(url_for("agents.view_profile"))
    flash("Failed to update profile photo. Please select a valid photo", "danger")

@agents.route("/admin/agents/change_password", methods=["POST"])
@login_required
def change_password():
    new_password = request.form.get("new_password")
    hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
    current_user.password = hashed_password
    db.session.commit()
    flash("Password changed successfully", "success")
    return redirect(url_for("agents.view_profile"))

@agents.route("/admin/agents/delete_account", methods=["POST"])
@login_required
def delete_account():
    db.session.delete(current_user)
    db.session.commit()
    flash("Your account has been deleted", "success")
    logout_user()
    return redirect(url_for("agents.home_agent"))


@agents.route("/admin/agents/my_ads", methods=['GET'])
@login_required
def my_ads():
    properties = Property.query.filter_by(agent_id=current_user.id).all()
    return render_template('my_ads.html', title='My Ads', properties=properties)


@agents.route("/admin/agents/property_details/<property_id>", methods=["GET", "POST"])
def property_details(property_id):
    """
    READ - Display ads individually with all data
    Displays the data and a specific ad by ID.
    The user's session is also checked so that the EDIT and DELETE buttons are
    rendered or not in the case of the ad owner.
    """
    # Check if there's a user logged in
    if current_user.is_authenticated:
        property_details = Property.query.filter_by(id=property_id).first()
        agent = current_user.username.upper()
        return render_template("property.html", property_details=property_details, agent=agent)

    # If no user is logged in
    property_details = Property.query.filter_by(id=property_id).first()
    return render_template("property.html", property_details=property_details)

@agents.route("/admin/agents/delete_property/<property_id>", methods=["GET", "POST"])
def delete_property(property_id):
  property_to_delete = Property.query.get(property_id)
  if property_to_delete:

      if current_user == property_to_delete.agent:
          # Deleting the property
          db.session.delete(property_to_delete)
          db.session.commit()
          flash('Property deleted successfully!', 'success')
      else:
          flash('You are not authorized to delete this property.', 'danger')
  else:
      flash('Property not found.', 'danger')

  return redirect(url_for('agents.home_agent')) 

@agents.route("/admin/agents/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):
  property_to_edit = Property.query.get(property_id)
  if property_to_edit:

      if current_user == property_to_edit.agent:
          if request.method == "POST":
              # Update property details
              property_to_edit.address = request.form['address']
              property_to_edit.price = request.form['price']
              property_to_edit.num_bedrooms = request.form['num_bedrooms']
              property_to_edit.num_bathrooms = request.form['num_bathrooms']
              property_to_edit.city = request.form['city']
              property_to_edit.listing_type = request.form['listing_type']
              property_to_edit.description = request.form['description']
              property_to_edit.listing_status = request.form['listing_status']

              # Check if an image link is provided
              if 'image_link' in request.form:
                  property_to_edit.image_link = request.form['image_link']
              # Commit the changes to the database
              db.session.commit()
              flash('Property updated successfully!', 'success')
              return redirect(url_for('agents.property_details', property_id=property_id))
          else:
              return render_template('edit_property.html', property_details=property_to_edit)
      else:
          flash('You are not authorized to edit this property.', 'danger')
          return redirect(url_for('agents.property_details', property_id=property_id))
  else:
      flash('Property not found.', 'danger')
      return redirect(url_for('agents.home_agent'))

@agents.route("/admin/agents/properties_list", methods=['GET', 'POST'])
def properties_list():
    # Get the selected option from the dropdown menu
    selected_option = request.form.get('listing_type')

    # Query properties based on the selected option
    if selected_option == 'For Sale':
        properties = Property.query.filter_by(listing_type='sale').all()
    elif selected_option == 'For Rent':
        properties = Property.query.filter_by(listing_type='rent').all()
    else:
        properties = Property.query.all()

    return render_template("properties_list.html", properties=properties, selected_option=selected_option)

@agents.route('/admin/agents/view_profile/add_description', methods=['POST'])
@login_required
def add_description():
    if request.method == 'POST':
        new_description = request.form.get('description')

        # Update the description attribute of the current agent
        current_user.description = new_description
        db.session.commit()

        flash('Description added successfully!', 'success')
        return redirect(url_for('agents.view_profile'))  # Redirect to the agent's profile page
    else:
        flash('Invalid request method', 'error')
        return redirect(url_for('agents.home_agent'))  # Redirect to the home page
