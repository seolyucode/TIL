#### 소스트리 GUI로 Git 다지기

배울 내용

1. Git GUI인 소스트리로 로컬 저장소 추가하기
2. 애드(Add)와 커밋(Commit)이 무엇인지 스테이지 개념과 함께 이해
3. 브랜치(Branch)로 평행세계 나누기
4. 머지(Merge)로 두 브랜치 합치기
5. 두 브랜치가 충돌(Conflict)났을 때 해결하기
6. 예의바른 병합 요청(Pull request) 보내기
7. 남의 저장소 통째로 복제하기: 포크(Fork)



소스트리(SourceTree) 설치 - GUI 환경 구축

1. 버튼 클릭으로 Git 명령을 실행할 수 있는 도구, 소스트리 설치

   Git 개념을 그래프로 가시적으로 볼 수 있어 편리

   https://ko.atlassian.com/software/sourcetree

2. 설치한 소스트리에 내 컴퓨터에서 이미 만든 로컬 저장소 추가하기

아틀라시안에서 만든 github 같은게 비트버켓

비트버켓 로그인하기

Mercurial 은 깃같은건데 안쓸꺼라서 체크해제

SSH 키 불러오기 아니오 선택



Add

탐색 - cat 폴더 - 추가

새로운 탭으로 oct도 추가

history 보기



### Add 와 Commit

`git init` 

`git add` 스테이지 사진관에 올라감

`git commit` 스테이지에 올라간 애들만 사진 찍음



Git에서의 커밋?

1. 변경 사항 모음(X) 하나의 최종 코드 모음(O)
2. 다만 기존 커밋과 비교해서 변경된 파일이 아니면 '변경되지 않았다'고만 저장해서 용량이 무겁지 않다
   * SVN 은 바로 이전 커밋과의 변경사항만 저장
   * 그래서 커밋당 용량은 더 가볍지만 한 버전을 보려면 맨 처음 커밋부터 계산해야해서 속도 느림
   * Git은 바로 이전 커밋만 보면 된다 -> 속도 빠름



1. Git 으로 추적하는 파일의 4가지 상태

   untracked <- 추적 안됨

   tracked <- 수정 없음, 수정함, 스테이지됨

2. 작업 공간(Working directory)에 있는 '수정함', '추적 안됨' 파일을 스테이지로 올려 '스테이지됨' 으로 변경

3. 커밋을 하면 '수정없음' 상태로 돌아가서 다시 파일을 수정할 수 있다



GUI 실습

cat 파일 수정 후 add, commit, push 하기

oct를 소스트리에 추가하고 pull 받아오기



cat에서 수정 후 GUI 보면

변경사항 있으면 '커밋하지 않은 변경사항' 생김

'커밋하지 않은 변경사항' - 커밋 - +버튼 눌러서 add 스테이지 올림 - 커밋 메세지 작성 - ...

cf) 도구 - 옵션 - 인증 - 계정 추가하기

GitHub HTTPS Basic 사용자명 비밀번호 새로고침 깃허브 비번 쓰고 확인

열어서 Default account for ... 설정 눌러서 '예'

커밋



히스토리 보면

master <- 내 컴퓨터만 있는거

origin/master <- GitHub에도 있는거



Push 누르고 master 선택 push



oct 에서 pull



한 줄로 커밋을 쌓으면 둘이 겹치지 않나?

=> 여러 줄로 쌓으면 됨. 한 줄에서 작업하면 충돌이 날 수 있음. 똑같은 코드를 동시에 고칠 가능성. 여러줄로 쌓으면 충돌나더라도 합치는 시점에 명시적으로 충돌 해결 가능

Branch - 가지

`git push origin master`

master 브랜치(기본으로 만들어져 있음)에 커밋을 푸시

master 브랜치 <- HEAD : 내가 지금 작업하는 로컬 브랜치를 가리킴



`git branch 브랜치이름` <- 브랜치 만들기

`git checkout 브랜치이름` <- 이동



실습

