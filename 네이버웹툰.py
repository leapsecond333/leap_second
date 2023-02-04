import requests

headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://comic.naver.com/webtoon/weekday'
site = requests.get(url, headers=headers)
source_data = site.text

for i in range(3):
    pos1 = source_data.find('<a href="/webtoon')+len('<a href="/webtoon')
    source_data = source_data[pos1-7:]

    pos2 = source_data.find('"')
    webtoonlink = source_data[: pos2]

    source_data = source_data[pos2+1:]

    pos1 = source_data.find('" class="title" title="')+len('" class="title" title="')
    source_data = source_data[pos1:]

    pos2 = source_data.find('">')
    title = source_data[: pos2]

    source_data = source_data[pos2+1:]

    url = 'https://' + webtoonlink
    site = requests.get(url, headers=headers)
    source_data = site.text




    

                # 파일저장
try:
    file_name = '{0}{1}{2}'.format(title, i, extract_data[-4:])
    ss = requests.get(extract_data, headers=headers)
    file = open(file_name, 'wb')
    file.write(ss.content)
    file.close()
    

except Exception as e:
    print('에러발생', e)
                
