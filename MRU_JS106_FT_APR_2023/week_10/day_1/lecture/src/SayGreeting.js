import { useRef, useState } from "react";

export const SayGreeting = () => {
  const [userName, SetUserName] = useState("Guest");
  const inputValue = useRef();

  return (
    <>
      <h1>Hello {userName}</h1>
      <input
        type="text"
        // id="skghkfjdg"
        ref={inputValue}
        onChange={() => {
          //   SetUserName(document.querySelector("#skghkfjdg").value);
          SetUserName(inputValue.current.value);
        }}
      ></input>
    </>
  );
};
