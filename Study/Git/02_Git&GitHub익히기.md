### Git 초기화와 로컬 저장소

`git init`



복습

GitHub에 코드 올리는 과정

1. #### 내 컴퓨터 프로젝트 폴더에 '여기에서 Git을 쓸거다' 라고 명령 `git init`

2. 즐겁게 코딩

3. 내가 변경한 파일 중 올리길 원하는 것만 선택 `git add`

4. 선택한 파일들을 한 덩어리로 만들고 설명 적어주기 `git commit -m '첫페이지 제작'`

5. 코딩 끝났으니 밥 먹고 오기

6. GitHub 사이트에서 프로젝트 저장소 만들기(블로그 만드는거랑 동일)

7. 내 컴퓨터 프로젝트 폴더에 GitHub 저장소 주소 알려주기 `git remote add`

8. 내 컴퓨터에 만들었던 덩어리 GitHub에 올리기 `git push`



이 폴더에서 Git 으로 버전관리 하고 싶어 => `git init`

.git <- 로컬 저장소. 앞으로의 버전 관리 작업. 명령어를 통해 조작

1. 원하는 폴더에서 Git 초기화 하면 그때부터 가능

   `git init`

2. Git 초기화를 하면 .git 이라는 숨겨진 폴더가 만들어짐. 로컬 저장소

3. 로컬 저장소에 내가 만든 버전 정보, 원격 저장소 주소 등이 저장됨

4. 원격 저장소에서 내 컴퓨터로 코드를 받아오면 로컬 저장소가 자동으로 생김

5. 한 폴더에 하나의 로컬 저장소만 유지해야 한다. 새폴더 만들고 작업



로컬 저장소 생성

1. 폴더 생성
2. Git Bash로 만든 폴더 들어가서 `git init` 으로 로컬 저장소 생성

`~` 루트 폴더 최상위 폴더

`pwd` 현재 폴더

`ls` 현재 폴더에 어떤 폴더/파일이 있는지

`cd 폴더이름` Tab키 쳐서 디렉토리 이동

`git init`

`ls -al` 숨김 폴더/파일까지 .git 로컬 저장소 만들어진거 확인

(master)



첫 번째 버전 만들기

`git add`

`git commit`

`git log`



GitHub에 코드 올리는 과정

1. 내 컴퓨터 프로젝트 폴더에 '여기에서 Git을 쓸거다' 라고 명령 `git init`

2. ### 즐겁게 코딩

3. ### 내가 변경한 파일 중 올리길 원하는 것만 선택 `git add`

4. ### 선택한 파일들을 한 덩어리로 만들고 설명 적어주기 `git commit -m '첫페이지 제작'`

5. 코딩 끝났으니 밥 먹고 오기

6. GitHub 사이트에서 프로젝트 저장소 만들기(블로그 만드는거랑 동일)

7. 내 컴퓨터 프로젝트 폴더에 GitHub 저장소 주소 알려주기 `git remote add`

8. 내 컴퓨터에 만들었던 덩어리 GitHub에 올리기 `git push`



덩어리 : 커밋(Commit) = 하나의 버전

최신 버전 이상하면 예전 버전으로 돌아가서 다시 시작, 시간 여행 가능



커밋으로 만들길 원하는 파일만 선택: add(Add)



버전 생성 실습

1. VS Code 에서 README.md, index.html 파일 생성

2. 원하는 파일만 선택하기

   `git add README.md`

3. 메세지를 달아 커밋으로 만들기

   `git commit -m "프로젝트 설명 파일 추가"`

4. 생성한 커밋 보기

   `git log`

`git add .` 전체 파일 추가



커밋

1. 커밋은 '의미 있는 변동사항'을 묶어서 만든다.
2. 버튼 클릭 버그를 고치는데 5가지 파일을 수정했다면 그 5가지를 묶어서 하나의 커밋으로 만든다.
3. 동료 개발자(혹은 미래의 나)가 '버튼 클릭 버그'를 고치는데 어떤 파일을 수정했는지 손쉽게 파악 가능
4. 커밋 메세지는 시간을 들여서라도 잘 적어서 나중에 후회하지 않는다

커밋은 기차처럼 쌓인다



#### 만든 버전 GitHub 에 올리기

`git remote add`

`git push`

GitHub에 코드 올리는 과정

1. 내 컴퓨터 프로젝트 폴더에 '여기에서 Git을 쓸거다' 라고 명령 `git init`

2. 즐겁게 코딩

3. 내가 변경한 파일 중 올리길 원하는 것만 선택 `git add`

4. 선택한 파일들을 한 덩어리로 만들고 설명 적어주기 `git commit -m '첫페이지 제작'`

5. 코딩 끝났으니 밥 먹고 오기

6. ### GitHub 사이트에서 프로젝트 저장소 만들기(블로그 만드는거랑 동일)

7. ### 내 컴퓨터 프로젝트 폴더에 GitHub 저장소 주소 알려주기 `git remote add`

8. ### 내 컴퓨터에 만들었던 덩어리 GitHub에 올리기 `git push`



로컬 저장소와 원격 저장소

내 컴퓨터의 로컬 저장소에서 버전관리가 완벽하게 되고 있는데

GitHub에 올려서 다른 사람들과 함께 버전 관리를 하자

`push`



### 원격 저장소 GitHub에서 만들고 커밋 푸시하기

1. GitHub에 로그인해서 저장소 생성

2. 내 컴퓨터 cat 폴더에 GitHub 저장소 주소 알려주기

   `git remote add origin https://github.com/아이디/이름.git`

   원격 저장소 추가 origin 은 원격저장소 이름

3. 만든 커밋 푸시하기

   `git push origin master`

   origin 리모트에 master 브랜치에

   기본 브랜치 이름이 master

4. GitHub 사이트에서 올라간 커밋 확인

```
$ git push origin master
remote: Permission to seolyulee/Programming.git denied to seolyucode.
fatal: unable to access 'https://github.com/seolyulee/Programming.git/': The requested URL returned error: 403
```

다른 계정이라 오류나서 원래 계정으로 실습할 수 밖에 없었다.

`git remote remove origin`

`git remote add origin https://github.com/계정/리포지토리` <- 그냥 폴더 이동시킴. .git 지우고



### 다른 사람이 만든 저장소 받아오기

`git pull`

#### 원격 저장소를 내 컴퓨터에 받아오기 : 클론(Clone)

원격 저장소에 고양이가 커밋 올렸다

신입 개발자 문어가 이 저장소를 본인 컴퓨터에 받아오고 싶어한다

`clone`

#### 원격 저장소의 데이터 가져오기 : 풀(pull)

그 와중에 고양이가 새로운 버전 '고양3'을 만들어 원격 저장소에 push

이 업데이트 된 데이터는 풀(pull) 명령어로 받아올 수 있다

문어도 물론 커밋을 만들어서 원격 저장소로 Push 할 수 있으나 원격 저장소에 푸시 권환이 있을 경우에만



내 컴퓨터에 oct 폴더 만들고 깃헙의 저장소 받아오기

`git clone https://github.com/아이디/이름.git`

파일 생성 후 add->commit->push

GitHub에서 새 커밋 확인

