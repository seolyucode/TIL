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



#### 저장소 통째로 복제하기 - 포크(fork)

흥한 오픈소스에 숟가락 얹고 싶은 상황, 기능 추가

다만 저장소의 푸시 권한이 없음

오픈소스 기여 위해선 커밋 전에 컬래버레이터 등록을 부탁해야할까?

=> 포크(fork) : 저장소 통쨰로 복제

1. 저장소 통째로 내 계정에 복제
2. 자유롭게 커밋, 푸시
3. 내 저장소의 브랜치와 원본 저장소의 브랜치를 머지해달라고 요청

브랜치 vs 코드

두 가지 모두 코드를 협업하기 위해 분기점을 나누는 방식이지만 특성이 다르므로 내 프로젝트에 맞게 사용

|        | 의의                                   | 편리한 점                                                    | 불편한 점                                              |
| ------ | -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| 브랜치 | 하나의 원본저장소에서 분기를 나눈다    | 하나의 원본저장소에서 코드 커밋 이력을 편하게 볼 수 있다     | 다수의 사용자가 다수의 브랜치를 만들면 관리하기 힘들다 |
| 포크   | 여러 원격저장소를 만들어 분기를 나눈다 | 원본저장소에 영향을 미치지 않으므로 마음껏 코드를 수정할 수 있다 | 원본저장소의 이력을 보려면 따로 주소를 추가해줘야 한다 |



포크 실습

1. GitHub 새로운 계정 만들기
2. 저장소 포크
3. 포크한 저장소 클론
4. 소스트리에서 새 계정 추가 및 디폴트 계정으로 설정
5. 좋아요 기능 만들고 커밋, 푸시
6. GitHub에서 커밋 확인

저장소 포크하면

https://github.com/seolyulee/gitTraining

클론 주소 복사

소스트리 + 버튼 Clone

주소 붙여넣고 경로 설정하고 클론

커밋이력 볼 수 있음

소스트리에서 새로운 계정 추가해야 함

dog 에는 dog 만 push 할 수 있어야 하므로

도구 - 옵션 - 인증 - 추가 - GitHub - HTTPS - Basic - ....

vscode에서 저장소 열기

파일 수정하고 소스트리에서 스테이지 올리고 커밋 푸시



콜라보레이터(push 권한 가짐) 추가

셋팅즈 - Collaborators - 추가



내 코드를 머지해주면 안되겠니 - 풀 리퀘스트(Pull request)

포크한 저장소에서 기능 개발을 마친 후 원본 저장소에 머지해달라고 하고 싶을 때

1. 머지하고 싶은 두 브랜치를 선택
2. 어떤 변경을 했는지 제목과 내용에 쓴다
3. 단일 저장소에 보낼 수도 있고, 이렇게 포크한 저장소에서도 보낼 수 있다

base 가 merge 를 당할 대상 브랜치

compare 새로 만든 브랜치



풀 리퀘스트로 머지 요청 보내기

1. 코드를 함께 작성하는 팀원이 있다면, 최대한 직접 머지하는건 피하고 모든 머지를 풀 리퀘스트를 통해서
2. 동료가 내 풀 리퀘스트(PR)를 보고 코드를 리뷰할 수 있다
3. 동료의 PR에 수정이 필요하면 댓글을 달아 change request를 보낼 수 있다
4. 오픈소스에 PR을 보낼 때는 '기여 안내문서(contribution quideline)'을 반드시 참고해야 한다



TIP: 브랜치 관리하기

1. 보통 `feat/기능이름` 으로 한 사람이 개발하는 기능 브랜치를 만든다.(혹은 `fix/버그이름` `hotfix/급한버그`)
2. 작업이 끝나면 `dev`(혹은 `master`) 브랜치로 PR을 보낸다
3. `dev` 브랜치에서 큼지막한 작업이 모두 머지되면 `release`(혹은 `latest`) 브랜치로 머지시키고 이를 실서버에 배포
4. 직접 커밋은 feat(혹은 fix, hotfix) 브랜치에서만 한다
5. dev나 master, release브랜치에는 직접 커밋하지 말고 머지만 한다



풀 리퀘스트 실습

1. 포크한 저장소에서 원본 저장소로 풀 리퀘스트 보내기
2. 로그인해서 풀 리퀘스트 수락 후 머지



포크한 저장소에서 New pull request

base, compare 설정

Create pull request

제목, 내용 Create pull request



Able to merge 는 base와 compare 브랜치가 충돌 안나는걸 깃헙이 자동 추적해서 알려주는 것



원래 계정 원본 저장소에 Pull requests 온 거 확인

File changed

Review changes

3가지 선택지 있음

change에 바로 댓글 달 수도 있음



Approve 

LGTM : Looks Goot To Me 좋아보인다

깃헙 외국 오픈소스에 컨트리뷰션할 때 많이 씀



밑에 Merge pull request - Confirm merge 머지됨

Insight 에 Contributors 에 추가된거 확인



부계정 메인페이지 가보면 Pinned 된 저장소 고를 수 있음

자랑하고 싶은 오픈소스 

Customize your pins 에서

원본 저장소 노출되게 할 수 있음

