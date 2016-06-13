from urllib.error import URLError, HTTPError
import urllib.request
import urllib.parse

url = 'http://tieba.baidu.com/p/2166231880'
values={'wd':'python',  
        'opt-webpage':'on',  
        'ie':'gbk'}  
url_values=urllib.parse.urlencode(values)  
#print(url_values)  
  
url_values=url_values.encode(encoding='UTF8')  
full_url=urllib.request.Request(url,url_values)  
#or ony one sentense:full_url=url+'?'+url_values  
  
try:  
    response=urllib.request.urlopen(full_url)   #open=urlopen  
except HTTPError as e:  
    print('Error code:',e.code)   
except URLError as e:  
    print('Reason',e.reason)  
the_page=response.read()  
print(the_page)  
