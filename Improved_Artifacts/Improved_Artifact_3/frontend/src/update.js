// React Component for Updating Animal Records
// This component provides an interface to select and modify existing animal records
// in the shelter database through the REST API

import React, { useState, useEffect } from "react";
import axios from "axios";

/**
 * Update Component - Implements the U in CRUD operations
 * Allows authenticated users to modify existing animal records
 * @param {Array} animals - Array of animal objects from parent state
 * @param {string} token - JWT authentication token
 * @param {function} setAnimals - Function to update animals state in parent component
 */
function Update({ animals, token, setAnimals }) {
  // State for selected animal and form data
  const [selectedAnimal, setSelectedAnimal] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    breed: "",
    age_upon_outcome: "",
    animal_type: "",
  });

  // Effect to populate form when animal is selected
  useEffect(() => {
    if (selectedAnimal) {
      setFormData({
        name: selectedAnimal.name || "",
        breed: selectedAnimal.breed || "",
        age_upon_outcome: selectedAnimal.age_upon_outcome || "",
        animal_type: selectedAnimal.animal_type || "",
      });
    }
  }, [selectedAnimal]);

  /**
   * Handles selection of animal from dropdown
   * Finds and sets the selected animal object
   */
  const handleSelectChange = (e) => {
    const animalId = e.target.value;
    const animal = animals.find((a) => a._id === animalId);
    setSelectedAnimal(animal);
  };

  /**
   * Handles input field changes
   * Updates form data state with new values
   */
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  /**
   * Handles the update of an existing animal record
   * Sends PUT request to backend API with query and updated data
   * Updates local state on success
   */
  const updateAnimal = async () => {
    // Check authentication
    if (!token) {
      alert("Login first");
      return;
    }

    // Check if animal is selected
    if (!selectedAnimal) {
      alert("Select an animal to update");
      return;
    }

    try {
      // Send PUT request to update animal
      const response = await axios.put(
        "http://127.0.0.1:8000/animals",
        {
          query: { _id: selectedAnimal._id },
          data: formData,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      console.log("UPDATE RESPONSE:", response.data);

      // Update the animals state
      setAnimals(
        animals.map((a) =>
          a._id === selectedAnimal._id ? { ...a, ...formData } : a,
        ),
      );

      alert("Animal updated successfully");
    } catch (err) {
      console.log(err);
      alert("Update failed");
    }
  };

  return (
    <div>
      {/* Component title */}
      <h3>Update Animal</h3>

      {/* Dropdown to select animal for updating */}
      <select onChange={handleSelectChange} defaultValue="">
        <option value="" disabled>
          Select an animal to update
        </option>
        {animals.map((animal, index) => (
          <option key={index} value={animal._id}>
            {animal.name || "no name"} - {animal.breed}
          </option>
        ))}
      </select>

      {/* Form appears when animal is selected */}
      {selectedAnimal && (
        <div>
          {/* Form inputs for animal data */}
          <br />
          <input
            type="text"
            name="name"
            placeholder="Name"
            value={formData.name}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <input
            type="text"
            name="breed"
            placeholder="Breed"
            value={formData.breed}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <input
            type="text"
            name="age_upon_outcome"
            placeholder="Age Upon Outcome"
            value={formData.age_upon_outcome}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <input
            type="text"
            name="animal_type"
            placeholder="Animal Type"
            value={formData.animal_type}
            onChange={handleInputChange}
          />
          <br />
          <br />

          {/* Submit button to update animal */}
          <button onClick={updateAnimal}>Update Animal</button>
        </div>
      )}
    </div>
  );
}

export default Update;
