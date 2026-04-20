import React, { useState } from "react";
import axios from "axios";
import Read from "./read";
import Create from "./create";
import Update from "./update";
import Delete from "./delete";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [token, setToken] = useState(localStorage.getItem("token") || "");

  const [animals, setAnimals] = useState([]);

  const login = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/login", null, {
        params: {
          username,
          password,
        },
      });

      console.log("LOGIN RESPONSE:", response.data);

      if (!response.data.access_token) {
        alert("Login failed");
        return;
      }

      localStorage.setItem("token", response.data.access_token);

      setToken(response.data.access_token);

      alert("Login successful");
    } catch (err) {
      console.log(err.response);

      alert("Login failed");
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setToken("");
    setAnimals([]);
    alert("Logged out successfully");
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Animal Shelter Portal</h1>

      {token ? (
        <>
          <h2>Welcome! You are logged in.</h2>
          <button onClick={logout}>Logout</button>
          <br />
          <hr />
          <Read token={token} animals={animals} setAnimals={setAnimals} />
          <Create token={token} setAnimals={setAnimals} />
          <br />
          <hr />
          <Update token={token} animals={animals} setAnimals={setAnimals} />
          <br />
          <hr />
          <Delete token={token} animals={animals} setAnimals={setAnimals} />
          <br />
          <hr />
        </>
      ) : (
        <>
          <h2>Login</h2>
          <input
            placeholder="username"
            onChange={(e) => setUsername(e.target.value)}
          />
          <br />
          <br />
          <input
            placeholder="password"
            type="password"
            onChange={(e) => setPassword(e.target.value)}
          />
          <br />
          <br />
          <button onClick={login}>Login</button>
        </>
      )}
    </div>
  );
}

export default App;
