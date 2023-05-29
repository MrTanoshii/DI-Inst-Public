export function getCurrentDate() {
  return Date();
}

export var helloStudent = "Hello Student!";

export const listGames = (person_name, ...game_list) => {
  console.log(`This is the game list of ${person_name}:`);
  for (const game_index in game_list) {
    console.log(`${parseInt(game_index) + 1}. ${game_list[game_index]}`);
  }
};
