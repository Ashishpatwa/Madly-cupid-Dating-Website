# Madly Cupid Project

Welcome to the Madly Cupid project! This project is a dating website built using Django and incorporates Agora for video calling features. Madly Cupid aims to connect people and facilitate meaningful interactions.

# Landing page

![WhatsApp Image 2023-11-07 at 2 36 43 PM](https://github.com/Ashishpatwa/Django-Madly-cupid/assets/52313013/df3f62c8-3354-4a78-a9fd-7797757bd373)


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
