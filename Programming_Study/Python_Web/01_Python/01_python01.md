### 파이썬 기초 & 크롤링 기초/심화

Python

* Easy to learn
* 방대한 분야
* 높은 생산성

Crawling

* 기초 문법 활용
* 타겟 웹 정보 다양한 파일 형식으로 저장

Scrapy

* A Fast and Powerful Scraping and Web Crawling Framework



### 개발 환경 설정

파이썬 언어 장점

* 문법이 간결
* 다양한 운영체제 지원
* GUI Application 개발(PyQT)
* 방대한 라이브러리 지원
* 범용 언어(네트워크, 웹, 데이터분석, 기계학습 등)

공부 방법 및 수업 진행 계획

* 반드시 직접 코딩 실습
* 너무 어려울 경우 우선은 패스 -> 숙련도 쌓이면 해결
* 꼭 복습 코딩 및 응용 실습
* 천천히 그러나 확실하게 학습



* 파이썬 3.x 설치
* Visual Studio Code 설치
* Visual Studio Code 환결 설정
* 테스트 코드 작성 및 실행



Chrome - python download - 버전에 맞게 executable installer

vscode download - User Installer

경로에 한글이 들어가지 않게 계정명 영어로(or c드라이브/d드라이브 하위에 설치) 해야 에러 안남

Add Python to Path 체크

vscode도 계정(영어) 아래에 설치

Path에 추가, 바탕화면에 추가 체크



window - cmd 명령 프롬프트 열고

python 쳐보기

나가는건 Ctrl + z 또는

`exit()` 



`code` 쳐봤을 때 vscode 실행되는지 확인



### vscode

view - Extensions 

python 관련 설정하기

* Python 설치 -> reload
* File - Open Folder - (C드라이브에 새폴더 만들고) 폴더 선택 
* view - Command Palette - python select interpreter - 설치한 파이썬 선택

New file - ***.py

```python
# Section01
# 파이썬 소개 및 작업 환경 설정

# 기본 출력
print('Hello Python!')  # task runner
```

Ctrl + s

File - Preferences - Keyboard Shortcuts 단축키 나옴

Debug - Start without Debugging



View - Command Palette - Tasks: Configure Task - create taskes.json... - Others

폴더 하위에 tasks.json 이란 파일이 생성되고 내용이 있을텐데 그걸 다 지우고

복붙하기

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Project Label",
            "type": "shell",
            "command": "python",
            "args": [
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "options": {
                "env": {
                    "PYTHONIOENCODING": "UTF-8"
                }
            },
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

Ctrl + Shift + b 누르면 실행됨



익스텐션에 korean 설치

view - Command Palette - configure display language 선택 -> locale.json 생성됨

en을 ko로 바꾸고 재실행하면 한글로 바뀜

Ctrl + space -> 언어들 나옴





