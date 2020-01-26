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