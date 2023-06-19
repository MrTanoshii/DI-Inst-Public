import "./Cell.css";

export const Cell = (props) => {
  return (
    <div
      className="cell"
      onClick={() => {
        if (props.cellState.value === "") {
          props.cellState.fn(props.player.player);
          props.player.setPlayer(props.player.player === "X" ? "O" : "X");
        }
      }}
    >
      {props.cellState.value}
    </div>
  );
};
