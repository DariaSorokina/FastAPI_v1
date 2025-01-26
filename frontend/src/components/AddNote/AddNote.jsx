import { useState, useEffect, useRef, useContext, FormEvent, FormEventHandler } from "react";
import axios from "axios";

import "./AddNote.styles.css";
import { NoteObject, NotesListUpdateFunctionContext } from "../../App";

export default function AddNote() {
  const [name, setName] = useState("");
  const [show, setShow] = useState("");
  const [gender, setGender] = useState("");
  const [part, setPart] = useState("");
  const [isFormSubmitting, setIsFormSubmitting] = useState(false);
  const [hasInputError, setHasInputError] = useState(false);

  const setActers = useContext(NotesListUpdateFunctionContext);

  const titleInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    titleInputRef.current.focus();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
     e.preventDefault();
    if (name.length > 0 || show.length > 0) {
      setIsFormSubmitting(true);
      const API_URL = import.meta.env.VITE_NOTES_API_URL;
      const { data } = await axios.post<NoteObject>(`${API_URL}/api/v1/acters`, {
        name,
        show,
        gender,
        part,
      });
      setActers((prev) => [...prev, data]);
    } else {
      setHasInputError(true);
    }
    setName("");
    setShow("");
    setGender("");
    setPart("");
    setIsFormSubmitting(false);
    titleInputRef.current.focus();
  };

  return (
    <form onSubmit={(event) => void handleSubmit(event)} id="add-note-form">
      <input
        type="text"
        placeholder="Enter Name"
        ref={titleInputRef}
        id="name-input"
        className={hasInputError ? "input-error" : ""}
        value={name}
        onChange={(event) => {
          setHasInputError(false);
          setName(event.target.value);
        }}
      />
      <input
        type="text"
        placeholder="Enter Show"
        ref={titleInputRef}
        id="show-input"
        className={hasInputError ? "input-error" : ""}
        value={show}
        onChange={(event) => {
          setHasInputError(false);
          setShow(event.target.value);
        }}
      />
      />
      <input
        type="text"
        placeholder="Enter Gender"
        ref={titleInputRef}
        id="gender-input"
        className={hasInputError ? "input-error" : ""}
        value={gender}
        onChange={(event) => {
          setHasInputError(false);
          setGender(event.target.value);
        }}
      />
      />
      <input
        type="text"
        placeholder="Enter Part"
        ref={titleInputRef}
        id="part-input"
        className={hasInputError ? "input-error" : ""}
        value={part}
        onChange={(event) => {
          setHasInputError(false);
          setPart(event.target.value);
        }}
      />
      <button id="add-note-btn" type="submit" disabled={isFormSubmitting}>
        {isFormSubmitting ? "..." : "Add Note_2"}
      </button>
    </form>
  );
}