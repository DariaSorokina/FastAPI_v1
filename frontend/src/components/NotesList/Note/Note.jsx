import { useState } from "react";
import NoteViewer from "./NoteViewer";
import NoteEditor from "./NoteEditor";
import { NoteObject } from "../../../App";

export enum NoteView {
  VIEWING,
  EDITING,
}

export default function Acter({acters}: { acters: NoteObject }) {
  const [acterView, setActerView] = useState<NoteView>(NoteView.VIEWING);

  switch (acterView) {
    case NoteView.VIEWING:
      return <NoteViewer acter ={acters} setNoteView={setNoteView} />;
    case NoteView.EDITING:
      return <NoteEditor acter ={acters} setNoteView={setNoteView} />;
    default:
      return <></>;
  }
}