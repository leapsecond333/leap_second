import requests

headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'          
    
site = requests.get(url, headers=headers)                                                       
source_data1 = site.text
source_data2 = site.text

count1 = source_data1.count('&page=1" target="_top">')

for k in range(count1):                                                             # 링크2 subject"><a href="    " target="_top">
    pos1 = source_data1.find('&page=1" target="_top">')+ len('&page=1" target="_top">')
    source_data1 = source_data1[pos1:]

    pos2 = source_data1.find("</a><span class='")
    extract_data1 = source_data1[: pos2]
    source_data1 = source_data1[pos2+1:]


    pos3 = source_data2.find(""""><img src='""")+ len(""""><img src='""")
    source_data2 = source_data2[pos3:]
    
    pos4 = source_data2.find("bgm_icon'/")
    extract_data2 = source_data2[: pos4]
    source_data2 = source_data2[pos4+1:]


    pos3 = source_data2.find('subject"><a href="')+ len('subject"><a href="')
    source_data2 = source_data2[pos3:]
    
    pos4 = source_data2.find('" target="_top">')
    extract_data2 = source_data2[: pos4]
    source_data2 = source_data2[pos4+6:]


    print('     ', extract_data1, '\n')
    print('     ', extract_data2, '\n')
