import re

def get_tag_value(text, tag, default=None):
    pattern = rf"#{tag}:(.*?);" #looks for #{tag}:<anything here>; , stops searching after first ;
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL) #ignorecase accepts any type of text (lowercase and uppercase), dotall allows to look for text through multiple lines 
    if match:
        return match.group(1).strip() #group(1) takes the text after #{tag}:
    return default

def get_bpm_data(text):
    bpm_line = get_tag_value(text, "BPMS") # stores beat = bpm
    if bpm_line is None:
        print("No BPMS tag found in the .sm file.")
        return {}

    bpm_pairs = bpm_line.split(",") # if there is more bpms, this separates them 
    bpm_dict = {}
    for pair in bpm_pairs:
        try:
            beat, bpm = pair.strip().split("=") #separates beat and bpm and stores them
            bpm_dict[float(beat)] = float(bpm) # adds to dictionary
        except ValueError:
            print(f"Malformed BPM entry: {pair}")
    return bpm_dict
    

def get_notes_data(text):
    notes_sections = re.findall(r"#NOTES:(.*?);", text, re.IGNORECASE | re.DOTALL) # returns all text after #NOTES: 
    if not notes_sections:
        print("No NOTES section found.")
        return []

    steps = []
    for section in notes_sections:
        lines = section.strip().split("\n") # separates text from each line
        data_lines = [line.strip() for line in lines if line.strip() and not line.strip().endswith(":")]  # discards empty strings, strips spaces and discarld lines ending with :
        for line in data_lines:
            if all(c in "0123M," for c in line):  # only 0123M are valid symbols (excludes lines with ",")
                steps.append(line)
    return steps
    

def parse_sm_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    title = get_tag_value(content, "TITLE")
    offset_str = get_tag_value(content, "OFFSET", default="0")
    try:
        offset = float(offset_str)
    except ValueError:
        print(f"Invalid offset value: {offset_str}, defaulting to 0.0")
        offset = 0.0

    bpms = get_bpm_data(content)
    note_data = get_notes_data(content)

    return {
        "title": title,
        "offset": offset,
        "bpms": bpms,
        "notes": note_data,
    }

# TEST OUTPUT
parsed = parse_sm_file("Projekt/FireStarter.sm")

print("Title:", parsed["title"])
print("Offset:", parsed["offset"])
print("BPMs:", parsed["bpms"])
print("Note lines:", parsed["notes"])