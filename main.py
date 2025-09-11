import requests

## make post request to twitch api using given client_id, client_secret, and the grant_type ##
client_id = 'k6p44kezorf5wzxox1spqaz5xbr33h'
client_secret = 'bq5cws373sexdjtw3budz1lokfak3n'
params = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}
response = requests.post('https://id.twitch.tv/oauth2/token', params=params)  


## get access token from the reponse's json (which we got from our get request) ##
auth_data = response.json()  
access_token = auth_data['access_token']
#print('Your access token: ' + access_token)


## use access token and client id to get a streamer's data in json form ##
my_headers = {
    'Client-Id': client_id,
    'Authorization' : f'Bearer {access_token}'
}
streamer_name = 'NorthernLion'
streamer = requests.get(f'https://api.twitch.tv/helix/users?login={streamer_name}', headers=my_headers)
streamer_data = streamer.json()
#print('Streamer's data: ' + streamer_data)


## use streamer's data to determine if they are live or not ##
if streamer_data['data'][0]['type']:
   print(f'{streamer_name} is live')
else:
    print(f'{streamer_name} is offline')