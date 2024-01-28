import React from "react";

function RecipeForm({ getData }) {
  const onSubmitHandler = (data) => {
    data.preventDefault();

    let finalData = [];
    for (let i = 0; i < 5; i++) {
      finalData.push(data.target[i].value);
    }
    getData(finalData);
  };
  return (
    <React.Fragment>
      <form
        style={{ textAlign: "center" }}
        onSubmit={(data) => {
          onSubmitHandler(data);
        }}
      >
        <label htmlFor="food_items">
          All the Ingredients: <input type="text" id="food_items" />
        </label>
        <br />
        <br />
        <label htmlFor="spice_level">
          Please Select Your Spice Level:
          <select id="spice_level">
            <option value={"Low Heat"}>Low Heat</option>
            <option value={"Medium Heat"}>Medium Heat</option>
            <option value={"Spicy"}>Spicy</option>
          </select>
        </label>
        <br />
        <br />
        <label htmlFor="cuisine">
          Preferred Cuisine:
          <input type="text" id="cuisine" />
        </label>
        <br />
        <br />
        <label htmlFor="is_veg">
          What do you prefer?
          <select id="is_veg">
            <option value={"is_veg"}>Vegeterian</option>
            <option value={"is_non_veg"}>Non-Vegeterian</option>
          </select>
        </label>
        <br />
        <br />
        <label htmlFor="allergy">
          Do you have any allergies?
          <input type="text" id="allergy" />
        </label>
        <br />
        <br />
        <button type="submit">GET RECIPE!</button>
      </form>
    </React.Fragment>
  );
}

export default RecipeForm;
