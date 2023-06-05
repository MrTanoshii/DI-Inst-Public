import "./App.css";
import Student from "./Student";
import Student2 from "./Student2";
import Longanist from "./Longanist.js";

const charactersJson = {
  people: [
    {
      id: "1",
      name: "Luke Skywalker",
      height: "172",
      mass: "77",
      hair_color: "blond",
    },
    {
      id: "2",
      name: "C-3PO",
      height: "167",
      mass: "75",
      hair_color: "n/a",
    },
    {
      id: "3",
      name: "R2-D2",
      height: "96",
      mass: "32",
      hair_color: "n/a",
    },
  ],
};
const characters = JSON.parse(JSON.stringify(charactersJson));

const listOfLonganist = [
  {
    id: 1,
    name: "Blessing",
    services: "Good fortune",
    price: "$10,000",
  },
  {
    id: 2,
    name: "Dhivyesh",
    services: "High marks",
    price: "2 Chicken",
  },
  {
    id: 3,
    name: "Tushil",
    services: "Bad luck",
    price: "Free",
  },
];

function App() {
  return (
    <div>
      <Longanist listOfLonganist={listOfLonganist} />
      <Student studentName="Khavind" />
      <Student2 studentName="Sanjiv" />
      {/* 
      <h1>Hello {diClassName} DI</h1>
      {myelement}
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div> */}
      {characters.people.map((item) => (
        <ul key={item.id}>
          <li>{item.name}</li>
          <li>{item.height}</li>
          <li>{item.hair_color}</li>
        </ul>
      ))}
    </div>
  );
}

export default App;
