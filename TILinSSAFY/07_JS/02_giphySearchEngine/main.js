// 1. input 태그 안의 값(value)을 잡는다.
// const input = document.querySelector('#js-userinput').value;  // .은 클래스 #은 아이디

// 2-1. button 에 'click' 이 일어났을 때, input 에 ENTER키를 쳤을 때 1에서 잡은 값을 요청으로 보낸다.
// [무엇].addEventListener([언제], [어떻게: function])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const inputCount = document.querySelector('#js-image-count').value;
const resultArea = document.querySelector('#js-result-area');

button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    searchAndPush(inputValue);
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value;
        searchAndPush(inputValue);
        // inputValue 로 Giphy API 에 요청 보내서 받기.
    }
});

// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
const searchAndPush = (keyword) => {
    const imageCount = 10;
    const imageCount = document.querySelector('#js-image-count').value;
    const API_KEY = 'tmt5H1BKj7qMvxtTaJh791Yzu9mkEFw2';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${imageCount}&offset=10&rating=G&lang=ko`;
    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 세팅
    AJAX.send();  // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response; 
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;

        inputArea.value = null;
        resultArea.innerHTML = null;
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
        // resultArea.innerHTML += giphyData.data[0].images.downsized.url;
    });
    // console.log('끝');

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);

        // resultArea.innerHTML += `<img src="${imageUrl}" class="container-image">`;
    }
};

// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
// const pushToDOM = (data) => {
//     // 2-2. 1에서 잡은 값을 요청으로 보낸다.
//     // 요청 => 응답을 받아서.
    
//     // 화면에 보여준다
//     resultArea.innerHTML += data; 
// };

// const sendAjaxReq = () => {
    
// }