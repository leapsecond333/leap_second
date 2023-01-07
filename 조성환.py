import requests


headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

date = [20230103, 20230104, 20230105, 20230106, 20230107]
page = [1, 2, 3, 4]

for i in range(0, 5):
    for j in range(page[3]):
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=731&sid1=105&date={0}&page={1}'.format(date[i], page[j])           

        if j == page[1]:
            extract_data1_save_data = source_data1[:pos2]
            if extract_data1_save_data == extract_data1:
                break
        
        site = requests.get(url, headers=headers)                                                       
        source_data1 = site.text
        source_data2 = site.text

        count1 = source_data1.count('72" alt="')
        count2 = source_data2.count('class="lede">')

        print(date[i], page[j],'='*60)
        for k in range(count1):                                                                         
            pos1 = source_data1.find('72" alt="')+ len('72" alt="')                                       
            source_data1 = source_data1[pos1:]
    
            pos2 = source_data1.find('onError="javascript:this.src=')
            extract_data1 = source_data1[: pos2]

            source_data1 = source_data1[pos2+1:]

            pos3 = source_data2.find('class="lede">')+ len('class="lede">')
            source_data2 = source_data2[pos3:]

            pos4 = source_data2.find('…</span>')
            extract_data2 = source_data2[:pos4]

            source_data2 = source_data2[pos4+1:]
            print('     ', extract_data1, '\n    : ', extract_data2)
