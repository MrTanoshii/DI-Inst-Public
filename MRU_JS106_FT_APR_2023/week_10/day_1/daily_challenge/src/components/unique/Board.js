import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useContext } from "react";

import { Cell } from "../shared/Cell";
import { GameContext } from "../../App";
import "./Board.css";

export const Board = () => {
  const gameCtx = useContext(GameContext);
  const cells = gameCtx.cells;
  const player = gameCtx.player;

  return (
    <Container style={{ border: "1px solid black" }}>
      <Row>
        <Col>
          <Cell cellState={cells[0]} player={player} />
        </Col>
        <Col
          style={{
            borderColor: "black",
            borderStyle: "solid",
            borderWidth: "0px 1px 0px 1px",
          }}
        >
          <Cell cellState={cells[1]} player={player} />
        </Col>
        <Col>
          <Cell cellState={cells[2]} player={player} />
        </Col>
      </Row>
      <Row
        style={{
          borderColor: "black",
          borderStyle: "solid",
          borderWidth: "1px 0px 1px 0px",
        }}
      >
        <Col>
          <Cell cellState={cells[3]} player={player} />
        </Col>
        <Col
          style={{
            borderColor: "black",
            borderStyle: "solid",
            borderWidth: "0px 1px 0px 1px",
          }}
        >
          <Cell cellState={cells[4]} player={player} />
        </Col>
        <Col>
          <Cell cellState={cells[5]} player={player} />
        </Col>
      </Row>
      <Row>
        <Col>
          <Cell cellState={cells[6]} player={player} />
        </Col>
        <Col
          style={{
            borderColor: "black",
            borderStyle: "solid",
            borderWidth: "0px 1px 0px 1px",
          }}
        >
          <Cell cellState={cells[7]} player={player} />
        </Col>
        <Col>
          <Cell cellState={cells[8]} player={player} />
        </Col>
      </Row>
    </Container>
  );
};
