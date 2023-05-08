const tasks = [];

const addXmark = (el) => {
  // Add an xmark to the parent element
  let xmarkEl = document.createElement("div");
  xmarkEl.classList.add("xmark");
  el.appendChild(xmarkEl);

  // Add an svg to xmark
  var svgEl = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svgEl.setAttributeNS(null, "viewBox", "0 0 384 512");
  svgEl.innerHTML =
    "<!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->";
  xmarkEl.appendChild(svgEl);

  // Add a path to svg
  let pathEl = document.createElementNS("http://www.w3.org/2000/svg", "path");
  pathEl.setAttributeNS(
    null,
    "d",
    "M376.6 84.5c11.3-13.6 9.5-33.8-4.1-45.1s-33.8-9.5-45.1 4.1L192 206 56.6 43.5C45.3 29.9 25.1 28.1 11.5 39.4S-3.9 70.9 7.4 84.5L150.3 256 7.4 427.5c-11.3 13.6-9.5 33.8 4.1 45.1s33.8 9.5 45.1-4.1L192 306 327.4 468.5c11.3 13.6 31.5 15.4 45.1 4.1s15.4-31.5 4.1-45.1L233.7 256 376.6 84.5z"
  );
  svgEl.appendChild(pathEl);
};

const addText = (el, text) => {
  // Add a <p></p> to the parent element
  let pEl = document.createElement("p");
  el.appendChild(pEl);
  pEl.innerText = text;
};

const addCheckBox = (el) => {
  // Add a <input type="checkbox"> to the parent
  let checkBoxEl = document.createElement("input");
  checkBoxEl.setAttribute("type", "checkbox");
  el.appendChild(checkBoxEl);
};

const addTask = () => {
  let taskListEl = document.getElementsByClassName("listTasks");

  let inputValue = document.forms[0].elements[0].value;

  if (!inputValue || inputValue === "") {
    return;
  }

  tasks.push(inputValue);

  // Add an taskEl to taskListEl
  let taskEl = document.createElement("div");
  taskEl.classList.add("task");
  taskListEl[0].appendChild(taskEl);

  taskEl.addEventListener("change", crossOut);

  addXmark(taskEl);
  addCheckBox(taskEl);
  addText(taskEl, inputValue);
};

window.onload = () => {
  console.log("Test");
  document.getElementById("add_button").addEventListener("click", addTask);
};

const crossOut = (el) => {
  if (el.target.checked) {
    el.target.nextElementSibling.classList.add("cross_out");
  } else {
    el.target.nextElementSibling.classList.remove("cross_out");
  }
};