1. cat 저장소 master에서 feat/main-page 브랜치 생성

   feat은 기능의 약자.

2. 커밋 추가

3. oct 에서 pull 받기

4. master 에서 feat/comment 브랜치 생성

5. 커밋 추가



브랜치 눌러서 feat/main-page 브랜치 생성

파일 수정하면 '커밋하지 않은 변경사항' 생김

스테이지에 올리고 커밋과 동시에 푸시



oct 에서 pull 받기

새로운 브랜치 말고 master 기점으로 브랜치 생성

파일 수정 후 '커밋하지 않은 변경사항'

스테이지 올리고 커밋과 동시에 푸시

왼쪽 보면 내 로컬 저장소에 있는 브랜치만 보여주므로 feat/comment만 보임

밑에 원격 origin 보면 다 보임

이동하려면 더블클릭



#### 두 버전 합치기 - 머지(merge)

feat 브랜치에서 작업이 끝나고 master에 합치려면

master 브랜치의 최신 커밋에(base)

cot 브랜치의 최신 커밋(compare)을 합치려고 한다

1. 먼저 base 가 될 master 브랜치로 이동

2. compare 브랜치인 oct를 나와 합치고 싶다라고 명령

   `git merge oct`

3. 합쳐진 결과는 oct 커밋

master 브랜치 더블 클릭해서 feat/main-page 커밋 우클해서 병합

master에 반영됨

원격 저장소 반영 위해 push



합치다가 충돌 : 컨플릭트(conflict)

머지 => 합집합

* Fast-forward
* Merge commit
* Conflict



컨플릭트 해결

=> 머지할 때 두 버전이 같은 곳을 수정했다면 이를 수동으로 고쳐줘야 한다

base

compare



머지, 컨플릭트 해결 실습

1. oct 에서 feat/comment 로 이동 후 '좋아요' 수정
2. master 에 feat/comment 수정본 머지 (머지 커밋 생성 확인)
3. cat 에서 feat/main-page 이동 후 '싫어요' 수정
4. master 에 feat/main-page 수정본 머지(컨플릭트)
5. 컨플릭트 해결

VScode 에서 oct 의 feat/comment 에서 수정 후

옆에 브랜치 클릭해서 변경사항 확인하고 + 버튼 누르면 스테이지 올라감

커밋 메세지 쓰고 V 커밋 클릭

밑에 feat/comment 옆에 새로고침 버튼 클릭하면 push/pull 한다

소스트리 가보면 좋아요 커밋 생긴거 확인

master 브랜치로 넘어간 후 머지를 원하는 대상인 좋아요 커밋 병합

Merge branch 'feat/comment' 생성됨. 

마스터 브랜치에 푸시함



cat feat/main-page 에 싫어요 추가

싫어요 커밋 푸시

싫어요를 마스터브랜치에 merge하려고 하는데

아까 mergecommit 보이지 않음

마스터 브랜치 가서 패치(새로고침)

master를 최신 상태 유지하기 위해 master 우클 가져오기 origin/master

현재 상태

* Merge branch 'feat/comment' 좋아요
* origin/feat/main-page 싫어요 
* 합치면 충돌
* 싫어요 병합하면 충돌남

컨플릭트가 난 파일은 자동으로 '커밋하지 않은 변경사항' - 스테이지 아래에 있게 됨

VScode 에서 git 패널 눌러보면

파일 나오는데, 

```
# cat

Hello Cat!!

## 목록
1. cat
<<<<<<< HEAD
2. 좋아요
=======
2. 싫어요
>>>>>>> feat/main-page
```

```
# cat

Hello Cat!!

## 목록
1. cat
2. 싫은데 좋아요
```

수동으로 바꾼다

소스트리 가보면, 아까와 달리 컨플릭트 해결된거 볼 수 있고 스테이지 올린 후 커밋한다

커밋 메세지가 자동으로 적혀있음(머지 커밋)

커밋하고 history 가보면 origin master 잘 업데이트 된 거 확인

