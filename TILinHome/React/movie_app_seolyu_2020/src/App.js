import React from 'react';
// import PropTypes from "prop-types";

// const foodILike = [
//   {
//     id: 1,
//     name: "Kimchi",
//     image:
//     "https://cdn.pixabay.com/photo/2020/01/01/00/15/one-address-based-4732816_1280.jpg",
//     // rating: 5    
//   },
//   {
//     id: 2,
//     name: "Samgyeopsal",
//     image:
//     "https://cdn.pixabay.com/photo/2014/01/24/04/36/roasted-250875_1280.jpg",
//     rating: 4.3
//   }
// ]

// function Food({ name, picture, rating }) {
//   return (
//     <div>
//       <h2>I like {name}</h2>
//       <h4> {rating}/5.0 </h4>
//       <img src={picture} alt={name} />
//     </div>
//   );
// }

// Food.propTypes = {
//   name: PropTypes.string.isRequired,
//   picture: PropTypes.string.isRequired,
//   rating: PropTypes.number
// };

// function App() {
//   // return <div className="App" />
//   return (
//     <div>
//       {foodILike.map(dish => (
//         <Food key={dish.id} name={dish.name} picture={dish.image} rating={dish.rating} />
//       ))}
//     </div>
//   );
// }

class App extends React.Component {
  constructor(props) {
    super(props);
    console.log("hello");
  }
  state = {
    count: 0
  };
  add = () => {
    this.setState(current => ({count: current.count + 1}));
  };
  minus = () => {
    this.setState(current => ({count: current.count - 1}));
  };
  componentDidMount() {
    console.log("component rendered");
  }
  componentDidUpdate() {
    console.log("I just updated");
  }
  componentWillUnmount() {
    console.log("Goodbye, cruel world")
  }
  render() {
    console.log("I'm rendering");
    return (
      <div>
        <h1>The number is: {this.state.count}</h1>
        <button onClick={this.add}>Add</button>
        <button onClick={this.minus}>Minus</button>
      </div>
    );
  }
}

export default App;
