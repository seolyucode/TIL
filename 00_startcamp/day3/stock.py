#패키지 : 데이터 가져오는 방법 중 1

from iexfinance.stocks import Stock

#company = Stock('TSLA', token = 'pk_277764e8357b441fad2ec55b5e68042b') # 테슬라 주식, 내 토큰 정보

#print(company.get_price())

company = Stock('AAPL', token = 'pk_277764e8357b441fad2ec55b5e68042b') # 테슬라 주식, 내 토큰 정보
print(company.get_quote())


