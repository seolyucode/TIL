Webpack을 쓰려면 nodejs.org 가서 nodejs LTS로 받기

`node -v`

`npm -v`  // 노드 설치하면 설치됨. 남이 만들어놓은 자바스크립트 코드 가져다 쓰기



`npm init`

package.json 파일 생김 <- 내가 쓰는 남의 소스코드(패키지)들이 여기에 정리됨

각각의 소스코드마다 버전들이 있어서 버전관리 위해

`npm install vue`  // vue 설치  `npm i vue`

`npm i webpack webpack-cli -D`  // 웹팩이랑 웹팩CLI 패키지를 설치하는데 개발할 때만 이 웹팩, 웹팩CLI를 쓰겠다는 뜻

-D 말고 --save-dev 입력해도 됨



vue 는 개발, 배포 둘 다 쓰는데

webpack, webpack-cli 는 배포를 위한 보조도구(devDependencies에)



webpack.config.js <- 웹팩에 대한 설정 적는다

```
module.exports = {
    entry: {
        app: './main.js',
    },
    module: {
        rules: [{
            
        }],
    },
    plugins: [

    ],
    output: {
        filename: '[name].js',
        path: './dist',
    },
};
```

웹팩 <- script 많아져서 하나로 합치려고 

스크립트에서 가장 대표가 되는 파일이 entry에

app <- 하나로 합쳐질 파일의 이름

dist 폴더 안에 app.js 가 최종결과물로 



뷰 컴포넌트 Vue 파일로 분리되어서 분리



package.json

```
  "scripts": {
    "build": "webpack"
  },
```



### 처음부터 .gitignore 파일 만들 경우

프로젝트 디렉터리에서

`vim .gitignore`

a : 다음 글자

i : 현재 커서

o : 윗줄

Git에서 무시하려는 정보 기입

ESC : 입력모드 나가기

:wq 저장 후 나가기



#### 사용 도중에 .gitignore 파일 만들 경우

`git rm -r --cached .`

`git add .`

`git commit -m 'git ignore add'`

`git push`

https://github.com/github/gitignore

https://www.gitignore.io/



webpack 은 자바스크립트만 합쳐줘서

rules 수정

```
const path = require('path');

module.exports = {
    entry: {
        app: path.join(__dirname, 'main.js'),
    },
    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader',
        }],
    },
    plugins: [

    ],
    output: {
        filename: '[name].js',
        path: path.join(__dirname, 'dist'),
    },
};
```

`npm i vue-loader -D`

(ctrl + c 로 취소 가능)

에러

```
const VueloaderPlugin = require('vue-loader/lib/plugin');
const path = require('path');

module.exports = {
    entry: {
        app: path.join(__dirname, 'main.js'),
    },
    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader',
        }],
    },
    plugins: [
        new VueloaderPlugin(),
    ],
    output: {
        filename: '[name].js',
        path: path.join(__dirname, 'dist'),
    },
};
```

`npm i vue-template-compiler -D`



vue 랑 vue-template-compiler 버전 같아야함

`npm i vue@2.7.0` 이런 식으로 특정 버전 깔기

@안쓰면 최신버전



`npm run build`

app.js 



```
const VueloaderPlugin = require('vue-loader/lib/plugin');
const path = require('path');

module.exports = {
    mode: 'development',
    devtool: 'eval',
    resolve: {
        extensions: ['.js', '.vue'],
    },
    entry: {
        app: path.join(__dirname, 'main.js'),
    },
    module: {
        rules: [{
            test: /\.vue$/,
            use: 'vue-loader',
        }],
    },
    plugins: [
        new VueloaderPlugin(),
    ],
    output: {
        filename: '[name].js',
        path: path.join(__dirname, 'dist'),
    },
};
```

```
import Vue from 'vue';
import NumberBaseball from './NumberBaseball';

new Vue(NumberBaseball).$mount('#root');
```

`npm run build`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="root"></div>
    <script src="./dist/app.js"></script>
</body>
</html>
```

