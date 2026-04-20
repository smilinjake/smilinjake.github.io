# Animal Shelter Management System

A web app for managing animal shelter records. You can add, view, update, and delete animal data from a simple interface.

## What You Need

Before you start, make sure you have:

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- MongoDB
- Git

## Getting Started

### 1. Get the code

```bash
git clone <repository-url>
cd CS_499_Module_5_Milestone
```

### 2. Set up MongoDB

Make sure MongoDB is running on your computer. The database and collection will be created automatically when you start the backend.

If you want sample data, you can import the CSV file (optional):

```bash
mongoimport --uri "mongodb://aacuser:admin@localhost:27017/aac" \
  --collection=animals \
  --type=csv \
  --headerline \
  --file=aac_shelter_outcomes.csv
```

Or just skip this step and start with an empty database - you can add animals through the app.

### 3. Set up the backend

First, install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Then start the backend server:

```bash
uvicorn main:app --reload
```

The API will run at `http://127.0.0.1:8000`

### 4. Set up the frontend

Open a new terminal and go to the frontend folder:

```bash
cd frontend
npm install
npm start
```

The app will open in your browser at `http://localhost:3000`

## How to Log In

Use these credentials:

- Username: `admin`
- Password: `password`

## What You Can Do

**View Animals** - Click "Load in animal records" to see all the animals. You can flip through pages with the buttons at the bottom.

**Add Animals** - Fill in the name, breed, age, and type, then click Create. It shows up right away.

**Edit Animals** - Pick an animal from the dropdown, change the info you want, and click Update.

**Delete Animals** - Check the boxes next to the animals you want to delete, then click "Delete Selected". You can pick animals from different pages before deleting.

**Log Out** - Click the Logout button to leave the app safely.

## Folder Structure

```
CS_499_Module_5_Milestone/
├── backend/
│   ├── main.py              # API stuff
│   ├── auth.py              # Login logic
│   ├── CRUD_Python_Module.py # Database operations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── create.js
│   │   ├── read.js
│   │   ├── update.js
│   │   ├── delete.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## Common Problems

**Backend won't start** - Make sure MongoDB is running and port 8000 is free.

**Frontend won't start** - Check that Node.js is installed and port 3000 is available.

**Can't log in** - Make sure the backend is running and you're using the right credentials.

**MongoDB errors** - Check that MongoDB is actually running on your computer.

## API Endpoints

- `POST /login` - Log in
- `GET /animals` - Get all animals
- `POST /animals` - Add an animal
- `PUT /animals` - Update an animal
- `DELETE /animals` - Delete an animal

## Notes

All requests to the API need a token from logging in.

The default MongoDB connection is `mongodb://aacuser:admin@localhost:27017/aac`

---

This is a school project for CS 499. The username and password are hardcoded for testing.</content>
