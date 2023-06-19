import { useEffect, useContext, useState } from "react";
import Card from "react-bootstrap/Card";

import { GameContext } from "../../App";

export function GameEnd() {
  const gameCtx = useContext(GameContext);
  const cells = gameCtx.cells;

  console.log(gameCtx.gameEnd);

  const { xWin, setXWin } = gameCtx.gameEnd.xWin;
  const { oWin, setOWin } = gameCtx.gameEnd.oWin;
  const { draw, setDraw } = gameCtx.gameEnd.draw;
  const { backgroundColor, setBackgroundColor } =
    gameCtx.gameEnd.backgroundColor;

  useEffect(() => {
    const players = ["X", "O"];

    players.forEach((player) => {
      let won = false;

      if (
        cells[0].value === player &&
        cells[1].value === player &&
        cells[2].value === player
      ) {
        won = true;
      } else if (
        cells[3].value === player &&
        cells[4].value === player &&
        cells[5].value === player
      ) {
        won = true;
      } else if (
        cells[6].value === player &&
        cells[7].value === player &&
        cells[8].value === player
      ) {
        won = true;
      } else if (
        cells[0].value === player &&
        cells[3].value === player &&
        cells[6].value === player
      ) {
        won = true;
      } else if (
        cells[1].value === player &&
        cells[4].value === player &&
        cells[7].value === player
      ) {
        won = true;
      } else if (
        cells[2].value === player &&
        cells[5].value === player &&
        cells[8].value === player
      ) {
        won = true;
      } else if (
        cells[0].value === player &&
        cells[4].value === player &&
        cells[8].value === player
      ) {
        won = true;
      } else if (
        cells[2].value === player &&
        cells[4].value === player &&
        cells[6].value === player
      ) {
        won = true;
      } else if (
        cells[0].value !== "" &&
        cells[1].value !== "" &&
        cells[2].value !== "" &&
        cells[3].value !== "" &&
        cells[4].value !== "" &&
        cells[5].value !== "" &&
        cells[6].value !== "" &&
        cells[7].value !== "" &&
        cells[8].value !== ""
      ) {
        setDraw(true);
      }

      if (backgroundColor === "") {
        if (draw) {
          setDraw(true);
          console.log("draw");
          setBackgroundColor("warning");
        } else if (won) {
          if (player === "X") {
            setXWin(true);
            setBackgroundColor("success");
          } else if (player === "O") {
            setOWin(true);
            setBackgroundColor("danger");
          }
        }
      }
    });
  }, [cells, draw, xWin, oWin]);

  function winGame() {
    if (xWin) {
      setBackgroundColor("success");
    } else if (oWin) {
      setBackgroundColor("danger");
    } else {
      setBackgroundColor("primary");
    }
  }

  return (
    <Card
      bg={backgroundColor}
      style={{
        width: "18rem",
        margin: "auto",
        backgroundColor: "rgb(215, 217, 219)",
        marginTop: "1rem",
      }}
    >
      <Card.Body>
        {xWin ? "X has won" : ""}
        {oWin ? "O has won" : ""}
        {draw ? "Noone won ;_;" : ""}
      </Card.Body>
    </Card>
  );
}
