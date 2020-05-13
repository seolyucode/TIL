Vue CLI

https://cli.vuejs.org

CLI <- Command Line Interface. 명령어를 통한 특정 액션을 수행하는 도구.

Get Started -> Installation -> 

VSCode 터미널 - 새 터미널 - `node -v`

노드 버전 10 이상 확인하기

`npm -v`

6 버전 이상인거 확인하기

`npm install -g @vue/cli`



설치하는 라이브러리가 위치하는 폴더에 파일쓰기 권한 없을 때(관리자 권한 아니라서) 에러나면

`sudo npm install -g @vue/cli`



[설치된 내용들 어디?](https://stackoverflow.com/questions/5926672/where-does-npm-install-packages)



[Vue CLI 2.x]

`vue init '프로젝트 템플릿 유형' '프로젝트 폴더 위치'`

`vue init 'webpack-simple' '프로젝트 폴더 위치'`



[Vue CLI 3.x]

`vue create '프로젝트 폴더 위치'`



터미널 - 새 터미널

`vue create vue-cli`

default(babel, eslint) 엔터  <- 화살표로 이동

`cd vue-cli`

`npm run serve`

