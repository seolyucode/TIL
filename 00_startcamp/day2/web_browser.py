import webbrowser

urls = [
    'www.github.com',
    'www.google.com',
    'https://music.youtube.com',
    'https://comic.naver.com',
    'http://edu.ssafy.com'

]

for url in urls:
    webbrowser.open(url)


'''
http://edu.ssafy.com/edu/board/mentoring/detail.do
?
searchBrdItmCdVal=
&
brdItmSeq=2449
&
regUserId=
&
searchMyItm=
&
searchWord=
&
_csrf=9b1a8383-1097-4365-9741-d0700562fdf5
&
pageIndex=1
'''

'''
for i in range(1, 30):
    url = f'http://edu.ssafy.com/edu/board/mentoring/detail.do?searchBrdItmCdVal=&brdItmSeq={i}&regUserId=&searchMyItm=&searchWord=&_csrf=9b1a8383-1097-4365-9741-d0700562fdf5&pageIndex=1'
    webbrowser.open(url)
'''

