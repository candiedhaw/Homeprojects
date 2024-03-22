
import os
import pandas as pd
import random
import vlc


# Path to the directory containing the MP3 files
directory_path = 'resources/Suzuki_Violin_Hilary/'

# Get the book folder name
book_mapping = {   "1": "Book1",
                   "2": "Book2",
                   "3": "Book3"}

user_input = input("Enter the book number as a number (1, 2, or 3): ")

folder_name = book_mapping.get(user_input, None)
if folder_name:
    print(f"Book chosen: {folder_name}")
else:
    print("Error: Invalid input. Please enter 1, 2, or 3.")



###########Creat song table and accomp table

# Get all file names in the directory
file_names = os.listdir(directory_path + folder_name + '/')

# Filter out only the MP3 files
mp3_files = [file for file in file_names if file.lower().endswith('.mp3')]

# Count the total number of MP3 files
file_counts = len(mp3_files)

# Calculate the number of songs (half of file_counts)
song_counts = file_counts // 2


# Initialize an empty DataFrame for file names
columns = ["Track Number", "Song Title", "File Name"]
file_name_df = pd.DataFrame(columns=columns)

# Extract track number and song title from each file name
for mp3_file in mp3_files:
    parts = mp3_file.split(" - ", 1)
    track_number = parts[0].strip()
    file_name = mp3_file
    song_title = parts[1].split("(")[0].strip() # Remove anything include and after "(" of the song name

    # Use pd.concat() to append rows
    file_name_df = pd.concat([file_name_df, pd.DataFrame({"Track Number": [track_number], "Song Title": [song_title], "File Name": [file_name]})], ignore_index=True)

# Sort the DataFrame based on track number, reset index
sorted_df = file_name_df.sort_values(by="Track Number", key=lambda x: x.astype(int)).reset_index(drop=True)

# Convert 'Track Number' column from string to integer
sorted_df["Track Number"] = sorted_df["Track Number"].astype(int)

# Create song_table (top half of the sorted DataFrame)
song_df = sorted_df.iloc[:song_counts]

# Create accomp_table (rest of the songs)
accomp_df = sorted_df.iloc[song_counts:]

# Print the results
print("File Counts:", file_counts)
print("Song Counts:", song_df)
print("\nSong Table:")
print(song_df.iloc[:, :-1].to_string(index=False))
#print("\nAccompaniment Table:")
#print(accomp_table)


############Play song


# Generate 3 random indices
random_indices = random.sample(range(song_counts), 3)

# Initialize VLC player
instance = vlc.Instance()
player = instance.media_player_new()

# Play each song twice at 0.75x speed
for index in random_indices:
    track_number, song_title, file_name = song_df.iloc[index]  # No need to skip header row
    print(f"Playing Track {track_number}: {song_title}")

    media = instance.media_new(directory_path + folder_name + '/' + file_name)
    player.set_media(media)

    # Play the song 2 time
    for _ in range(2):
        player.play()
        player.set_rate(8)
        while player.get_state() != vlc.State.Ended:
            pass  # Wait for song to finish playing

# Clean up
player.stop()

