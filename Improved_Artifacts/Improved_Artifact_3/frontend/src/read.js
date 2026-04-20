// React Component for Reading Animal Records
// This component fetches and displays animal data from the shelter database
// Includes pagination for handling large datasets

import React, { useState } from "react";
import axios from "axios";

/**
 * Read Component - Implements the R in CRUD operations
 * Displays paginated list of animals with load functionality
 * @param {string} token - JWT authentication token
 * @param {Array} animals - Array of animal objects from parent state
 * @param {function} setAnimals - Function to update animals state in parent component
 */
function Read({ token, animals, setAnimals }) {
  // State for pagination
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 25;

  // Calculate pagination values
  const totalPages = Math.ceil(animals.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentAnimals = animals.slice(startIndex, endIndex);
  /**
   * Fetches animal records from the backend API
   * Updates the animals state with retrieved data
   */
  const loadAnimals = async () => {
    try {
      // Verify user authentication
      console.log(token);
      if (!token) {
        alert("Login first");
        return;
      }

      // Send GET request to retrieve animals
      const response = await axios.get("http://127.0.0.1:8000/animals", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      console.log("ANIMAL DATA:", response.data);

      // Update parent component's animals state
      setAnimals(response.data);
    } catch (err) {
      console.log(err);
      alert("Access denied. Login first.");
    }
  };

  return (
    <div>
      {/* Load button to fetch animal data */}
      <br />
      <button onClick={loadAnimals}>Load in animal records</button>

      {/* Display current page of animals */}
      <ul>
        {currentAnimals.map((animal) => (
          <li key={animal._id}>
            <div style={{ whiteSpace: "nowrap" }}>
              <span>Name: {animal.name || "no name"} | </span>
              <span>Breed: {animal.breed} | </span>
              <span>Age: {animal.age_upon_outcome} | </span>
              <span>Type: {animal.animal_type}</span>
            </div>
          </li>
        ))}
      </ul>

      {/* Pagination controls */}
      <div>
        {/* Page indicator */}
        <p>
          Page {currentPage} of {totalPages}
        </p>

        {/* Navigation buttons */}
        <button onClick={() => setCurrentPage(1)} disabled={currentPage === 1}>
          First
        </button>
        <button
          onClick={() => setCurrentPage(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        {/* Next page button */}
        <button
          onClick={() => setCurrentPage(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          Next
        </button>
        {/* Last page button */}
        <button
          onClick={() => setCurrentPage(totalPages)}
          disabled={currentPage === totalPages}
        >
          Last
        </button>
      </div>
    </div>
  );
}

export default Read;
