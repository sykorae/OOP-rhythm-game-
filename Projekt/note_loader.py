from parser import parse_sm_file
from note import NoteLeft, NoteRight, NoteUp, NoteDown, Note
from config import *
from parser import parse_sm_file

column_to_notetype = {
    0: NoteLeft,
    1: NoteDown,
    2: NoteUp,
    3: NoteRight,
}
def create_notes(filename: str) -> list[Note]:
    sm_data = parse_sm_file("Projekt/FireStarter.sm")
    bpm = list(sm_data["bpms"].values())[0]
    offset = sm_data["offset"]
    bars = sm_data["bars"]

    seconds_per_beat = 60 / bpm
    total_beats = 0
    notes = []

    for bar in bars:
        num_lines = len(bar)
        for i, line in enumerate(bar):
            beat_in_bar = (i / num_lines) * 4.0
            beat_time = total_beats + beat_in_bar
            timestamp = offset + beat_time * seconds_per_beat

            for column, char in enumerate(line):
                if char == "1":
                    if column == 0:
                        notes.append(NoteLeft(timestamp, FALL_SPEED, SCREEN_H ))
                    if column == 1:
                        notes.append(NoteDown(timestamp, FALL_SPEED, SCREEN_H ))
                    if column == 2:
                        notes.append(NoteUp(timestamp, FALL_SPEED, SCREEN_H ))
                    if column == 3:
                        notes.append(NoteRight(timestamp, FALL_SPEED, SCREEN_H ))
            # LM: Check this one.
            
            # for column, char in enumerate(line):
            #     if char == "1":
            #         notes.append(column_to_notetype[column](timestamp, FALL_SPEED, SCREEN_H))
        total_beats += 4
    return notes
    