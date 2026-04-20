// React Component for Deleting Animal Records
// This component provides batch deletion functionality for animal records
// Includes pagination and checkbox selection for managing large datasets

import React, { useState } from "react";
import axios from "axios";

/**
 * Delete Component - Implements the D in CRUD operations
 * Allows authenticated users to select and delete multiple animal records
 * @param {Array} animals - Array of animal objects from parent state
 * @param {string} token - JWT authentication token
 * @param {function} setAnimals - Function to update animals state in parent component
 */
function Delete({ animals, token, setAnimals }) {
  // State for selected animals and pagination
  const [toDelete, setToDelete] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 25;

  // Calculate pagination values
  const totalPages = Math.ceil(animals.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentAnimals = animals.slice(startIndex, endIndex);

  /**
   * Handles checkbox selection/deselection of animals for deletion
   * Toggles animal in/out of toDelete array
   */
  const handleSelect = (animal) => {
    if (toDelete.includes(animal)) {
      setToDelete(toDelete.filter((a) => a !== animal));
    } else {
      setToDelete([...toDelete, animal]);
    }
  };

  /**
   * Handles batch deletion of selected animals
   * Sends DELETE requests for each selected animal and updates state
   */
  const deleteSelected = async () => {
    if (!token) {
      alert("Login first");
      return;
    }

    try {
      for (let animal of toDelete) {
        await axios.delete("http://127.0.0.1:8000/animals", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
          data: { _id: animal._id },
        });
      }

      // Update animals state by removing deleted ones
      setAnimals(animals.filter((a) => !toDelete.includes(a)));
      setToDelete([]);
      setCurrentPage(1); // Reset to first page after deletion
      alert("Deleted successfully");
    } catch (err) {
      console.log(err);
      alert("Delete failed");
    }
  };

  return (
    <div>
      {/* Component title */}
      <h3>Select Animals to Delete</h3>

      {/* List of animals with checkboxes for selection */}
      <ul>
        {currentAnimals.map((animal, index) => (
          <li key={animal._id || index}>
            <input
              type="checkbox"
              checked={toDelete.includes(animal)}
              onChange={() => handleSelect(animal)}
            />
            <span>
              {animal.name || "no name"} - {animal.breed}
            </span>
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
        <button
          onClick={() => setCurrentPage(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <button
          onClick={() => setCurrentPage(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          Next
        </button>
      </div>
      <button onClick={deleteSelected}>Delete Selected</button>
    </div>
  );
}

export default Delete;
