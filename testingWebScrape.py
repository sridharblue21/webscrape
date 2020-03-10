import bs4, requests,os

url = 'https://imgs.xkcd.com/comics/machine_learning_captcha.png'
filename = url.split('/')[-1]
print(filename)
fileobj = open(filename , 'wb')
res = requests.get(url)
if res.status_code == 200:
    fileobj.write(res.content)
    fileobj.close()
