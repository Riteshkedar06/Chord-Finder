import os

# Define the base directory where you want to create the chord folders
base_dir = "/Users/ritesh/Documents/projects/ChordFinder/datasets"

# Define the chords including major and minor
chords = ["A_major", "A_minor", "B_major", "B_minor", "C_major", "C_minor", 
          "D_major", "D_minor", "E_major", "E_minor", "F_major", "F_minor", 
          "G_major", "G_minor"]

# Function to create directories for each chord
def create_chord_directories(base_dir, chords):
    for chord in chords:
        dir_path = os.path.join(base_dir, chord)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

# Run the function
create_chord_directories(base_dir, chords)
