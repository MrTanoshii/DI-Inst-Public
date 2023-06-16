const initialState = [
  {
    firstName: "Albert",
    lastName: "Robert",
    progress: 0,
  },
  {
    firstName: "Bob",
    lastName: "Marley",
    progress: 0,
  },
  {
    firstName: "Madeline",
    lastName: "Rose",
    progress: 0,
  },
  {
    firstName: "Elisa",
    lastName: "Kim",
    progress: 0,
  },
];

export const progressStudies = (state = initialState, action) => {
  let newStudent;
  switch (action.type) {
    case "PROGRESS":
      newStudent = structuredClone(state[action.payload.studentIndex]);
      newStudent.progress += action.payload.value;
      // Clamp the value between 0 and 100 (inclusive)
      newStudent.progress = newStudent.progress < 0 ? 0 : newStudent.progress;
      newStudent.progress =
        newStudent.progress > 100 ? 100 : newStudent.progress;

      return [
        ...state.map((student, index) =>
          index !== action.payload.studentIndex ? student : newStudent
        ),
      ];
    case "PROCRASTINATE":
      newStudent = structuredClone(state[action.payload.studentIndex]);
      newStudent.progress += action.payload.value;
      // Clamp the value between 0 and 100 (inclusive)
      newStudent.progress = newStudent.progress < 0 ? 0 : newStudent.progress;
      newStudent.progress =
        newStudent.progress > 100 ? 100 : newStudent.progress;

      return [
        ...state.map((student, index) =>
          index !== action.payload.studentIndex ? student : newStudent
        ),
      ];
    default:
      console.log("Default");
      return state;
  }
};
