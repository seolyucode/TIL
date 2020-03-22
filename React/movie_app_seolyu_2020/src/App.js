import React from 'react';

function Food({ name, picture }) {
  return <div>
    <h2>I like {name}</h2>
    <img src={picture} />
  </div>;
}

const foodILike = [
  {
    name: "Kimchi",
    image:
    "https://cdn.pixabay.com/photo/2020/01/01/00/15/one-address-based-4732816_1280.jpg"    
  },
  {
    name: "Samgyeopsal",
    image:
    "https://cdn.pixabay.com/photo/2014/01/24/04/36/roasted-250875_1280.jpg"
  }
]

function App() {
  // return <div className="App" />
  return (
    <div>
      {foodILike.map(dish => (
        <Food name={dish.name} picture={dish.image}/>
      ))}
    </div>
  );
}

export default App;
