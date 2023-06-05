import React from "react";

// Class component
class Student extends React.Component {
  render() {
    console.info(this.props);
    return (
      <div>
        <h1>Welcome {this.props.studentName}!</h1>
      </div>
    );
  }
}

export default Student;
