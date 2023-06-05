import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    {/* <div> */}
    {/* <script type="text/javascript">console.log("This is being run");</script> */}
    <App />
    {/* </div> */}
  </React.StrictMode>
);

// const element1 = <h3>Hello Jatin</h3>;
// root.render(element1);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
