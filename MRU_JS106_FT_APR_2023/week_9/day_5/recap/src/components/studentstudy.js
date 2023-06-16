import { useDispatch } from "react-redux";

import { study, slack, research, ranService } from "../actions";

export const StudentStudy = (props) => {
  const dispatch = useDispatch();

  return (
    <>
      <div className="grid-item">
        {props.student.firstName} {props.student.lastName}
      </div>
      <div className="grid-item">{props.student.progress} / 100</div>
      <div className="grid-item">
        <button
          onClick={() => {
            dispatch(study({ studentIndex: props.studentIndex }));
          }}
        >
          Study
        </button>
        <button
          onClick={() => {
            dispatch(research({ studentIndex: props.studentIndex }));
          }}
        >
          Research
        </button>
        <button
          onClick={() => {
            dispatch(slack({ studentIndex: props.studentIndex }));
          }}
        >
          Slack
        </button>
        <button
          onClick={() => {
            dispatch(ranService({ studentIndex: props.studentIndex }));
          }}
        >
          Ran Service
        </button>
      </div>
    </>
  );
};
