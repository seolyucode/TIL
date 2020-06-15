lunches = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887'
}

# 파일 쓰기
with open('lunch.csv', 'w', encoding='utf-8') as f: #파일 여는 문법
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')

# 파일 읽기


# for lunch in lunches:
#     print(lunch) #키값
#     print(lunches[lunch])

# for name, phone in lunches.items():
#     print(name, phone)

