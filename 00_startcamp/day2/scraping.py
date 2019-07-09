import requests # 요청 보내주는
import bs4 # 파이썬 친화적으로 예쁘게 만들어주는


url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
#print(response)
text = bs4.BeautifulSoup(response, 'html.parser')
kospi = text.select_one('#KOSPI_now') #전체 중 선택

print(kospi.text)