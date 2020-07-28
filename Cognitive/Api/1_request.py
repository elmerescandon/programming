import requests

url = 'https://www.google.com'
r = requests.get(url)
print(r)
if r.status_code == 200:
    content = r.content
    print(content)
    file = open('google.html','wb')
    file.write(content)
    file.close()
