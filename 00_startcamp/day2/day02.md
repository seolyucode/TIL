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

