my = [1, 2, 3, 4, 5, 8] #리스트는 순서O 인덱스 접근

real = [1, 2, 3, 4, 5, 7]
bonus = 8

match = set(my).intersection(set(real)) #집합. 순서X
# print(len(match))
match_count = len(match)

# [1, 2, 3] => list / {1, 2, 3} => set / (1, 2, 3) => tuple / {'a' : A} => dict

if match_count == 6:
    result = '1등' #print는 디버깅용(값확인. 코드 종결X)
elif match_count == 5:
    #if is_bonus == True:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝ㅠ'

print(result)


# my와 real의 6개가 같으면 1등
# my와 real이 5개가 같고 나머지 하나가 bonus면 2등
# my와 real이 5개가 같으면 3등
# '' 4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝



s2s3_student1 = {
    'name' : '김싸피',
    'age' : 22,
}

s2s3 = [s2s3_student1, ] 

