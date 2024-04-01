from flask import jsonify, Blueprint
from apex.models import Property

api = Blueprint('api', __name__)

# Route to retrieve a list of property listings in JSON format
@api.route('/api/property_listings', methods=['GET'])
def property_listings():
    # Query property listings from the database
    property_listings = Property.query.all()

    # Convert property listings to a list of dictionaries
    property_data = []
    for property in property_listings:
        property_data.append({
            'id': property.id,
            'address': property.address,
            'city': property.city,
            'price': property.price,
            'listing_type': property.listing_type,
            'listing_status': property.listing_status,
            'description': property.description,
            'Agent': property.agent.full_name
        })

    # Return property listings in JSON format
    return jsonify(property_data)


# Route to retrieve detailed information about a specific property in JSON format
@api.route('/api/property_details/<int:property_id>', methods=['GET'])
def property_details(property_id):
    # Query property details from the database based on property ID
    property_details = Property.query.get(property_id)

    # Check if property details exist
    if property_details:
        # Convert property details to a dictionary
        property_data = {
            'id': property_details.id,
            'address': property_details.address,
            'city': property_details.city,
            'price': property_details.price,
            'listing_type': property_details.listing_type,
            'listing_status': property_details.listing_status,
            'description': property_details.description,
            'Agent': property_details.agent.full_name
        }
        # Return property details in JSON format
        return jsonify(property_data)
    else:
        # Return error message if property details not found
        return jsonify({'error': 'Property not found'}), 404