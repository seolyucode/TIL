import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent' : ':)'} #User-Agent #406이라서 추가

response = requests.get(url, headers=headers).text 
#url 뿐 아니라 딕셔너리 감
#200은 오케이 404는 없다 406은 Not Acceptable 
#뱉어낸 애를 response에 저장

#print(response)


text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50') #모든 가로열들 다 잡아서(리스트)

for row in rows: #줄들(리스트) 중 줄
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)

#print(type(rows)) #rows는 리스트 type() 타입 궁금할 때 print(type(rows))
