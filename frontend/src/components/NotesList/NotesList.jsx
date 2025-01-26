import { NoteObject } from "../../App";
import Note from "./Note";

import "./NotesList.styles.css";

export default function NotesList({acters}) {
  return (
    <div id="acters-list-container">
      <h2 id="acters-list-header">Acter</h2>
      <ul id="acters-list">
        {acters.map((acter) => (
          <li key={acter.id}>
            <Acter acter={acter} />
          </li>
        ))}
      </ul>
    </div>
  );
}