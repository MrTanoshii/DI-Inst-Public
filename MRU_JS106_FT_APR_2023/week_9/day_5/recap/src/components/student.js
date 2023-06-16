import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { addStudent } from "../redux/student_redux";

// Display student name as a list item
// where the list of student names is a prop called `studentNames`

function Student(props) {
  const studentNamesRedux = useSelector((state) => state.student.studentNames);
  const globalState = useSelector((state) => state);
  const dispatch = useDispatch();

  console.log(globalState);

  return (
    <>
      <h1>Props student list</h1>
      <ul>
        {props.studentNames.map(
          (nimporteEneNomLaDan, nimporteBlahBlahBlahIndex) => (
            <li key={nimporteBlahBlahBlahIndex}>{nimporteEneNomLaDan}</li>
          )
        )}
      </ul>
      <h1>Redux student list</h1>
      <ul>
        {studentNamesRedux.map((studentName, index) => (
          <li key={index}>{studentName}</li>
        ))}
      </ul>
      <input id="student_name_input" />
      <button
        onClick={() =>
          dispatch(
            addStudent({
              studentName: document.querySelector("#student_name_input").value,
            })
          )
        }
      >
        Add Student
      </button>
    </>
  );
}

export default Student;
