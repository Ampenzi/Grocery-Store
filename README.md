# Grocery-Store
THIS IS A WEB APP FOR A GROCERY STORE. THE APP ALLOWS USER TO SIGN UP, LOGIN, SHOP AND MAKE ORDERS ONLINE.
THE ADMIN CAN ALSO UPDATE PRODUCT DETAILS AND ORDER DETAILS.
THE APP IS COMPLETE AND CAN BE DEPLOYED EVEN THOUGH A FEW SETTING MIGHT NEED TO BE CHANGED. 
TO RUN THE APP FOLLOW THE STEPS BELOW!


````Requirements````
---Python 3.1 +
---Django
---Code Editor 

# INSTALLATION RUNNING
ONES YOU HAVE DOWNLOADED OR CLONE THE APP
1. Create Virtual Environment:
    (1) virtualenv venv
    (2) venv\scripts\activate #for windows or source/bin/activate #for linux
2. Install requirements
    pip install -r requirements.txt
3. run migrations using:
    python manage.py migrate
4. create super user
    python manage.py createsuperuser 
        Using prompt assign:
            ===username
            ===password
3. Start local server
    `python manage.py runserver `
