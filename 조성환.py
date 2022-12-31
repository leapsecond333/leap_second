# requests 모듈을 이용해서
# 네이버 뉴스 메인화면에서 있는 뉴스들 제목 전체 가져오기
import requests

# headers없으면 네이버가 요청차단
headers = \
        {'User-Agent' :'Mozilla/5.0(Window NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
a = 20221230

for i in range(6, 1, -1):
    save_news_list = []

    
    for b in range(1, 4, 1):
        print(i, a, b, '='*60)
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=731&mid=shm&sid1=105&date={0}&page={1}'.format(str(a), str(b)) # 원하는 사이트 입력
        current_news_list = []
        site = requests.get(url, headers = headers) # 내용 가져오기
        source_data1 = site.text                    # 인터넷 소스코드를 source_data1변수에 저장

        count1 = source_data1.count('72" alt="')    #뉴스 제목 개수 가져오기

        
        
        for k in range(count1):
            pos1 = source_data1.find('72" alt="')+ len('72" alt="')# 뉴스 제목 앞 부분위치 지정
            source_data1 = source_data1[pos1:]   # 해당 위치로 이동

            pos2 = source_data1.find('"')       # 뉴스 제목 뒷부분까지 위치 지정
            extract_data1 = source_data1[:pos2]  # 앞부분부터 뒷부분까지 내용 추출해서 저장

            source_data1 = source_data1[pos2+1:] # 다음뉴스를 찾기위해 뒷부분을 이동시키기
            current_news_list.append(extract_data1)
                        # 화면에 출력
        if save_news_list == current_news_list:
            print('중복처리')
            continue
        else:
            save_news_list = current_news_list
        k=0
        for n in save_news_list:
            print(k+1, n)
    a = a - 1
