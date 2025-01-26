import { useState, useEffect, useRef, useContext, FormEvent } from "react";
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

  const titleInputRef = useRef<HTMLInputElement>({} as HTMLInputElement);

  useEffect(() => {
    titleInputRef.current.focus();
  }, []);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

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






      <textarea
        placeholder="Enter Note"
        id="note-body-textarea"
        className={hasInputError ? "input-error" : ""}
        cols={30}
        rows={10}
        value={noteBody}
        onChange={(event) => {
          setHasInputError(false);
          setNoteBody(event.target.value);
        }}
      />
      <button id="add-note-btn" type="submit" disabled={isFormSubmitting}>
        {isFormSubmitting ? "..." : "Add Note"}
      </button>
    </form>
  );
}