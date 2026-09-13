from main import Find_Audio_Files, main_final, main_init, MUSIC_FOLDER
from mainWindow import main_Window, sub_Window

init_error_massage = main_init()

if not init_error_massage:
    del init_error_massage
else:
    sub_Window(init_error_massage)

# check if test folder exist
if not MUSIC_FOLDER.is_dir():
    sub_Window(f"Folder '{MUSIC_FOLDER}' dose not exist.")

# making a list of audio files (path)
try:
    audio_files = Find_Audio_Files(MUSIC_FOLDER)
except OSError as Error:
    sub_Window(f"somthing went wrong (ERROR: {Error})")

if not audio_files:
    sub_Window("No Audio files were found")

main_Window(audio_files, "dark", "dark-blue")


main_final()