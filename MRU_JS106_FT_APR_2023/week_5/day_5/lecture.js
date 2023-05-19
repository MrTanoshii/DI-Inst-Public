/*
Steps:

    1. Add the click event to the button
    2. Make a fetch pokemon from api function
    3. Onclick, fetch pokemon and add to list
    4. On error, display error message
    5. [BONUS] Add picture of pokemon to list using https://github.com/PokeAPI/sprites
*/

let apiUrl = "https://pokeapi.co/api/v2/pokemon/";

const fetchPokemon = async (pokemonName) => {
  // try {
  return await (await fetch(apiUrl + pokemonName)).json();
  // }
  // catch {

  // }
};

const addPokemon = async (pokemonName) => {
  const errorMsgEl = document.querySelector("#error-msg");
  errorMsgEl.innerText = "";

  try {
    let result = await fetchPokemon(pokemonName);

    // Add pokemon to the list
    let uListEl = document.querySelector("#pokeballs");
    let listItemEl = document.createElement("li");
    listItemEl.innerText = result.name + " - " + result.height;
    uListEl.appendChild(listItemEl);
  } catch {
    errorMsgEl.innerText = `Pokemon '${pokemonName}' failed.`;
    console.error(`Pokemon '${pokemonName}' failed.`);
  }
};

// console.log(fetchPokemon("pikachu"));

let btnEl = document.querySelector("#capture-btn");
let pokemonEl = document.querySelector("input[name='pokemon-name']");

btnEl.addEventListener("click", () => addPokemon(pokemonEl?.value));
