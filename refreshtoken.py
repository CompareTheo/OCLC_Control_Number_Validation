import requests
import re

token_url = "https://oauth.oclc.org/token"
callback_uri = "https://library.lmu.edu"

client_id = 'c8xdg03m0ENtsvOtUqtijdxmxbtvYPv7uuWxJOzpXs6nMnILMh6UHfPGqbN5ryS4h6i17NW74tb9voVe'
client_secret = 'twUZCIQdXvRgHYz0mLVwCwLZ0h87VUPr'

def refreshing_token():
	r_token = open('refresh.log')
	for line in r_token:
		refresh = line.strip()
		print(refresh)
		data = {'grant_type': 'refresh_token', 'refresh_token': refresh, 'redirect_uri': callback_uri}
		print("refreshing token")
		refresh_token_response = requests.post(token_url, data=data, allow_redirects=False, auth=(client_id, client_secret))

		print('response')
		print(refresh_token_response.headers)
		print('body: ' + refresh_token_response.text)
		response = refresh_token_response.text
		regex = r"(tk_.{36})"
		access = re.search(regex, response)
		token = access.group(1)
		with open('access.log', 'w') as a:
			a.write(token)
		print(token)