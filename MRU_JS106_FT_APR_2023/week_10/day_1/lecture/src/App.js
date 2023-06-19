import "./App.css";
import CounterClass from "./CounterClass";
import { CounterFn } from "./CounterFn";
import { SayGreeting } from "./SayGreeting";

// Arrow function component
const App = () => {
  return (
    <>
      {/* <CounterClass />
      <CounterClass />
      <CounterClass /> */}
      {/* <CounterFn /> */}
      <SayGreeting></SayGreeting>
      {/* <Blahblah /> */}
    </>
  );
};

export default App;
