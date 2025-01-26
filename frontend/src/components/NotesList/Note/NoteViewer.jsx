import { useState } from "react";

import DeleteModal from "./DeleteModal";
import { NoteView } from "./Note";

import "./Note.styles.css";

export default function ActerViewer({ acter, setActerView }) {
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const { id, name, show, gender, part } = acter;
  const handleDeleteNote = () => {
    setShowDeleteModal(true);
  };
  return (
    <div id="note-container">
      {showDeleteModal && (
        <DeleteModal showDeleteModal={setShowDeleteModal} noteId={id} />
      )}
      <h3>{name}</h3>
      <p>{show}</p>
      <p>{gender}</p>
      <p>{part}</p>
      <div className="note-buttons-container">
        <button
          className="neutral-btn"
          onClick={() => setNoteView("editing")}
        >
          Edit
        </button>
        <button className="delete-btn" onClick={() => handleDeleteNote()}>
          Delete
        </button>
      </div>
    </div>
  );
}