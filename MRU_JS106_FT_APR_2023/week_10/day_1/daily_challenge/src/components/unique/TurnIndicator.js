import { useContext } from "react";

import { GameContext } from "../../App";

export const TurnIndicator = () => {
  const gameCtx = useContext(GameContext);
  const player = gameCtx.player.player;

  return (
    <div>
      <span className="player">{player}</span>'s turn
    </div>
  );
};
