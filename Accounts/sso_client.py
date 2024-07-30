import requests

def connect_to_monfocusprof(auth_key, institution_user_id, user_type, user_data):
    """
    Fonction pour connecter un utilisateur à monFocusprof via SSO.
    """
    sso_endpoint = "http://13.60.38.30:8000/accounts/institution-sso/"
    
    payload = {
        "auth_key": auth_key,
        "institution_user_id": institution_user_id,
        "user_type": user_type,
        "user_data": user_data
    }
    
    response = requests.post(sso_endpoint, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erreur de connexion SSO: {response.text}")
