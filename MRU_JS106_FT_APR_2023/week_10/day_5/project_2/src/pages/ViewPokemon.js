import { Outlet, useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import Axios from "axios";

export function ViewPokemon() {
  const [pokemon, setPokemon] = useState("");
  const [pokemonImg, setPokemonImg] = useState("");
  const [pokemonWeight, setPokemonWeight] = useState(-1);
  const params = useParams();

  // setPokemonWeight().response.data.pokemonWeight;

  const getPokemon = () => {
    const pokemonName = params.pokemonName;
    const processedPokemonName =
      pokemonName[0].toUpperCase() + pokemonName.substring(1);

    setPokemon(processedPokemonName);

    Axios.get(`http://localhost:3000/pokemon/${pokemonName}`, {
      crossDomain: true,
    }).then((response) => {
      setPokemonImg(response.data.icon);
      setPokemonWeight(response.data.weight);
    });
  };

  useEffect(() => {
    getPokemon();
  }, []);

  return (
    <>
      <h1>Pokemon Page</h1>
      <div>
        <h2>{pokemon}</h2>
        <ul>
          <li>
            <img src={`/` + pokemonImg} alt="Pokemon" />
          </li>
          <li>Weight: {pokemonWeight}</li>
        </ul>
      </div>
      <Outlet />
    </>
  );
}
