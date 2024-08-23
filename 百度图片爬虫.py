import os
import urllib
import requests

#paginator 为页数
def get_param(keyword, paginator):
    #把中文搜索词转换为符合规则的编码
    keyword = urllib.parse.quote(keyword)
    params = []
    #为爬取的每页链接定制参数
    for i in range(1,paginator + 1):
        params.append(
            f"tn=resultjson_com&logid=10111382095455918310&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=0&pn={(i-1)*30}&rn=30"
            )
    return params


def get_urls(url,params):
    urls = []
    for param in params:
        urls.append(url + param)
    return urls

def get_image_url(urls,headers):
    image_url = []
    for url in urls:
        page_json = requests.get(url,headers = headers).json()
        page_data = page_json.get("data")
        for data in page_data:
            if data:
                image_url.append(data.get("thumbURL"))
    return image_url

def get_image(keyword,image_url):
    file_name = os.path.join('.',keyword)
    print(file_name)
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    for index,url in enumerate(image_url,start= 1):
        with open(file_name + "/{}.jpg".format(index),"wb") as f:
            f.write(requests.get(url,headers = headers).content)
        if index != 0 and index % 30 == 0:
            print("第{}页下载完成".format(index/30))

if __name__ == "__main__":
    url = "https://image.baidu.com/search/acjson?"
    headers = {
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Safari/537.36"
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0"
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0"
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://image.baidu.com/",
        "Accept-Language": "en-US,en;q=0.9"
    }
    keyword = "玫瑰花"
    page = 2
    params = get_param(keyword,page)
    urls = get_urls(url,params)
    image_url = get_image_url(urls,headers)
    get_image(keyword,image_url)