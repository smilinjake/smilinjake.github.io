// React Component for Creating New Animal Entries
// This component provides a form interface for users to add new animals
// to the shelter database through the REST API

import React, { useState } from "react";
import axios from "axios";

/**
 * Create Component - Implements the C in CRUD operations
 * Allows authenticated users to create new animal records
 * @param {string} token - JWT authentication token
 * @param {function} setAnimals - Function to update the animals state in parent component
 */
function Create({ token, setAnimals }) {
  // State variables for form inputs
  const [name, setName] = useState("");
  const [breed, setBreed] = useState("");
  const [age, setAge] = useState("");
  const [animal_type, setType] = useState("");

  /**
   * Handles the creation of a new animal record
   * Sends POST request to backend API with form data
   * Updates local state on success and clears form
   */
  const createAnimal = async () => {
    try {
      // Check if user is authenticated
      if (!token) {
        alert("Login first");
        return;
      }

      // Prepare animal data object for API request
      const animalData = {
        name,
        breed,
        age_upon_outcome: age,
        animal_type,
      };

      // Send POST request to create new animal
      const response = await axios.post(
        "http://127.0.0.1:8000/animals",
        animalData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      console.log("ANIMAL CREATED:", response.data);

      // Update parent component's animals state with new record
      setAnimals((prev) => [...prev, response.data]);

      // Clear form fields after successful creation
      setName("");
      setBreed("");
      setAge("");
      setType("");

      alert("Animal created successfully");
    } catch (err) {
      console.log(err);
      alert("Create failed");
    }
  };

  return (
    <>
      {/* Section divider */}
      <hr />
      {/* Component title */}
      <h3>Create New Entry</h3>

      {/* Form inputs for animal data */}
      <input
        value={name}
        placeholder="Name"
        onChange={(e) => setName(e.target.value)}
      />
      <input
        value={breed}
        placeholder="Breed"
        onChange={(e) => setBreed(e.target.value)}
      />
      <input
        value={age}
        placeholder="Age"
        onChange={(e) => setAge(e.target.value)}
      />
      <input
        value={animal_type}
        placeholder="Type"
        onChange={(e) => setType(e.target.value)}
      />

      {/* Submit button to create animal */}
      <button onClick={createAnimal}>Create</button>
    </>
  );
}

export default Create;
