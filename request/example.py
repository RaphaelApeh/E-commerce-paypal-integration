import requests
# payload = {'username':'admin','password':'webly.com'}
response = requests.get('https://httpbin.org/get')

# with open('index.html','wb') as f:
#     f.write(response.content)
print(response.url)