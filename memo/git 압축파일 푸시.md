`git config --global user.name "깃커밋에사용될이름"`

`git config --global user.email "깃커밋에사용될이메일"`

`git config --list`



`git init`  // 깃 저장소 생성

`git clone`  // 원격저장소 프로젝트 로컬저장소에



github의 원격저장소와 연결

`git remote add origin https://github.com/username/프로젝트.git`



`git remote -v`



`git push origin master`  // master branch 에 push



// fatal: The current branch master has no upstream branch.

// 브랜치가 원격저장소에 없을 때

`git push -u origin master`  // -u 원격저장소에 master라는 브랜치 생성 후 push



[rejected] master->master(fetch first) 이미 변경된 파일이 원격저장소에 있을 경우

`git pull origin master`  // 원격저장소의 내용을 가져와 로컬저장소의 내용과 자동으로 병합작업.

// fetch 원격저장소의 내용을 확인만 하고 로컬저장소의 내용과 병합작업 수행X

`git push -f -u origin master`  // git commit 기록 날리고 push