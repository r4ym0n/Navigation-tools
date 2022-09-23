import requests
import re

def get_title(url):
    s = requests.session()
    result = s.get(url)
    result.encoding = 'utf-8'
    content = result.text
    print(content)
    title = re.findall('<title>(.*)</title>', content)[0]
    return title


title = get_title('https://baidu.com')
