## Different countries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import pyttsx3

# Sample data for friends, countries, and languages
friends_data = [{"name": "bot", "photo": "bot.jpg", "country": "Thailand", "language": "ไทย ", "greeting": "สุขสันต์วันเกิด (S̄uk̄hs̄ạnt̒ wạn keid)", "flag": "thailand_flag.jpg"},
    {"name": "hans", "photo": "hans.jpg", "country": "Germany", "language": "Deutsch", "greeting": "Alles Gute zum Geburtstag!", "flag": "germany_flag.jpg"},   
    {"name": "bhunf", "photo": "bhunf.jpg", "country": "China", "language": "简体中文", "greeting": "生日快乐 (Shēngrì kuàilè)", "flag": "china_flag.jpg"},  
    {"name": "kart", "photo": "kart.jpg", "country": "USA", "language": "English", "greeting": "Happy Birthday!", "flag": "usa_flag.jpg"},
    {"name": "ji", "photo": "ji.jpg", "country": "South Korea", "language": "한국어", "greeting": "생일 축하해요 (Saeng-il chugha haeyo)", "flag": "south_korea_flag.jpg"},
    {"name": "wei", "photo": "wei.jpg", "country": "Taiwan", "language": "繁體中文", "greeting": "生日快樂 (se lit khoai lok)", "flag": "taiwan_flag.jpg"},
    {"name": "louis", "photo": "louis.jpg", "country": "South Africa", "language": "Afrikaans", "greeting": "Gelukkige verjaarsdag!", "flag": "south_africa_flag.jpg"},
    {"name": "dong", "photo": "dong.jpg", "country": "Netherlands", "language": "Nederlands", "greeting": "Gefeliciteerd met je verjaardag!", "flag": "netherlands_flag.jpg"},
    {"name": "mei", "photo": "mei.jpg", "country": "Macau", "language": "粵式中文", "greeting": "生日快樂 (saang jat faai lok)", "flag": "macau_flag.jpg"},
    {"name": "indra", "photo": "indra.jpg", "country": "Indonesia", "language": " Bahasa Indonesia", "greeting": "Selamat ulang tahun!", "flag": "indonesia_flag.jpg"}
]

