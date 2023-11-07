# Madly Cupid Project

Welcome to the Madly Cupid project! This project is a dating website built using Django and incorporates Agora for video calling features. Madly Cupid aims to connect people and facilitate meaningful interactions.

# Landing page

![WhatsApp Image 2023-11-07 at 2 36 43 PM](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/df3f62c8-3354-4a78-a9fd-7797757bd373)

# Login page

![WhatsApp Image 2023-11-07 at 2 36 43 PM (1)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/99eef194-b88f-4cfe-a790-d05418b9658e)

# Signup page

![image](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/8366aacf-7468-4126-a3d4-4e502b24ef13)


# Home page

![WhatsApp Image 2023-11-07 at 2 36 43 PM (4)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/953f30aa-7ff9-4856-8029-f84178bd409f)

# View Profile
![WhatsApp Image 2023-11-07 at 2 36 43 PM (6)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/bb6094fb-a8ec-462e-9d95-0cd91fd860dd)

![WhatsApp Image 2023-11-07 at 2 36 43 PM (7)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/cd46f994-9c24-4e83-a1eb-2c7644c7bcf4)

![WhatsApp Image 2023-11-07 at 2 36 43 PM (8)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/d341b5a9-1d2a-4dbf-97c3-1a3a60586197)

![WhatsApp Image 2023-11-07 at 2 36 43 PM (9)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/8c37e5a7-8583-4048-8efb-2edb9094cae0)

# Chating

![WhatsApp Image 2023-11-07 at 2 36 43 PM (11)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/69adb4c6-9695-4017-9175-19a613fa2b44)

![WhatsApp Image 2023-11-07 at 2 36 43 PM (5)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/cf68346b-817d-4204-877a-64049a439876)

# Video calling

![WhatsApp Image 2023-11-07 at 2 35 08 PM](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/b10b17ce-efcc-4078-ba14-a295583d3cd9)


# Visitor

![WhatsApp Image 2023-11-07 at 2 36 43 PM (10)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/221615c5-1b3e-4621-8f54-64fa89423979)

# Notification

![WhatsApp Image 2023-11-07 at 2 36 43 PM (12)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/14702bee-249b-4156-8bce-099b783cab38)

# Likes

![WhatsApp Image 2023-11-07 at 2 36 43 PM (13)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/13fc0248-1ddf-4bbc-b278-d7f2c94a63a7)


# Terms and Conditions

![WhatsApp Image 2023-11-07 at 2 36 43 PM (14)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/ed054703-c011-4d68-b28b-1fd37df5a7b6)


# Privacy Policy

![WhatsApp Image 2023-11-07 at 2 36 43 PM (15)](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/9e230bd7-c330-49c2-a0ea-6fee95023f5d)




## Setup Instructions

To set up the Madly Cupid project on your local machine, please follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/madly-cupid.git
   ```

2. Navigate to the project directory:
   ```
   cd Major_project
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     virtualenv1\Scripts\activate
     ```
   - For Linux/Mac:
     ```
     source virtualenv1/bin/activate
     ```

4. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Update Agora Credentials:
   - Create an account at [https://www.agora.io/](https://www.agora.io/) and create an app.
   - Once you create your app, you will be provided with an App ID and App Certificate.
   - Update the following files with your Agora credentials:
     - `views.py` file:
       ```python
       def getToken(request):
           appId = "YOUR APP ID"
           appCertificate = "YOUR APPS CERTIFICATE"
           ...
       ```
     - `streams.js` file:
       ```javascript
       ...
       const APP_ID = 'YOUR APP ID';
       ...
       ```

6. Run database migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Access the application:
   - Open your web browser and visit [http://localhost:8000/](http://localhost:8000/) to access the Madly Cupid application.

## Broadcast Notification

To enable broadcast notifications, follow these steps:

1. Ensure you have RabbitMQ installed and running on your machine.

2. Open a new terminal and activate the virtual environment (`virtualenv1`):
   ```
   source virtualenv1/bin/activate
   ```

3. Start the Celery beat service:
   ```
   celery -A Major_project beat -l INFO
   ```

4. Open another terminal and activate the virtual environment (`virtualenv1`):
   ```
   source virtualenv1/bin/activate
   ```

5. Start the Celery worker service:
   ```
   celery -A Major_project.celery worker --pool=solo -l info
   ```
