import tkinter as tk
import customtkinter as ctk
from Game_2048 import *

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Dark or Light mode
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class GameMenu(ctk.CTk):
    def __init__(self, title="Game Menu", size="1200x800", fullscreen=False):
        super().__init__()

        # Store fullscreen state
        self.fullscreen = fullscreen

        # Get screen resolution if fullscreen is enabled
        if self.fullscreen:
            self.screen_width = self.winfo_screenwidth()  # Get screen width
            self.screen_height = self.winfo_screenheight()  # Get screen height
            size = f"{self.screen_width}x{self.screen_height}"  # Set window size
            self.geometry(size)
        else:
            self.geometry(size)  # Use provided size if not fullscreen

        # Window settings
        self.title(title)
        self.resizable(True, True)
        self.attributes("-fullscreen", self.fullscreen)

        # Make Window Active on Launch
        self.lift()           # Bring window to front
        self.focus_force()    # Force focus on the window

        # Background Frame (Full Screen)
        self.main_frame = ctk.CTkFrame(self, fg_color="#2a2d2e")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Bind the Escape key to quit
        self.bind("<Escape>", self.quit_game)

        # Game Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, text=title, font=("Arial", 80, "bold"), text_color="white"
        )
        self.title_label.place(relx=0.5, rely=0.15, anchor="center")

        # Play Button
        self.play_button = ctk.CTkButton(self.main_frame, text="Play", font=("Arial", 24), command=self.start_game)
        self.play_button.place(relx=0.5, rely=0.4, anchor="center")

        # Options Button (Optional)
        self.options_button = ctk.CTkButton(self.main_frame, text="Options", font=("Arial", 20), command=self.show_options)
        self.options_button.place(relx=0.5, rely=0.55, anchor="center")

        # Quit Button
        self.quit_button = ctk.CTkButton(self.main_frame, text="Quit", font=("Arial", 20), fg_color="red", hover_color="#8b0000", command=self.quit_game)
        self.quit_button.place(relx=0.5, rely=0.70, anchor="center")

        # Credits Button
        self.credits_button = ctk.CTkButton(self.main_frame, text="Credits", font=("Arial", 20), command=self.show_credits)
        self.credits_button.place(relx=0.1, rely=0.95, anchor="center")

        # High Scores Button
        self.highscores_button = ctk.CTkButton(self.main_frame, text="High Scores", font=("Arial", 20), command=self.show_highscores)
        self.highscores_button.place(relx=0.9, rely=0.95, anchor="center")

        # Fullscreen Toggle
        self.fullscreen_var = tk.BooleanVar(value=self.fullscreen)
        self.fullscreen_toggle = ctk.CTkSwitch(self.main_frame, text="Fullscreen", variable=self.fullscreen_var, command=self.toggle_fullscreen)
        self.fullscreen_toggle.place(relx=0.5, rely=0.95, anchor="center")

        # Bind resize event for responsiveness
        self.bind("<Configure>", self.on_resize)

    def start_game(self):
        game(self.winfo_width(), self.winfo_height())

    def show_options(self):
        print("Opening options... (Expand this later)")

    def quit_game(self, event=None):  # Accept event parameter for Escape key
        self.destroy()

    def show_credits(self):
        print("Bah y'a que moi quoi")

    def show_highscores(self):
        print("t'es un champion")

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)
        if self.fullscreen:
            self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        else:
            self.geometry("1200x800")

    def on_resize(self, event):
        """Adjusts button sizes dynamically when window resizes."""
        width = self.winfo_width()
        height = self.winfo_height()

        # Adjust button sizes based on window size
        button_width = int(width * 0.3)  # 30% of window width
        button_height = int(height * 0.12)  # 12% of window height

        self.play_button.configure(width = button_width, height = button_height, corner_radius = button_height // 3)
        self.options_button.configure(width = button_width * 0.95, height = button_height, corner_radius = button_height // 3)
        self.quit_button.configure(width = button_width * 0.90, height = button_height, corner_radius = button_height // 3)
        self.credits_button.configure(width = button_width // 2, height = button_height // 2, corner_radius = button_height // 6)
        self.highscores_button.configure(width = button_width // 2, height = button_height // 2, corner_radius = button_height // 6)

MainMenu = GameMenu(title="2048", size="1200x800")
MainMenu.mainloop()
