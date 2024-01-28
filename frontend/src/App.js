import React, { useState, useEffect, Component } from 'react';
import './App.css';
import ImageUpload from './components/ImageUpload';
import axios from 'axios'
import cogWheel from "./images/settings.png"
import logo from "./images/mealmate.png"
import NavBar from './components/NavBar'
function App() {

 const [entries, setEntries] = useState([])

 function addEntry(newEntry){
  setEntries((prevEntries) => [...prevEntries, newEntry]);
 }
  return (
    
    <div className="App">
      <NavBar cogWheel = {cogWheel} logo = {logo}></NavBar>
      <ImageUpload addEntry={addEntry}></ImageUpload>
      {entries && entries.map((entry, index) => (
          <div key={index}>
            {entry.foods_identified}
            {entry.recipe}
            {entry.calories}
            {entry.protein}
            {entry.carbs}
            {entry.fats}
            {entry.sugar}
          </div>
        ))}
    </div>
  );
}

export default App;
