// A simple website that fetches pokemon names stores them in a PostgreSQL db.
// Provides an API endpoint to return the pokemon.

const knex = require("knex")({
  client: "pg",
  version: "8.11",
  connection: {
    host: "127.0.0.1",
    port: 5432,
    user: "postgres",
    password: "postgres",
    database: "project_1",
  },
});

const express = require("express");
const app = express();
const port = 3000;

app.use("/public", express.static("public"));

app.all("/:name", (req, res) => {
  res.send(`<h1>Hello ${req?.params?.name}</h1>`);
  res.end();
});
app.all("/pokemon/:name", (req, res) => {
  const pokemonPromise = getPokemonFromDB(req?.params?.name);
  pokemonPromise.then((pokemon) => {
    res.setHeader("content-type", "application/json");
    res.header("Access-Control-Allow-Origin", "*");
    res.send(JSON.stringify(pokemon));
    res.end();
  });
});
app.all("/pokemon/view/:name", (req, res) => {
  const pokemonPromise = getPokemonFromDB(req?.params?.name);
  pokemonPromise.then((pokemon) => {
    res.send(`<img src="/public/${pokemon.icon}"/>`);
    res.end();
  });
});
app.all("*", (req, res) => {
  res.send("<h1>404 Page not found.</h1>");
  res.end();
});

app.listen(port, () => {
  console.log(`The server is listening on ${port}`);
});

// https://pokeapi.co/api/v2/

const getPokemonFromAPI = async (pokemonName) => {
  const linkFetch = fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
  const resultJson = (await linkFetch).json();
  //   console.log(resultJson);
  //   const faviconLink = await resultJson;
  //   console.log(faviconLink);
  //   console.log("Found link: " + faviconLink);
  //   return faviconLink;
  return resultJson;
};

// const result = getPokemonDetails("mewtwo");
// console.log(result);

const getPokemonFromDB = async (pokemonName) => {
  const dbResult = await knex
    .select("*")
    .from("pokemon")
    .where("name", pokemonName);
  return dbResult[0];
};

const fs = require("fs");
const https = require("https");
const path = require("path");

// const pokemonPromise = getPokemonFromAPI("arbok");
// pokemonPromise.then((pokemon) => {
//   https.get(pokemon.sprites?.back_default, (res) => {
//     // Open file in local filesystem
//     const fileName = path.basename(pokemon.sprites?.back_default);
//     const file = fs.createWriteStream(`./public/${fileName}`);

//     // Write data into local file
//     res.pipe(file);

//     // Close the file
//     file
//       .on("finish", () => {
//         file.close();
//         console.log(`File downloaded!`);

//         knex("pokemon")
//           .insert({
//             name: pokemon.name,
//             icon: fileName,
//             weight: pokemon.weight,
//           })
//           .then(() => {
//             console.log("Pokemon inserted into db");
//             return true;
//           })
//           .catch((err) => {
//             console.error(err);
//             return false;
//           });
//       })
//       .on("error", (err) => {
//         console.log("Error: ", err.message);
//       });
//   });
// });
