import requests

url = 'your-api-link'
fp = 'darkest.jpg'

files = {'image': open(fp, 'rb')}
payload = {'txt': '1234'}

response = requests.post(url, files=files, data=payload, verify=False)

res = response.json()
print(res)
