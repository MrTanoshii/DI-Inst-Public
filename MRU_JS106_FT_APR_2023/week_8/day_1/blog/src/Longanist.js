import React from "react";
import "./Longanist.css";

// Arrow function component
const Longanist = (props) => {
  return (
    <div className="longanist">
      {props.listOfLonganist.map((longanist) => (
        <ul
          key={longanist.id}
          //   style={{ fontSize: "20px", fontWeight: "300", letterSpacing: "2px" }}
        >
          <li>Name: {longanist.name}</li>
          <li>Services: {longanist.services}</li>
          <li>Price: {longanist.price}</li>
        </ul>
      ))}
    </div>
  );
};

export default Longanist;
