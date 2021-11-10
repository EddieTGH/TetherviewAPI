import requests

from ln_oauth import auth, headers

credentials = 'credentials.json'
access_token = auth(credentials) # Authenticate the API
headers = headers(access_token) # Make the headers to attach to the API call.

def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get("https://api.linkedin.com/v2/people?q=vanityName&vanityName={vanityName}", headers=headers)
    user_info = response.json()
    return user_info
 
# Get user id to make send connect notif
user_info = user_info(headers)
urn = user_info['id']

personID = "urn:li:person:" + str(urn)

api_url = "https://api.linkedin.com/v2/invitations"

message = "Hi its Josh from Tetherview! Can we connect?"
connectData = {
    "invitee": personID,
    "message": {
        "com.linkedin.invitations.InvitationMessage": {
            "body": message
        }
    }
}

if __name__ == '__main__':
    r = requests.post(api_url, headers=headers, json=connectData)
    r.json()



