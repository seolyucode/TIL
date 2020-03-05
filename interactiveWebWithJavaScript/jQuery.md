# jQuery를 설치하는 방법



1. ### 링크 사용

   작성한 `...` 태그 바로 윗 줄에 [jQuery CDN](https://code.jquery.com/)의 코드를 붙여 넣어주는 방법

   ```html
   <script
     src="https://code.jquery.com/jquery-3.2.1.min.js"
     integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
     crossorigin="anonymous"></script>
   <script>
     // 우리 자바스크립트 코드...
   </script>
   ```

   인터넷에 있는 원격 jQuery 코드를 내 프로젝트로 가져옴

   

2. ### 직접 jQuery 코드를 다운받아서 쓰는 방법

   [jQuery 사이트](https://jquery.com/)에 들어가서 jQuery 코드를 직접 다운로드(jquery-3.2.1.min.js) 받아서 프로젝트 안에 두고(js 폴더 안에) <script> 태그에 jquery.js 파일에 대한 경로를 써준다

   ```html
   <script src="js/jquery-3.2.1.min.js"></script>
   <script>
     // 우리 자바스크립트 코드...
   </script>
   ```

   

