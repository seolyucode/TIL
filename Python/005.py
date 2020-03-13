name = 'leeseolyu'
age = 15
n = 8888888888.8888
# print('제 이름은 %s입니다. 제 나이는 %d입니다.' % (name, age))
s = '제 이름은 %s입니다. 제 나이는 %d입니다.'
print(s % (name, age))
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))
print('제 이름은 {0}입니다. 제 나이는 {0}입니다.'.format(name, age))
s = '제 이름은 {name}입니다. 제 나이는 {age}입니다.'
print(s.format(name='seolyu', age=15))
print('{0:4} X {1:4} = {2:4}'.format(2, 3, 6))
print('{0:<4} X {1:<4} = {2:<4}'.format(2, 3, 6))
print('{0:.3f}'.format(1/4.0))
print('{0:.4f}'.format(1/4.0))
print('{0:,.3f}'.format(n))