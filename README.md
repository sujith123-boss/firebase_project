# POC Application with Flask and Firebase Authentication

This project is a Proof of Concept (POC) application using Flask and Firebase Authentication. It includes a simple HTML page for client authentication and API interaction.

## Project Structure

poc_app/
├── app.py
├── api/
│ ├── init.py
│ ├── models.py
│ ├── resources.py
│ └── config.py
└── templates/
└── index.html


## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- Firebase project with authentication enabled
- Firebase Admin SDK service account key

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/poc_app.git
    cd poc_app
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install Flask firebase-admin Flask-RESTful
    ```

### Configuration

1. **Set up Firebase Admin SDK:**

   Replace placeholders in `app.py` with your actual Firebase credentials. You can find these details in your Firebase project's service account key.

   ```python
   # app.py
   firebase_config = {
       "type": "service_account",
       "project_id": "auth-f633a",
       "private_key_id": "YOUR_PRIVATE_KEY_ID",
       "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
       "client_email": "firebase-adminsdk-abcde@auth-f633a.iam.gserviceaccount.com",
       "client_id": "YOUR_CLIENT_ID",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_x509_cert_url": "YOUR_CLIENT_CERT_URL"
   }

Running the Application
Start the Flask app: python app.py


Open a web browser and go to http://127.0.0.1:5000/. You should see the HTML page for signing in and calling the API.






