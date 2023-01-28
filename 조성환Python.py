import requests


headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


for i in range(0, 30, 1):
    url = 'https://www.todayhumor.co.kr/board/view.php?table=bestofbest&no={number}&s_no={s_number}&page=1'.format(number = 464828-i , s_number = 464828-i )
    site = requests.get(url, headers=headers)
    source_data = site.text


    count1 = source_data.count('Ym202301.jpg"')

    for j in range(count1):
        
        pos1 = source_data.find('src="http://thimg')+ len('src="http://thimg') - 12
        source_data = source_data[pos1:]

        pos2 = source_data.find('Ym202301.jpg"') + 12
        
        image_extract_data = source_data[: pos2]

        source_data = source_data[pos2+1:]

        if i + 1 == 3:
            for k in range(1, 9, 1):
                pos1 = source_data.find('src="')+ len('src="')
                source_data = source_data[pos1:]

                pos2 = source_data.find('src=""')

            pos1 = source_data.find('src="')+ len('src="')
            source_data = source_data[pos1:]

            pos2 = source_data.find('.jpg"')
            
            image_extract_data = source_data[: pos2]

        source_data = source_data[pos2+1:]
        print(i+1, '의', j+1, '번째', '이미지', image_extract_data)
