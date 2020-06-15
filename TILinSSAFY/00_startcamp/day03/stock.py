#패키지 : 데이터 가져오는 방법 중 1

from iexfinance.stocks import Stock
import random

#company = Stock('TSLA', token = 'pk_277764e8357b441fad2ec55b5e68042b') # 테슬라 주식, 내 토큰 정보

#print(company.get_price())
companies = ['AAPL', 'GOOGL', 'TSLA', 'FB', 'AMZN']
#애플 구글 테슬라 페이스북 아마존

company = Stock(random.choice(companies), token = 'pk_277764e8357b441fad2ec55b5e68042b')
company = Stock('AAPL', token = 'pk_277764e8357b441fad2ec55b5e68042b') # 테슬라 주식, 내 토큰 정보
print(company.get_quote())


