### git 에서 원격저장소의 branch 가져오기



`git remote update`  원격의 브랜치에 접근하기 위해 git remote 갱신



`git branch`  로컬저장소의 브랜치 목록

`git branch -r`  원격저장소의 브랜치 리스트

`git branch -a`  모든 브랜치의 리스트



`git checkout -t 원격저장소이름/원격저장소의브랜치`  원격 저장소의 브랜치 가져오기

`-t` 옵션과 `원격저장소의브랜치` 입력하면 로컬에 동일한 이름의 브랜치 생성하면서 해당 브랜치로 checkout 함

`git checkout -b [생성할 브랜치 이름] [원격 저장소의 브랜치 이름]`  브랜치 이름 변경해서 가져오기

`git checkout [원격저장소의브랜치이름]`  아무 옵션없이 원격 저장소의 branch를 checkout 하면 `detached HEAD` 상태여서 변경사항을 commit, push 할 수 없고 다른 branch 로 checkout 하면 사라짐



원격 저장소의 특정 branch 를 로컬 저장소의 새로운 branch 로 가져오기

`git checkout -b [새로운 로컬 branch 이름] [원격 저장소 이름]/[원격 branch 이름]`

`git checkout [새로운 로컬 branch 이름]`

 `git pull [원격저장소이름] [원격저장소의브랜치이름]`



새로운 로컬 브랜치를 저장소 remote branch 에도 생성하고 싶을 때는

git push [원격저장소이름] [새로운로컬branch이름]

브랜치 연동

git branch --set-upstream-to [원격저장소이름]/[새로운로컬branch이름]



브랜치 삭제하기

merge 작업이 끝난 로컬의 브랜치를 삭제하려면

다른 브랜치로 checkout한 후, 삭제한다

`git checkout [다른브랜치]`

`git branch --delete [삭제할브랜치]`

작업된 사항이나 commit 이력이 남아있는 경우 삭제가 안될 때는 강제로 삭제

`git branch -D [삭제할브랜치]`

`-D` 옵션을 통해 로컬 브랜치를 강제로 삭제할 수 있다

이 경우 로컬 브랜치는 삭제되지만 remote 브랜치는 아직 삭제가 안되었을 수도 있다

remote branch 를 삭제하려면

`git push [원격저장소이름] :[삭제한브랜치]`