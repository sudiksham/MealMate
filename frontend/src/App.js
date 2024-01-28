import React, { useState, useEffect, Component } from "react";
import "./App.css";
import axios from "axios";
import cogWheel from "./images/settings.png";
import logo from "./images/mealmate.png";
import NavBar from "./components/NavBar";
import RecipeForm from "./components/RecipeForm";
function App() {
  const [entries, setEntries] = useState([]);

  function addEntry(newEntry) {
    setEntries((prevEntries) => [...prevEntries, newEntry]);
  }
  const dataHandler = async (data) => {
    console.log(data);
    let modifiedData = {
      food_items: data[0].split(","),
      spice_level: data[1],
      cuisine: data[2],
      is_veg: data[3],
      allergy: data[4],
    };
    console.log(modifiedData);
    await axios({
      method: "POST",
      url: "http://127.0.0.1:8000/",
      data: modifiedData,
    }).then((response) => {
      // Assuming response.data contains the new entry
      addEntry(response.data);
    });
  };
  return (
    <div className="App">
      <NavBar cogWheel={cogWheel} logo={logo}></NavBar>
      <RecipeForm getData={dataHandler} />
      {entries.length > 0 && <h1>Recipe: </h1>}
      {entries && entries.map((entry, index) => <div key={index}>{entry}</div>)}
    </div>
  );
}

export default App;
