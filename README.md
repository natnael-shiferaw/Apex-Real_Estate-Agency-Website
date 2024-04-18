# Apex Real Estate Agency

### A Flask web application for a real estate agency.

![Image](https://i.imgur.com/KEA7Ve8.png)

---

## About the Project

 The project aims to develop a comprehensive web application for a real estate agency, catering to the diverse needs of buyers, sellers, landlords, and agents in the property market. The application provides users with a seamless platform to browse properties for sale or rent, while also offering sellers and landlords the ability to easily connect with the agency to list their properties. Additionally, the project includes a robust dashboard for real estate agents, empowering them to manage properties efficiently through CRUD operations, as well as providing a streamlined registration and login process for agents.

 `This project mainly includes two interfaces: `

## 1. Client-facing Interface

- This is the interface for the users(Buyers, Renters, Landlords and Sellers.
- In this interface the users can browse properties, view listings, communicate with the real estate agents and contact the agency for inquiries and transactions.
- In this interface users can easily filter property listings to view only those available for sale or rent, streamlining their search process and ensuring they find properties that        match their needs and preferences.


---
## Routes for the client-facing Interface 

## Buy

This route shows properties available for sale, allowing users to browse listings, filter properties based on their preferences, and explore detailed information about each property.

![Images for the Buy Route](https://i.imgur.com/JONRp4i.png)

---

## Rent

This Route displays properties available for rent, enabling users to search for rental properties, view listings, and gather essential details such as rental rates and property features.

![Image for the Rent Route](https://i.imgur.com/ycD9Ua8.png)

---

## Sell

This Route provides information and resources for users interested in selling their properties. This page will include guidance on the selling process, benefits of listing with the agency, and a contact form for sellers to get in touch with agents.

![Image for Sell Route](https://i.imgur.com/OHgvCyK.png)

---

## 2. Agents Dashboard Interface

This interface is located at (**/admin/agents**) route. For instance in the deployed site, It's found at https://apex-real-estate-agency-website-m2z3.onrender.com/admin/agents.

- Agents can easily register and create accounts to gain access to the dashboard, streamlining the onboarding process and ensuring seamless interaction with the system.
- The dashboard provides agents with a secure login feature, allowing them to access their accounts and manage property listings with ease.
- Agents have the ability to add new property listings, update existing details, and remove properties from the database as needed, ensuring accurate and up-to-date information for 
 clients.
- Additionally, agents can manage their profiles, ensuring that their contact information and other details are kept current.

![Image for agents dashboard](https://i.imgur.com/EyfaTXn.png)

---

## Routes for Agents dashboard Interface

## Create Account

- In this route agents can create an account so they can manage the properties they are representing, add a property, update a property and delete it from the database.

![Image for create account route](https://i.imgur.com/oO7atIk.png)

---

## Login

- In this route agents can securely login to their account to manage their accounts and properties with ease.

![Image for Login Route](https://i.imgur.com/E2JYlYq.png)

---


**After the Agent is logged in, The navigation links would be changed inorder to allow the agents to perform their operations.**

- **User not logged in:**

![Imgae for user not logged in](https://i.imgur.com/LfXOFRr.png)

- **User logged in:**

![Image for navigation change](https://i.imgur.com/1V2zc2G.png) 

---

## Add Property

- This route allows agents to add new property listings to the database, providing fields to input details such as **address**, **price**, **size**, **bedrooms**, **bathrooms**, **amenities**, and **image**.

![Image for add property route](https://i.imgur.com/51Oh5F1.png)

---

## Profile

- This route allows agents to manage their profile. Agents can change their profile picture, add description about them selves, change their password and delete their account.

![Image for agents profile](https://i.imgur.com/rkRKLta.png)

---

## My ads

- This route lists all the properties that are represented by the agent.

![Image for my ads](https://i.imgur.com/77wh327.png)

---

## Property Details

- This route shows all the details of a particular property including it's **image**, **Property description**, **price** and **Property summary**.

![Image for property details](https://i.imgur.com/CsSYVJ9.png)

---

## Edit Property

- This route allow the agents to edit the detials of the property in hand.

![Image for edit property](https://i.imgur.com/qovJKeD.png)

---

## Delete Property

- This route allow the agents to delete the property from the database.

![Image for delete property](https://i.imgur.com/hHlUGUE.png)

---

## Technologies Used

- **In this project, I've achieved the creation of a fully functional real estate web application that addresses the needs of both users and real estate professionals. The architecture of the application follows a client-server model, with the frontend built using HTML5, CSS3, JavaScript, and the Bootstrap framework, while the backend is powered by Python and the Flask framework. Data flows seamlessly between the client and server, allowing users to browse properties, contact the agency, and register/login as agents.**

## Installation

- **Inorder for this flask web application to work, you will need to install all the modules in `requirements.txt` file.**
```
pip install -r requirements.txt
```

- **After installing the required modules, you will need to set the values for the configurations used in the `config.py` file within the apex directory. These values would be set as environment variables.**
![Image for config](https://i.imgur.com/bJNd4go.png)

*For the configurations, you will set the environment variables with the values you would be using.*

1. `SECRET_KEY`: This secret key would be used for secure sessions and you will need to set your own secret key.
2. `SQLALCHEMY_DATABASE_URI`: represents the Uniform Resource Identifier (URI) used by SQLAlchemy to connect to a database. It contains the necessary information to establish a connection to the database, including the database dialect, username, password, host, port, and database name.
   Me Personally, I have used a sqlite database used locally which is located in the directory named `instance` and within this directory a file named `realestate.db`. Here is the value    for the environment variable. ```sqlite:///realestate.db```
3. `EMAIL_USER`: This is the email address for your real estate agency.
4. `EMAIL_PASSWORD`: This is the password for the email address you provided.

**You can change the values for `MAIL_SERVER`, `MAIL_PORT` and `MAIL_USE_TLS`, if you are using a different email provider other than gmail.**

---

### Deployed Website

- Here is the link for the deployed site. [click here](https://apex-real-estate-agency-website-m2z3.onrender.com)

### Landing Page

- Here is the link for the landing page. [click here](https://apex-realestate-landing-page.my.canva.site/apex-real-estate-website)

### [Linkedin](www.linkedin.com/in/natnaelshiferaw)

---
