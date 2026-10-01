import customtkinter as ctk
from PIL import Image, ImageTk

class AuthApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Auth App")
        self.geometry("1280x720")
        self.minsize(900, 600)
        self.configure(fg_color="#f4f4f4")

        # Background image
        try:
            bg = Image.open("background.png").resize((1280, 720))
            self.bg_image = ImageTk.PhotoImage(bg)
            self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Background image not found: {e}")
            self.configure(fg_color="#eaeaea")

        # Centered white form container
        self.form_frame = ctk.CTkFrame(
            self,
            width=440,
            height=560,
            corner_radius=24,
            fg_color="white"
        )
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login screen
        self.login_frame = ctk.CTkFrame(
            self.form_frame,
            width=360,
            height=500,
            fg_color="white",
            corner_radius=18
        )
        self.login_frame.pack_propagate(False)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.login_title = ctk.CTkLabel(
            self.login_frame,
            text="Welcome Back",
            font=("Arial", 28, "bold"),
            text_color="#1a1a1a"
        )
        self.login_title.pack(pady=(30, 5))

        self.login_subtitle = ctk.CTkLabel(
            self.login_frame,
            text="Sign in to continue",
            font=("Arial", 13),
            text_color="#585858"
        )
        self.login_subtitle.pack(pady=(0, 20))

        self.login_username = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=42,
            placeholder_text="Username",
            font=("Arial", 15),
            border_color="#d9d9d9",
            fg_color="white",
            text_color="#111111"
        )
        self.login_username.pack(pady=(10, 12))

        self.login_password = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=42,
            placeholder_text="Password",
            show="*",
            font=("Arial", 15),
            border_color="#d9d9d9",
            fg_color="white",
            text_color="#111111"
        )
        self.login_password.pack(pady=(0, 18))

        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            width=300,
            height=44,
            corner_radius=12,
            fg_color="#3a86ff",
            hover_color="#2d72da",
            font=("Arial", 16, "bold"),
            command=self.handle_login
        )
        self.login_button.pack(pady=(0, 16))

        self.signup_prompt = ctk.CTkLabel(
            self.login_frame,
            text="Don't have an account?",
            font=("Arial", 12),
            text_color="#555555"
        )
        self.signup_prompt.pack(pady=(6, 0))

        self.to_register_button = ctk.CTkButton(
            self.login_frame,
            text="Sign up",
            width=120,
            height=30,
            fg_color="transparent",
            text_color="#3a86ff",
            hover_color="#eef4ff",
            border_width=0,
            font=("Arial", 12, "bold"),
            command=self.show_register
        )
        self.to_register_button.pack(pady=(2, 25))

        # Register screen
        self.register_frame = ctk.CTkFrame(
            self.form_frame,
            width=360,
            height=500,
            fg_color="white",
            corner_radius=18
        )
        self.register_frame.pack_propagate(False)
        self.register_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.register_frame.pack_forget()

        self.register_title = ctk.CTkLabel(
            self.register_frame,
            text="Create Account",
            font=("Arial", 28, "bold"),
            text_color="#1a1a1a"
        )
        self.register_title.pack(pady=(30, 5))

        self.register_subtitle = ctk.CTkLabel(
            self.register_frame,
            text="Register your account",
            font=("Arial", 13),
            text_color="#585858"
        )
        self.register_subtitle.pack(pady=(0, 20))

        self.register_username = ctk.CTkEntry(
            self.register_frame,
            width=300,
            height=42,
            placeholder_text="Username",
            font=("Arial", 15),
            border_color="#d9d9d9",
            fg_color="white",
            text_color="#111111"
        )
        self.register_username.pack(pady=(10, 12))

        self.register_password = ctk.CTkEntry(
            self.register_frame,
            width=300,
            height=42,
            placeholder_text="Password",
            show="*",
            font=("Arial", 15),
            border_color="#d9d9d9",
            fg_color="white",
            text_color="#111111"
        )
        self.register_password.pack(pady=(0, 18))

        self.register_button = ctk.CTkButton(
            self.register_frame,
            text="Register",
            width=300,
            height=44,
            corner_radius=12,
            fg_color="#3a86ff",
            hover_color="#2d72da",
            font=("Arial", 16, "bold"),
            command=self.handle_register
        )
        self.register_button.pack(pady=(0, 16))

        self.login_prompt = ctk.CTkLabel(
            self.register_frame,
            text="Already have an account?",
            font=("Arial", 12),
            text_color="#555555"
        )
        self.login_prompt.pack(pady=(6, 0))

        self.to_login_button = ctk.CTkButton(
            self.register_frame,
            text="Login",
            width=120,
            height=30,
            fg_color="transparent",
            text_color="#3a86ff",
            hover_color="#eef4ff",
            border_width=0,
            font=("Arial", 12, "bold"),
            command=self.show_login
        )
        self.to_login_button.pack(pady=(2, 25))

        # Welcome screen
        self.welcome_frame = ctk.CTkFrame(
            self.form_frame,
            width=360,
            height=500,
            fg_color="white",
            corner_radius=18
        )
        self.welcome_frame.pack_propagate(False)
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.welcome_frame.pack_forget()

        self.welcome_title = ctk.CTkLabel(
            self.welcome_frame,
            text="Welcome!",
            font=("Arial", 32, "bold"),
            text_color="#1a1a1a"
        )
        self.welcome_title.pack(pady=(60, 20))

        self.welcome_message = ctk.CTkLabel(
            self.welcome_frame,
            text="You have successfully logged in",
            font=("Arial", 14),
            text_color="#585858"
        )
        self.welcome_message.pack(pady=(0, 10))

        self.welcome_username = ctk.CTkLabel(
            self.welcome_frame,
            text="",
            font=("Arial", 16, "bold"),
            text_color="#3a86ff"
        )
        self.welcome_username.pack(pady=(0, 60))

        self.logout_button = ctk.CTkButton(
            self.welcome_frame,
            text="Logout",
            width=300,
            height=44,
            corner_radius=12,
            fg_color="#ff6b6b",
            hover_color="#e63946",
            font=("Arial", 16, "bold"),
            command=self.logout
        )
        self.logout_button.pack(pady=(0, 20))

        self.show_login()

    def show_login(self):
        self.register_frame.place_forget()
        self.welcome_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_register(self):
        self.login_frame.place_forget()
        self.welcome_frame.place_forget()
        self.register_frame.place(relx=0.5, rely=0.5, anchor="center")

    def handle_login(self):
        username = self.login_username.get()
        if username.strip():
            self.welcome_username.configure(text=f"@{username}")
            self.login_frame.place_forget()
            self.register_frame.place_forget()
            self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.login_username.delete(0, "end")
            self.login_password.delete(0, "end")
        else:
            # Show error or just proceed
            self.welcome_username.configure(text="User")
            self.login_frame.place_forget()
            self.register_frame.place_forget()
            self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.login_username.delete(0, "end")
            self.login_password.delete(0, "end")

    def handle_register(self):
        username = self.register_username.get()
        if username.strip():
            self.welcome_username.configure(text=f"@{username}")
            self.register_frame.place_forget()
            self.login_frame.place_forget()
            self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.register_username.delete(0, "end")
            self.register_password.delete(0, "end")
        else:
            self.welcome_username.configure(text="User")
            self.register_frame.place_forget()
            self.login_frame.place_forget()
            self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.register_username.delete(0, "end")
            self.register_password.delete(0, "end")

    def logout(self):
        self.show_login()


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = AuthApp()
    app.mainloop()
