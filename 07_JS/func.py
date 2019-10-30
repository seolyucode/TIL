# x = lambda x, y: x + y
# print(x(1, 2))

# print((lambda x, y: x + y)(1, 2))

# # add sub mul div

# class Calculator:
#     @classmethod
#     def add(x, y):
#         return x + y

# Calculator.add(1, 2)

def add(x, y):
    return x + y

calculator = {
    'add': add,  
    'sub': lambda x, y: x - y,
    'mul': None,
}

# key는 string / value는 객체

print(calculator['add'](1, 2))
print(calculator['sub'](1, 2))

# 1급 객체 : int string arr/list obj/dict FUNCTION
# 인자로 넘어갈 수 있고, return 으로 나올 수 있다.
'''
from . import views

path('asdf/', views.index)
addEventListener('click', 콜백함수)
addEventListener('click', function(){
    console.log('클릭')
})
..
def index(request):
    return HttpResponse
'''

def a():
    def add(x, y):
        return x + y
    
    return add

print(a()(1, 2))


addd = a()
print(addd(2, 3))

# map func 1st arg must be FUNCTION

new_list = map(, ['ah', 'eh', 'i'])
new_map = map(str, [1, 2, 3])

a = list(new_map)
# '-ah-'