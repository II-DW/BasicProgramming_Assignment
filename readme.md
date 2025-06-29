# 나만의 감정일기 만들기 (feat. 푸앙이)


<div align="center">
<img src="https://img.shields.io/badge/Python-white?style=flat&logo=Python&logoColor=blue"/> 
</div>
<hr/>
<br>

## 프로그램 실행방법

### 초기 세팅
#### 1. 모든 파일을 불러온 후, 가장 상위 경로에 .env에 OPENAI_API_KEY = "<YOUR KEY>" 형식으로 저장
#### 2. pip install -r requirements.txt 실행
#### 3. app.py 실행

### 이후 cmd 창에 1 또는 2 입력

### 1 입력시
#### 1. YYYYMMDD 형식으로 날짜를 입력
#### 2. 해당 일의 일기를 입력

### 2 입력시
#### 1. UI 창이 뜨는지 확인
#### 2. 상단의 연, 월 변경해서 확인

### cf) 웹사이트 확인시 (웹사이트에서는 github에 commit된 data.json을 기반으로 합니다.)
#### https://ii-dw.me 접속 및 상단 calander 메뉴를 통해 확인

## 실행 목적 1: 감정 일기 작성

### 프로그램 처리 과정

##### 1. YYYYMMDD 형식으로 날짜를 입력받음.
##### 2. 해당 일의 일기를 입력받고, LLM에게 보내서, 오늘의 감정이 어떤지 분류함.
##### 3. data.json 파일에 이를 저장


### 분류 감정 목록
| 감정       | 푸앙이 |
|------------|------------------|
| 기쁨 | ![Image](./static/기쁨.gif)             |
| 두려움 | ![Image](./static/두려움.gif)             |
| 슬픔 | ![Image](./static/슬픔.gif)             |
| 지침 | ![Image](./static/지침.gif)              |
| 짜증 | ![Image](./static/짜증.gif)             |
| 혐오 | ![Image](./static/혐오.gif)            |

## 실행 목적 2: 감정 캘린더 확인


### 프로그램 처리 과정

##### 1. UI 창을 열고, 날짜에 맞는 감정을 추출해, 이에 맞는 gif를 등록함.
##### 2. 만약 사용자가 캘린더에서 연, 월을 바꾸는 이벤트가 발생하면 gif를 새로 등록함.

### 사용 예시
![Image](./static/example.gif)

# 오류 수정
##### 직전 달의 마지막 날이 토요일인 달에는, 달력이 한 줄 밀리는 현상 발생.
##### 해당 달의 날짜에 7일을 더하는 방식으로 수정함.

# 웹사이트 추가
##### 달력을 생성 후, gh-pages로 배포
##### https://ii-dw.me/calendar



