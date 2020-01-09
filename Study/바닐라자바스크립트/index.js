// alert('Im Working. Im JS. Im Beautiful. Im worth it')

const title = document.getElementById("title");

// console.log(title);
console.dir(title);
console.dir(document);

// DOM
// Document Object Module
// 자바스크립트는 html에 있는 모든 요소를 가지고 와서 DOM 객체로 바꿈
// 객체는 많은 키를 가지고 있다

title.innerHTML = "Hi! From JS";
title.style.color = 'red';

document.title = 'I own you now'

// 실제 바뀐 HTML 확인 가능