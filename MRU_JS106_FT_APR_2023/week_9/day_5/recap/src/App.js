import "./App.css";

import Student from "./components/student";

const studentNames = [
  "Abeenesh",
  "Blessing",
  "Dhivyesh",
  "Nilesh",
  "Tushil",
  "Jatin",
];

function App() {
  return (
    <div className="App">
      <h1>Classwork</h1>
      <h2>Make a pet list with</h2>
      <ul>
        <li>an input box for a new pet name</li>
        <li>a button to add the pet</li>
        <li>a button to remove a pet at random</li>
        <li>initial state should contain the pet "Mario" and "Pikachu"</li>
      </ul>
      <Student studentNames={studentNames} />
    </div>
  );
}

export default App;
