import "./App.css";

import { useSelector } from "react-redux";

import Student from "./components/student";
import { StudentStudy } from "./components/studentstudy";

const studentNames = [
  "Abeenesh",
  "Blessing",
  "Dhivyesh",
  "Nilesh",
  "Tushil",
  "Jatin",
];

function App() {
  const studentState = useSelector((state) => state.studentProgress);

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

      <div className="grid-container advanced-react-redux">
        {studentState.map((student, index) => {
          console.info(student);
          return (
            <StudentStudy student={student} key={index} studentIndex={index} />
          );
        })}
      </div>
    </div>
  );
}

export default App;
