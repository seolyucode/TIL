#요청-주소 응답-문서
import bs4 #파이썬이 보기 쉽게 변환
import requests 
import csv # , , , 쉽게 읽고 쓸 수 있게

url = 'https://www.melon.com/chart/index.htm' #요청 보내는 주소

headers = {'User-Agent' : ':)'} #User-Agent #406이라서 추가 #유무만 검증

response = requests.get(url, headers=headers).text 
#url 뿐 아니라 딕셔너리 감
#200은 오케이 404는 없다 406은 Not Acceptable 
#뱉어낸 애를 response에 저장

#print(response)


text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50') #모든 가로열들 다 잡아서(리스트) rows에

# with open('melon50.csv', 'w', encoding='utf-8') as f:
#     f.write('순위, 제목, 가수\n')
    # for row in rows: #줄들(리스트) 중 줄
    #         rank = row.select_one('td:nth-child(2) > div > span.rank').text
    #         title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    #         artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    #         #print(rank, title, artist)
    #         f.write(f'{rank}, {title}, {artist}\n')

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline='')) #대리작가
writer.writerow(['순위', '제목', '가수'])

for row in rows: #줄들(리스트) 중 줄
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    #print(rank, title, artist)
    writer.writerow([rank, title, artist])

#print(type(rows)) #rows는 리스트 type() 타입 궁금할 때 print(type(rows))


