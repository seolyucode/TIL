# what is git

git : scm(source code manager) / vcs(version control system)

git => 버젼관리를 해주는 감시카메라



### 명령어

`git init` : (master)

`git add <filename>`

`git commit -m '<message>'`

변경사항 저장

`git add <filename>` : 사진 찍기 전

`git commit -m '<message>'`

...



`git status` : 상태를 물어보는 명령어(변경사항)

`git log` : 사진(commit)들 로그를 보여줌

`git push origin master`



`cd ..` : 위로가기(change directory)

`cd TIL` : TIL로 

`mkdir practice_git` : practice_git 디렉토리 만들기

`touch final.txt` : final.txt 생성

`rm final.txt` : 지우기

`~` : home

`python -V` : 파이썬 버전



`git remote add origin https://github.com/seolyucode/practice_git.git`

`git remote -v`

`git push origin master`



ls



`git config --global user.email 'seolyu.90@gmail.com'`

`git config --global user.name 'seolyu'`



`git log`



`pwd` : 현재위치



`mkdir logfile`

`cd logfile/`

`touch a b c d e f`

`cd ..`

`git add logfile/`

`git add .` : 지금 있는 곳 통째로 더하기

`git commit -m 'add all'`

`git push origin master`



`cd ..`

`cd TIL`

`git status`

`git commit -m 'startcamp | learn git | 190708' ` : commit message / 과거형X 현재형O

`git remote add github https://github.com/seolyucode/TIL.git`

`git remote -v` 

`git push github master`



### 배운 것들

`git add .`

`git commit -m 'python | learn list | 190709'`

`git push github master`





### Chrome

```python
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

```



요청 - 주소(Url)

응답 - 문서



wysiwyg :  What You See Is What You Get



```python
print('hi')
```



TIL폴더에 .vscode 폴더 제외하고

.gitignore에 .vscode/



`import requests`

`pip install requests`

`py -m pip install requests`



시스템 환경 변수 편집 - 환경 변수



`py -m venv venv`

`pip install requests`



https://isitchristmas.com/



### scraping.py

```python
import requests # 요청 보내주는
import bs4 # 파이썬 친화적으로 예쁘게 만들어주는


url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
#print(response)
text = bs4.BeautifulSoup(response, 'html.parser')
kospi = text.select_one('#KOSPI_now') #전체 중 선택

print(kospi.text)
```



`pip install bs4` : 긴 텍스트를

`import bs4`



`python -m pip install --upgrade pip` : 노란글씨안보이게하려고



~~~python
import requests # 요청 보내주는
import bs4 # 파이썬 친화적으로 예쁘게 만들어주는


url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#print(response)
text = bs4.BeautifulSoup(response, 'html.parser')
exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value') #전체 중 선택

print(exchange_rate.text)
~~~



```python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent' : ':)'} #User-Agent #406이라서 추가

response = requests.get(url, headers=headers).text 
#url 뿐 아니라 딕셔너리 감
#200은 오케이 404는 없다 406은 Not Acceptable 
#뱉어낸 애를 response에 저장

#print(response)


text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50') #모든 가로열들 다 잡아서(리스트)

for row in rows: #줄들(리스트) 중 줄
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)

#print(type(rows)) #rows는 리스트 type() 타입 궁금할 때 print(type(rows))

```

