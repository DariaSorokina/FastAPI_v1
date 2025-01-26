import { useContext } from "react";
import axios from "axios";

import { NotesListUpdateFunctionContext } from "../../../App";
import "./DeleteModal.styles.css";

export default function DeleteModal({ acter_id, showDeleteModal }) {
  const setActers = useContext(NotesListUpdateFunctionContext);
  const handleYesClick = async () => {
    const API_URL = "http://127.0.0.1:8000";
    await axios.delete(`${API_URL}/api/v1/acters/${acter_id}`);
    const { data } = await axios.get(`${API_URL}/acters`);
    setActers(data);
    showDeleteModal(false);
  };
  const handleNoClick = () => {
    showDeleteModal(false);
  };
  return (
    <div id="delete-modal-container">
      <div id="delete-modal">
        <p id="prompt-msg">Delete this Acter?</p>
        <div id="btn-container">
          <button id="yes-btn" onClick={() => handleYesClick()}>
            Yes
          </button>
          <button id="no-btn" onClick={handleNoClick}>
            No
          </button>
        </div>
      </div>
    </div>
  );
}