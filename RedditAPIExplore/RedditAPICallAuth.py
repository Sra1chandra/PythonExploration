# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Get this from the app creation details
CLIENT_ID = 'T92MdXPL42HDkabj6eXHtw'
CLIENT_SECRET = 'ZVEsAY_ROxNnH4bNITR5PhThklxrbg'


# %%
import requests
auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)


# %%
with open('pw.txt','r') as f:
    pw = f.read()


# %%
data = {
    'grant_type' : 'password',
    'username' : 'Numerous_Ingenuity61',
    'password' : pw
}
headers = {'User-Agent': 'MyAPI/0.0.1'}


# %%
res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth,data=data,headers=headers)
ACCESS_TOKEN = res.json()['access_token']
headers['Authorization']= f'bearer {ACCESS_TOKEN}'


# %%
response = requests.get('https://oauth.reddit.com/api/v1/me',headers=headers)


