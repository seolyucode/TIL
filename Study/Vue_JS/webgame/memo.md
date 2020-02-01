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