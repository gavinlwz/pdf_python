import requests
url="http://fs.pc.kugou.com/202103191909/cd7effc3f2beeaeeaf83c647caa5597c/KGTX/CLTX001/3ff33d85825652161f26f75cf962fa71.mp3"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

url1=requests.get(url,headers=header)
with open("别知己.MP3",'wb') as f:
    r = requests.get(url, timeout=600, verify=False)
    f.write(requests.get(url).content)
# 1
    # f.write(url1.content)
    # http: // music.163.com / song / media / outer / url?id = 网易云音乐接口