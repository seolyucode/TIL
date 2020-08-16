### 현대 웹 서비스 개발 절차

요구사항 -> 서비스 기획 -> UI, UX 상세 설계 -> GUI 디자인 -> 퍼블리싱 -> 백엔드 API 개발 -> 프런트엔드 -> QA



### 프런트엔드 개발자의 역할

* 화면단 코드 작성
* 기획, 디자인, 퍼블리싱, 백엔드 개발자와 소통

---

Swagger.io

https://github.com/joshua1988/vue-til

---

NVM(Node Version Manager)

https://github.com/nvm-sh/nvm

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash`

`vi ~/.bashrc`

```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

insert 하고 :wq

그냥 나올 땐 :q 잘못썼을 땐 :q!

커멘드낫파운드

---

https://vueserver.run.goorm.io/api/docs/

---

mongodb cloud

https://www.mongodb.com/cloud

---

vue cli

`npm i -g @vue/cli`

`vue --version`

`vue create vue-til`

---

eslint 에러 화면 덮지 않게

vue.config.js

```javascript
module.exports = {
    devServer: {
        overlay: false
    }
};
```

---

https://eslint.org/

설정 파일 변경되면 서버 재실행

---

prettier.io

.prettierrc

package.json 보면 설정했었던대로

뷰CLI

- ESLint

- Prettier

충돌 나니까 ESLint 안에 Prettier 해야함

```js
  rules: {
    // "no-console": "error",  // 콘솔 있으면 에러
    "no-console": "off",
    // "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    // "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off"
    "prettier": {
      // 프리티어로 정리하면서 ESlint 룰 적용
    }
  },
```

---

```js
  rules: {
    // "no-console": "error",  // 콘솔 있으면 에러
    "no-console": "off",
    // "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    // "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off"
    "prettier/prettier": ['error', {
      printWidth: 80
    }]
  },
```

https://joshua1988.github.io/web-development/vuejs/boost-productivity/

---

설정에서 ESLint

Eslint: Validate - settings.json 편집

```json
 "eslint.validate": [
    {
      "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
      },
      "eslint.workingDirectories": [
        {"mode": "auto"}
      ],
    }
  ]
```

설정 format on save 해제

 

.eslintrc.js에

 extends: ["plugin:vue/essential", "@vue/prettier"],

---

파일의 절대 경로

VSCode에서 제공하는 파일 이용해서

Vue-til 폴더 코드로 열고

jsconfig.json 파일 생성

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "~/*": [
        "./*"
      ],
      "@/*": [
        "./src/*"
      ],
    }
  },
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

---

https://kr.vuejs.org/v2/style-guide/index.html

---

https://github.com/joshua1988/vue-til/tree/complete 클론

git checkout 1_setup`

`npm i`

---

[화면 구성]

로그인 

회원가입

메인

추가 / 수정



`npm i vue-router`

---

mode: 'history',

https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations

---

`npm i axios`

---

빌드 명령어 입력시(npm run build) -> production 모드

---

javascript email validate

https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript

```javascript
function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
```

---

Vue Router - Programmatic Navigation

---

`npm i vuex`

dependencies: 애플리케이션 로직과 관련된 라이브러리 목록

---

https://github.com/axios/axios#interceptors

---

// axios.post('https://vue-server.run.goorm.io/signup')

instance.interceptors.request.use();

---

https://ionicons.com/usage/

---

### 중간 리뷰

1. 개발환경 설정
   * 개발 툴 및 필요 프로그램 설치
   * API 서버 프로젝트 클론
2. Vue CLI 프로젝트 생성
   * Prettier
   * ESLint
   * jsconfig
3. 뷰 라우터 및 컴포넌트 설계
   * `<router-link>`
   * `<router-view>`
   * `mode: history`와 서버 배포시 주의 사항
   * 코드 스플리팅 `component: () => import('경로')`
4. 회원 가입 페이지 개발
   * 사용자 폼 처리
   * async & await
   * axios
   * swagger API 문서 보는 방법
5. 실무 환경 구성
   * `axios.create()`
   * env 파일 설정 방법
   * Vue CLI 버전 3 이상에서의 env 파일 규칙
6. 로그인 페이지 개발
   * 사용자 폼 처리 기능 구현
   * async & await 에러 처리 방법
   * 사용자 폼 유효성 검사
7. 로그인 상태 관리
   * 뷰엑스를 이용한 사용자 아이디 관리
   * `this.$router.push('/main')`
8. API 인증 처리를 위한 토큰 관리
   * JSON Web Token
   * `Authorization` 토큰 값으로 API 인증을 받는 방법
   * `axios.interceptors`
9. 학습 노트 데이터 조회
   * 학습 노트 목록 표시 기능 구현
   * 목록 아이템 컴포넌트화
   * 스피너를 이용한 데이터 로딩 상태 표시
10. 브라우저 저장소를 이용한 인증 값 관리
    * 쿠키를 이용한 로그인 인증 값 저장
    * actions를 이용한 컴포넌트 로직 정리
11. 학습 노트 데이터 생성
    * 학습 노트 생성 기능 구현
    * 학습 노트 본문 길이 유효성 검사

---

앞으로

* 데이터 성격 별로 API 함수 모듈화
* 학습 노트 삭제 기능
* 날짜 형식 포맷팅 `filter`
* 학습 노트 데이터 수정
* 라우터 심화
* 프런트엔드 테스팅

---

https://github.com/joshua1988/vue-til/blob/complete/src/components/common/ToastPopup.vue

---

