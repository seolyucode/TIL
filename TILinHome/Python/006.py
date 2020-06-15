name = 'leeseolyu'
age = 30

# 15자리에 맞춰서 중앙정렬
print('{0:^15}'.format(name))

print('{0:<15}'.format(name))
print('{0:>15}'.format(name))

print('{0:#^15}'.format(name))
print('{0:0<15}'.format(name))
print('{0:!>15}'.format(name))

print(f'제 이름은 {name}입니다. 제 나이는 {age}입니다.')