# Sample options for languages
language_options = ["한국어 "," Bahasa Indonesia", "English", "简体中文", "Afrikaans","繁體中文", "ไทย", "にほんご", "Nederlands","Español","粵式中文","Deutsch"]

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Country and Language Game")
        self.root.geometry("600x700")
        self.root.configure(bg="#ADD8E6")  # Change background color to light blue
        self.country_canvas = None
        self.language_canvas = None
        self.current_friend_index = 0
        self.score = 0
        self.selected_country = None
        self.selected_language = None
        
        self.engine = pyttsx3.init()  # 初始化语音引擎
        
        self.create_widgets()

    def create_widgets(self):
        self.name_label=tk.Label(self.root, text="Fill out your name:", bg="#ADD8E6", font=("Helvetica", 22))
        self.name_label.pack(pady=10,anchor='center')
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.name_entry.pack(pady=5, anchor='center')

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", font=("Helvetica", 16))
        self.start_button.pack(pady=10,anchor='center')

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("Input Error", "Please enter your name to start the game.")
            return

        self.start_button.pack_forget()
        self.name_entry.pack_forget()
        self.name_label.pack_forget()  # 隱藏 "Fill out your name" 標籤
        welcome_message = f"Welcome {self.player_name}!"
        self.welcome_label = tk.Label(self.root, text=welcome_message, bg="#ADD8E6", font=("Helvetica", 20, "bold"))
        self.welcome_label.pack(pady=10) # 歡迎寶寶
        
        self.condition_label = tk.Label(self.root, text="You need to get at least 70 points to win the prize :)", bg="#ADD8E6", font=("Helvetica", 16),fg="purple")
        self.condition_label.pack(pady=10)

        self.instructions_label = tk.Label(self.root, text="This game is designed to test how well you know your ten friends (some of whom might be really close to you). You need to identify their nationalities and the languages they speak. If you get both answers correct, you earn 10 points; otherwise, you get 0 points. The goal is to score above 70 points to win a special gift. If you don't reach 70 points, you'll need to try again to show more affection towards your friends. Good luck! 66666", bg="#ADD8E6", font=("Helvetica", 12), wraplength=500, justify="left")
        self.instructions_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_page, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.next_button.pack(pady=20)

    def next_page(self):
        self.welcome_label.pack_forget()
        self.condition_label.pack_forget()
        self.instructions_label.pack_forget()
        self.next_button.pack_forget()

        self.title_label = tk.Label(self.root, text="", bg="#ADD8E6", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.photo_label = tk.Label(self.root, bg="#ADD8E6")  # Change background color to light blue
        self.photo_label.pack(pady=10)

        tk.Label(self.root, text="Select Country:", bg="#ADD8E6", font=("Helvetica", 12)).pack()  # Change background color to light blue

        self.flag_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.flag_frame.pack(pady=5)

        for friend in friends_data:
            flag_image = Image.open(friend["flag"])
            flag_image = flag_image.resize((80, 48), Image.LANCZOS)
            flag_photo = ImageTk.PhotoImage(flag_image)
            flag_button = tk.Button(self.flag_frame, image=flag_photo, command=lambda f=friend:  [self.select_country(f), friend["canvas"].itemconfig("circle_fill", fill="green")])
            flag_button.image = flag_photo
            flag_button.pack(side=tk.LEFT, padx=10)

              # Add a canvas with a circle for selection indication
            canvas = tk.Canvas(self.flag_frame, width=15, height=15, bg="#ADD8E6")
            canvas.create_oval(2, 2, 12, 12,outline="black")
            canvas.create_oval(2, 2, 12, 12,tags="circle_fill")
            canvas.pack(side=tk.LEFT)

            friend["canvas"]=canvas

        tk.Label(self.root, text="Select Language:", bg="#ADD8E6", font=("Helvetica", 12)).pack()  # Change background color to light blue

        self.language_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.language_frame.pack(pady=5)

        for language in language_options:
            language_button = tk.Button(self.language_frame, text=language, command=lambda l=language: self.select_language(l), bg="#4CAF50", fg="white", font=("Helvetica", 10))
            language_button.pack(side=tk.LEFT, padx=10)

            # Add a canvas with a circle for selection indication
            canvas = tk.Canvas(self.language_frame, width=15, height=15, bg="#ADD8E6")
            canvas.create_oval(2, 2, 12, 12,outline="black")
            canvas.create_oval(2, 2, 12, 12,tags="circle_fill")
            canvas.pack(side=tk.LEFT)

            language_button.canvas = canvas
            language_button.config(command=lambda l=language, btn=language_button: [self.select_language(l), btn.canvas.itemconfig("circle_fill", fill="green")])
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.submit_button.pack(pady=20)

        self.greeting_label = tk.Label(self.root, bg="#ADD8E6", font=("Helvetica", 12))  # Label to display greeting in selected language
        self.greeting_label.pack(pady=5)

        self.load_friend()
       
     
    def hide_initial_labels(self):
        self.condition_label.pack_forget()
        self.instructions_label.pack_forget()

    def load_friend(self):
        friend = friends_data[self.current_friend_index]
        
        image = Image.open(friend["photo"])
        image = image.resize((550, 250), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.photo_label.config(image=photo)
        self.photo_label.image = photo

        self.title_label.config(text=f"How much do you know about {friend['name']}?",font=("Helvetica", 20, "bold"))

    def select_country(self, friend):
        self.selected_country = friend["country"]
        if self.country_canvas:
            self.country_canvas.delete("fill")
        self.country_canvas = friend["canvas"]
        self.country_canvas.create_oval(2, 2, 12, 12, fill="green", tags="fill")

    def select_language(self, language):
        self.selected_language = language
        if self.language_canvas:
            self.language_canvas.delete("fill")
        for btn in self.language_frame.winfo_children():
            if isinstance(btn, tk.Button) :
                  btn.canvas.delete("circle_fill")  # 清除之前的選擇
                  if btn.cget("text") == language:
                    self.language_canvas = btn.canvas
                    self.language_canvas.create_oval(2, 2, 12, 12, fill="green", tags="fill")
                    break
    
    def check_guess(self):
        correct_country =  friends_data[self.current_friend_index]["country"].strip().lower()
        correct_language = friends_data[self.current_friend_index]["language"].strip().lower()
        correct_greeting = friends_data[self.current_friend_index]["greeting"]

        # 標準化玩家的答案
        selected_country = self.selected_country.strip().lower()
        selected_language = self.selected_language.strip().lower()
        if selected_country == correct_country and selected_language == correct_language:
        
      
            messagebox.showinfo("Result", f"This is correct, Bao bao is so intelligent! {correct_greeting}")
            
            self.greeting_label.config(text=correct_greeting)
            self.score += 10
            
            # 使用语音引擎朗读生日快乐
            self.engine.setProperty('rate', 150)  # 語速
            self.engine.setProperty('volume', 1.0)  # 音量
            self.engine.say(correct_greeting)
            self.engine.runAndWait()
        else:
            messagebox.showinfo("Result", f"So sorry but the correct answer is {correct_country} and {correct_language}.")
        # 使用语音引擎朗读生日快乐
            self.engine.setProperty('rate', 150)  # 語速
            self.engine.setProperty('volume', 1.0)  # 音量
            self.engine.say(correct_greeting)
            self.engine.runAndWait()
        
        self.current_friend_index += 1
        
        if self.current_friend_index < len(friends_data):
            self.load_friend()
            self.greeting_label.config(text="")
            self.selected_language = None
            self.selected_country = None
        else:
            if self.score >= 70:
                messagebox.showinfo("GG Well Play", f" Your score is {self.score}/{len(friends_data) * 10}, You are so smarrrrt! Ready for the prize? Let's Gooo!!")
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            else:
                messagebox.showinfo("Game Over", f"Game Over! Your score is {self.score}/{len(friends_data) * 10}.")
                play_again = messagebox.askyesno("Play Again?", "Your score is below 70. Do you want to try again?")
            if play_again:
                self.reset_game()
            else:
                self.root.quit()

    def reset_game(self):
        self.current_friend_index = 0
        self.score = 0
        self.selected_country = None
        self.selected_language = None
        self.load_friend()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()