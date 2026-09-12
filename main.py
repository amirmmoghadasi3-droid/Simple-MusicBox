import pygame
import os
from pathlib import Path

# test folder (music/audio files)
MUSIC_FOLDER = Path("music")
# audio file extensions
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma'}

# finding audio files inside the folder
def Find_Audio_Files(folder_path: Path):
    audio_files = []
    for file in folder_path.iterdir():
        if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS:
            audio_files.append(file)
    return sorted(audio_files)

# playing the selected music
def Play_Music(file_path: Path):
    print(f"({file_path.name})playing...")

    try:
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.play()

        # wiat until music finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as Error:
        print(f"cant play this audio (ERROR: {Error})")

# main program
def main():
    # check if test folder exist 
    if not MUSIC_FOLDER.is_dir():
        print(f"Folder '{MUSIC_FOLDER}' dose not exist.")
        return
    
    # making a list of audio files (path)
    try:
        audio_files = Find_Audio_Files(MUSIC_FOLDER)
    except OSError as Error:
        print(f"somthing went wrong (ERROR: {Error})")
        return
    
    if not audio_files:
        print("No Audio files were found")
        return
    
    # show audio files
    print("== MUSIC FILES ==")
    for i in range(len(audio_files)):
        print(i+1,') ',audio_files[i].name)

    while True:
        try: choice = int(input("Enter number to play: "))
        except:
            print("invaled input (try again)")
            continue

        if 0 < choice <= len(audio_files):
            selected_file = audio_files[choice-1]
            Play_Music(selected_file)
            break
        else:
            print("out of list (try again)")
            continue
        


### STARTING MUSIC BOX ###
if __name__ == "__main__":
    try:
        pygame.mixer.init()
        main()
    except pygame.error as Error:
        print(f"Could not initialize the Music (ERROR: {Error})")
    except OSError as Error:
            print(f"Could not initialize the Music (ERROR: {Error})")

    finally:
        pygame.mixer.quit()