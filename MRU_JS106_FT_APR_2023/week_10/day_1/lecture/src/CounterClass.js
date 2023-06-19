import React from "react";

class CounterClass extends React.Component {
  // Keep track of a count which is an int
  // Display the count in a Header 1
  // Button decrement
  // Button increment

  constructor() {
    super();
    this.state = { count: 0, userName: "DNTKJBA" };

    // this.handleClick = this.handleClick.bind(this);
  }

  handleIncrement = () => {
    this.setState({ ...this.state, count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        <button
          onClick={() => {
            // Don't mutate directly, React can't keep track of this!
            // this.state.count -= 1;
            console.log("Decrement Handler", this.state);
            this.setState({ ...this.state, count: this.state.count - 1 });
            console.log("Decrement Handler", this.state);
          }}
        >
          Decrement
        </button>
        <h1>{this.state.count}</h1>
        <button onClick={this.handleIncrement}>Increment</button>
      </div>
    );
  }
}

export default CounterClass;
