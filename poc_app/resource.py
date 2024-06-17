from flask import request
from flask_restful import Resource
from firebase_admin import auth
from .models import profiles, Profile

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token['uid']
    except Exception as e:
        return None

class ProfileListResource(Resource):
    def get(self):
        id_token = request.headers.get('Authorization').split(' ').pop()
        uid = verify_token(id_token)
        if not uid:
            return {'message': 'Invalid-token'}, 401

        return jsonify([profile.to_dict() for profile in profiles.values()])

    def post(self):
        id_token = request.headers.get('Authorization').split(' ').pop()
        uid = verify_token(id_token)
        if not uid:
            return {'message': 'Invalid-token'}, 401

        data = request.json
        profile = Profile(user_id=uid, name=data['name'], email=data['email'])
        profiles[uid] = profile
        return profile.to_dict(), 201

class ProfileResource(Resource):
    def get(self, profile_id):
        id_token = request.headers.get('Authorization').split(' ').pop()
        uid = verify_token(id_token)
        if not uid:
            return {'message': 'Invalid-token'}, 401

        profile = profiles.get(profile_id)
        if not profile:
            return {'message': 'Profile not found'}, 404

        return profile.to_dict()

    def put(self, profile_id):
        id_token = request.headers.get('Authorization').split(' ').pop()
        uid = verify_token(id_token)
        if not uid:
            return {'message': 'Invalid-token'}, 401

        data = request.json
        profile = profiles.get(profile_id)
        if not profile:
            return {'message': 'Profile not found'}, 404

        profile.name = data['name']
        profile.email = data['email']
        return profile.to_dict()

    def delete(self, profile_id):
        id_token = request.headers.get('Authorization').split(' ').pop()
        uid = verify_token(id_token)
        if not uid:
            return {'message': 'Invalid-token'}, 401

        profile = profiles.pop(profile_id, None)
        if not profile:
            return {'message': 'Profile not found'}, 404

        return {'message': 'Profile deleted'}
