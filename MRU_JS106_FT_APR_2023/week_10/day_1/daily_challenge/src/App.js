import { createContext, useState } from "react";
import Button from "react-bootstrap/Button";

import { TurnIndicator } from "./components/unique/TurnIndicator";
import { GameEnd } from "./components/unique/GameEnd";
import { Board } from "./components/unique/Board";

import "./App.css";

export const GameContext = createContext(null);

function App() {
  const [cell1, setCell1] = useState("");
  const [cell2, setCell2] = useState("");
  const [cell3, setCell3] = useState("");
  const [cell4, setCell4] = useState("");
  const [cell5, setCell5] = useState("");
  const [cell6, setCell6] = useState("");
  const [cell7, setCell7] = useState("");
  const [cell8, setCell8] = useState("");
  const [cell9, setCell9] = useState("");

  const [player, setPlayer] = useState("X");

  const [gameMode, setGameMode] = useState("1P");

  const [xWin, setXWin] = useState(false);
  const [oWin, setOWin] = useState(false);
  const [draw, setDraw] = useState(false);
  const [backgroundColor, setBackgroundColor] = useState("");

  const resetGame = () => {
    setCell1("");
    setCell2("");
    setCell3("");
    setCell4("");
    setCell5("");
    setCell6("");
    setCell7("");
    setCell8("");
    setCell9("");

    setPlayer("X");

    setXWin(false);
    setOWin(false);
    setDraw(false);
    setBackgroundColor("");
  };

  return (
    <GameContext.Provider
      value={{
        cells: [
          { value: cell1, fn: setCell1 },
          { value: cell2, fn: setCell2 },
          { value: cell3, fn: setCell3 },
          { value: cell4, fn: setCell4 },
          { value: cell5, fn: setCell5 },
          { value: cell6, fn: setCell6 },
          { value: cell7, fn: setCell7 },
          { value: cell8, fn: setCell8 },
          { value: cell9, fn: setCell9 },
        ],
        player: { player: player, setPlayer: setPlayer },
        gameMode: { gameMode: gameMode, setGameMode: setGameMode },
        gameEnd: {
          xWin: { xWin: xWin, setXWin: setXWin },
          oWin: { oWin: oWin, setOWin: setOWin },
          draw: { draw: draw, setDraw: setDraw },
          backgroundColor: {
            backgroundColor: backgroundColor,
            setBackgroundColor: setBackgroundColor,
          },
        },
      }}
    >
      <div className="App">
        <h1>REACT TIC TAC TOE</h1>
        <Button
          variant={gameMode === "1P" ? "primary" : "outline-primary"}
          onClick={() => {
            setGameMode("1P");
          }}
        >
          [NOT WORKING]Versus AI
        </Button>{" "}
        <Button
          variant={gameMode === "2P" ? "primary" : "outline-primary"}
          onClick={() => {
            setGameMode("2P");
          }}
        >
          2 Players
        </Button>{" "}
        <Button variant="outline-danger" onClick={resetGame}>
          Reset Board
        </Button>
        <TurnIndicator />
        <Board />
        <GameEnd />
      </div>
    </GameContext.Provider>
  );
}

export default App;
