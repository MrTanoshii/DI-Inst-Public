import { useState } from "react";

export const Blessing = () => {
  const [advice, setAdvice] = useState("test");

  async function getAdvice() {
    let result = await fetch("https://api.adviceslip.com/advice");
    // console.log(res);
    console.log(advice);
    let data = await result.json();
    console.log(data);
    setAdvice(data.slip.advice);
  }

  return (
    <div>
      <h1>{advice}</h1>
      <button onClick={getAdvice}>Get Advice</button>
    </div>
  );
};
