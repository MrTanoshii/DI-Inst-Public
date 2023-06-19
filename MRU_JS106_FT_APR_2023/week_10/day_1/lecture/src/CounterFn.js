import { useEffect, useState } from "react";

export const CounterFn = () => {
  const [count, setCount] = useState(0);
  const [date, setDate] = useState("19/06/2023");
  const [id] = useState("34m5h34kn5343");

  const incrementCount = () => {
    setCount(count + 1);
  };

  // Replaces DidComponentMount()
  useEffect(() => {
    setCount(count + 10);
  }, []);

  // Replaces DidComponentUpdate()
  useEffect(() => {
    console.log("New hook", count, date, id);
    /// Replaces WillComponentUnMount()
    return () => {
      console.warn("This hook is being returned");
    };
  }, [count, date]);

  return (
    <div>
      <button
        onClick={() => {
          setCount(count - 1);
        }}
      >
        {/* <button
        onClick={() => {
          setDate("sgkjhdfhgkdf");
        }}
      > */}
        Decrement
      </button>
      <h1>{count}</h1>
      <button onClick={incrementCount}>Increment</button>
    </div>
  );
};

export const Blahblah = () => {
  console.log("BLAH");
};
