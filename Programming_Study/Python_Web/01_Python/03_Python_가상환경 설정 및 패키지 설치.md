가상 환경 - 가상환경 설정 및 패키지 설치

한 운영체제에 버전 다른거 여러개 설치하면 충돌 일어날 수 있음(포맷하게 될 수도) => 가상환경

| 가상환경A  | 가상환경B         | 가상환경C  |
| ---------- | ----------------- | ---------- |
| 프로젝트 A | 프로젝트 B        | 프로젝트 B |
| Python 3.5 | Python 2.x        | Python 3.6 |
| Django     | Numpy, Tensorflow | PyQT5      |
| Web        | Data Analysis     | GUI APP    |

 별개의 가상환경 => 효율적 프로젝트 관리, 다른 모듈 사용하더라도 여러 프로젝트..



파이썬 가상환경 명령어 기초

* 가상환경 생성
* 가상환경 실행/해제 -> (윈도우: Script, 맥: Bin) 폴더
* 패키치 설치 및 삭제
* 패키지 리스트 출력
* 패키지 검색

cmd

python -m venv python_basic  # 절대경로로 잡아도 되고 하위경로에 있는 python_basic이라는 곳에 가상환경 잡기

cd python_basic  # 들어가서

dir  

cd Scripts

activate.bat  # 가상환경 활성화

deactivate.bat  # 가상환경 활성화 빠져나오기

