import requests

proxies = {"http":"115.178.228.219:8080"}
headers  = {"user-agent":"Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

r = requests.get("http://testing-ground.scraping.pro/whoami", proxies=proxies, headers=headers)
print(r.text)
for cookie in r.cookies:
    print(cookie)
print(r.cookie["TestingGround"])
