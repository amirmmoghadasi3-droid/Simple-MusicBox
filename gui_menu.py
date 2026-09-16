import customtkinter
from main import Play_Music
from pathlib import Path


def button_function(file: Path, parent: customtkinter.CTk):
    play_error_message = Play_Music(file)
    if not play_error_message:
        # nothing went wrong, nothing to show
        pass
    else:
        sub_Window(parent, play_error_message)


# sub window (for errors and messages)
def sub_Window(parent: customtkinter.CTk, text: str):

    COLOR_TEXTBOX_BG = "white"
    COLOR_BORDER = "white"
    COLOR_BG = "white"

    sub_window = customtkinter.CTkToplevel(parent)  # child window
    sub_window.geometry("600x400")
    sub_window.title("ERROR")
    sub_window.configure(fg_color=COLOR_BG)

    # keep it tied to the main window
    sub_window.transient(parent)
    sub_window.grab_set()

    textbox = customtkinter.CTkTextbox(
        master=sub_window,
        fg_color=COLOR_TEXTBOX_BG,
        text_color="red",
        border_color=COLOR_BORDER,
        border_width=1)
    textbox.pack(padx=20, pady=20, fill="both", expand=True)

    textbox.insert("1.0", text)
    textbox.configure(state="disabled")  # read-only



# mainWindow program
def main_Window(files: list, mode, theme):

    customtkinter.set_appearance_mode(mode)        
    customtkinter.set_default_color_theme(theme)   

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
            command=lambda file=audio_file: button_function(file, main_window)
        )
        button.pack(pady=5, padx=5, fill="x")

    main_window.mainloop()


# testing mainWindow
def test():
    files = ['test1.mp3', 'test2.wav', 'test3.mp3']
    main_Window(files, "dark", "dark-blue")


if __name__ == "__main__":
    test()
