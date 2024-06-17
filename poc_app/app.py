from flask import Flask, jsonify
from flask_restful import Api
import firebase_admin
from firebase_admin import credentials
from api.resources import ProfileResource, ProfileListResource

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('firebasekey.json')
firebase_admin.initialize_app(cred)

api.add_resource(ProfileListResource, '/api/profiles')
api.add_resource(ProfileResource, '/api/profiles/<string:profile_id>')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
