import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

data = json.loads(response)
#print(type(data), data)

print(data['bnusNo'])

'''
real_numbers = data["drwtNo1"]
print(real_numbers)
real_numbers = data["drwtNo2"]
print(real_numbers)
'''

'''
#1
real_numbers = []
for i in range(6): #drwtNo 개수를 모르면
    real_numbers[i] = data[f'drwtNo{i}'] #f-string
'''

#2
real_numbers = []
for key, value in data.items(): #딕셔너리는 for문에서 키값만 나와서, .items() 쓰면 키,value같이
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)


#True가 나옴. 
#print(response == '{"totSellamnt":81961886000,"returnValue":"success","drwNoDate":"2019-07-06","firstWinamnt":2240409000,"drwtNo6":39,"drwtNo4":34,"firstPrzwnerCo":9,"drwtNo5":37,"bnusNo":12,"firstAccumamnt":20163681000,"drwNo":866,"drwtNo2":15,"drwtNo3":29,"drwtNo1":9}') 
#print(response['bnusNo'])
#print(response)
#print(type(response)) # str

#print(dict(response))

'''
    {#딕셔너리
        "totSellamnt":81961886000,    # 총 판매금액
        "returnValue":"success",      # 성공적으로 응답
        "drwNoDate":"2019-07-06",     # 추첨일
        "firstWinamnt":2240409000,    # 1등 금액
        "drwtNo6":39,                 # no6
        "drwtNo4":34,                 # no4
        "firstPrzwnerCo":9,           # 1등 당첨자 수
        "drwtNo5":37,                 # no5
        "bnusNo":12,                  # bonus
        "firstAccumamnt":20163681000, # 
        "drwNo":866,                  # 회차
        "drwtNo2":15,                 # no2
        "drwtNo3":29,                 # no3
        "drwtNo1":9                   # no1
    }
'''