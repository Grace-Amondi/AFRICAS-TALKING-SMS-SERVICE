
# Setting Up a USSD Service for MicroFinance Institutions
#### A step-by-step guide

- Setting up the logic for USSD is easy with the [Africa's Talking API](docs.africastalking.com/ussd). This is a guide to how to use the code provided on this [repository](https://github.com/Piusdan/USSD-Python-Demo) to create a USSD that allows users to get registered and then access a menu of the following services:

| USSD APP Features                            |
| --------------------------------------------:| 
| Request to get a call from support           | 
| Deposit Money to user's account              |   
| Withdraw money from users account            |   
| Send money from users account to another     |   
| Repay loan                                   |   
| Buy Airtime                                  |  

## Prerequisites

# INSTALLATION AND GUIDE

1. clone/download the project into the directory of your choice

- First, in the config.py file in your root directory and fill in your Africa's Talking API credentials as below.
    
    AT_APIKEY = [your api key]
    AT_USERNAME = [your username]
    AT_NUMBER = [to test calls, enter a live number]
    SMS_CODE = [your sms code]
    PRODUCT_NAME = [your product name]

# requirements

    Python version 2.* 
    AfricastalkingGateway==1.7
    alembic==0.9.1
    click==6.7
    dominate==2.3.1
    Flask==0.12
    Flask-Bootstrap==3.3.7.1
    Flask-Migrate==2.0.3
    Flask-Script==2.0.5
    Flask-SQLAlchemy==2.2
    Flask-SSLify==0.1.5
    itsdangerous==0.24
    Jinja2==2.9.5
    Mako==1.0.6
    MarkupSafe==1.0
    migrate==0.3.8
    python-editor==1.0.3
    requests==2.13.0
    SQLAlchemy==1.1.6
    visitor==0.1.3
    Werkzeug==0.12.1

-> The project is currently not compatible with future python version

-> Recommendend running the project in a virtual environment


2. Create a virtual environment

          $ makevirtualenv microfinance            # creates a virtual environment
          $ source microfinace/bin/activate        # start the virtual environment

3. Install the project's requirements 

          $ pip install requirements.txt           # download and install project's dependancies

4. Initialise your database

        $ python manage.py runserver             # starts project

5. Run your server

          $ python manage.py runserver             # starts project
          # This command starts your server on https://localhost:5000

- You need to set up on the sandbox and [create](https://sandbox.africastalking.com/ussd/createchannel) a USSD channel that you will use to test by dialing into it via our [simulator](https://simulator.africastalking.com:1517/).

- Assuming that you are doing your development on a localhost, you have to expose your application living in the webroot of your localhost to the internet via a tunneling application like [Ngrok](https://ngrok.com/). Otherwise, if your server has a public IP, you are good to go! Your URL callback for this demo will become:
 http://<your ip address>/ussd/callback

