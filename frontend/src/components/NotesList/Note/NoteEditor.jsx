import axios from "axios";
import { useState, useContext } from "react";
import { NotesListUpdateFunctionContext } from "../../../App";
import { NoteView } from "./Note";

import "./Note.styles.css";

export default function NoteEditor({ acter, setActerView }) {
  const [acterName, setActerName] = useState(acter.name);
  const [acterShow, setActerShow] = useState(acter.show);
  const [acterGender, setActerGender] = useState(acter.gender);
  const [acterPart, setActerPart] = useState(acter.part);
  const [isInvalidSave, setIsInvalidSave] = useState(false);
  const setActers = useContext(NotesListUpdateFunctionContext);
  const handleNoteSave = async (event, id) => {
    event.preventDefault();
    if (acterName.length > 0 || acterShow.length > 0) {
      const API_URL = "http://127.0.0.1:8000";
      await axios.put(`${API_URL}/api/v1/acters/${id}`, {
        name: acterName,
        show: acterShow,
        gender: acterGender,
        part: acterPart,
      });
      const { data } = await axios.get(`${API_URL}/api/v1/acters`);
      setActers(data);
      setActerView("viewing");
    } else {
      setIsInvalidSave(true);
      noteTitleInputRef.current.focus();
    }
  };
  return (
    <form
      id="acter-container"
      onSubmit={(event) => handleNoteSave(event, acter.id)}
    >
      <input
        type="text"
        placeholder="Enter Acter Name"
        id="acter-name-edit-input"
        className={isInvalidSave ? "input-error" : ""}
        value={acterName}
        onChange={(event) => {
          setIsInvalidSave(false);
          setActerName(event.target.value);
        }}
      />
      <input
        type="text"
        placeholder="Enter Acter Show"
        id="acter-show-edit-input"
        className={isInvalidSave ? "input-error" : ""}
        value={acterShow}
        onChange={(event) => {
          setIsInvalidSave(false);
          setActerShow(event.target.value);
        }}
      />
      <input
        type="text"
        placeholder="Enter Acter Gender"
        id="acter-gender-edit-input"
        className={isInvalidSave ? "input-error" : ""}
        value={acterGender}
        onChange={(event) => {
          setIsInvalidSave(false);
          setActerGender(event.target.value);
        }}
      />
      />
      <input
        type="text"
        placeholder="Enter Acter Part"
        id="acter-part-edit-input"
        className={isInvalidSave ? "input-error" : ""}
        value={acterPart}
        onChange={(event) => {
          setIsInvalidSave(false);
          setActerPart(event.target.value);
        }}
      />
      <div className="note-buttons-container">
        <button className="save-btn" type="submit">
          Save
        </button>
        <button
          className="neutral-btn"
          type="button"
          onClick={() => setActerView("viewing")}
        >
          Cancel
        </button>
      </div>
    </form>
  );
}