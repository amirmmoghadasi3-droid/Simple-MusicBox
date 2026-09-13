import customtkinter
from main import Play_Music
from pathlib import Path

def button_function(file: Path):
    play_error_massage = Play_Music(file)
    if not play_error_massage:
        del play_error_massage
    else:
        sub_Window(play_error_massage)


# sub window (for errors and massages)
def sub_Window(text: str):
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    sub_window = customtkinter.CTk()  # create sub window
    sub_window.geometry("600x400")

    sub_window.title("ERROR")
    textbox = customtkinter.CTkTextbox(master=sub_window, text_color="red")
    textbox.pack( padx=20, pady=20, fill="both", expand=True )

    textbox.insert(1.0, text=text)  
    textbox.configure(state="disabled")  # configure textbox to be read-only

    sub_window.mainloop()


# mainWindow program
def main_Window(files: list, mode, theme):

    customtkinter.set_appearance_mode(mode)  # Modes
    customtkinter.set_default_color_theme(theme)  # Themes

    main_window = customtkinter.CTk()  # create CTk window
    main_window.geometry("600x400")
    main_window.title("Music Box")

    # Scrollable frame
    scrollable_frame = customtkinter.CTkScrollableFrame(
        master=main_window,
        width=560,
        height=340
    )
    scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Create a button for every audio file
    for audio_file in files:
        file_name = audio_file.name if isinstance(audio_file, Path) else audio_file

        button = customtkinter.CTkButton(
            master=scrollable_frame,
            width=560,
            height=28,
            text=file_name,
            command=lambda file=audio_file: button_function(file)
        )
        button.pack(pady=5, padx=5, fill="x")


    main_window.mainloop()


# testing mainWindow
def test():
    files = ['test1.mp3', 'test2.wav', 'test3.mp3']
    main_Window(files, "dark", "dark-blue")

if __name__ == "__main__":
    test()
