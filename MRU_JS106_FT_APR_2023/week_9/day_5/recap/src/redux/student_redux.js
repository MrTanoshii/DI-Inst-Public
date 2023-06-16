import { createSlice } from "@reduxjs/toolkit";

export const StudentSlice = createSlice({
  name: "studentSlice",
  initialState: {
    studentNames: [
      "Abraham",
      "Victor",
      "Ambareen",
      "Vincent",
      "Damien",
      "Sebastien",
    ],
    whateverIWant: 92392359828,
  },
  reducers: {
    addStudent: (state, action) => {
      state.studentNames.push(action.payload.studentName);
    },
    // incrementByAmount: (state, action) => {
    //   state.value += action.payload;
    // },
  },
});

// Action creators are generated for each case reducer function
export const { addStudent } = StudentSlice.actions;

export default StudentSlice.reducer;
