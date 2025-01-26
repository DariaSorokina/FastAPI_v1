import {
  useState,
  useEffect,
  createContext,
  Dispatch,
  SetStateAction,
} from "react";
import axios from "axios";

import AddNote from "./components/AddNote";
import NotesList from "./components/NotesList";

import "./App.css";
import "./utility.styles.css";

export const NotesListUpdateFunctionContext = createContext(null);

export default function App() {
  const [acters, setActers] = useState([]);
  useEffect(() => {
    const getActers = async () => {
			// The URL of the backend
			// you can specify your own if you have a different one
      const API_URL = "http://127.0.0.1:8000";
      const { data } = await axios.get(`${API_URL}/api/v1/acters`);
      setActers(data);
    };
    getActers();
  }, []);
  return (
    <NotesListUpdateFunctionContext.Provider value={setActers}>
      <div>
        <h1 id="app-title">Acters App</h1>
        <AddNote />
        <NotesList acters={acters} />
      </div>
    </NotesListUpdateFunctionContext.Provider>
  );
}