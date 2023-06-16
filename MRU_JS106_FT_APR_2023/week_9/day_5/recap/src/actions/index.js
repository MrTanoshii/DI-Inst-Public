export const study = (index) => {
  return {
    type: "PROGRESS",
    payload: { value: 10, studentIndex: index?.studentIndex },
  };
};

export const research = (index) => {
  return {
    type: "PROGRESS",
    payload: { value: 15, studentIndex: index?.studentIndex },
  };
};

export const slack = (index) => {
  return {
    type: "PROCRASTINATE",
    payload: { value: -10, studentIndex: index?.studentIndex },
  };
};

export const ranService = (index) => {
  return {
    type: "PROCRASTINATE",
    payload: { value: -12, studentIndex: index?.studentIndex },
  };
};
