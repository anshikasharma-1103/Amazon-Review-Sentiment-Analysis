import customtkinter as ctk
import joblib
from tkinter import messagebox, filedialog
from datetime import datetime
import time
import threading
from trend_analysis import show_trends

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ==========================
# APP SETTINGS
# ==========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Amazon AI Review Analyzer")

app.geometry("1500x900")


# ==========================
# SCROLLABLE PAGE
# ==========================

scroll_frame = ctk.CTkScrollableFrame(
    app,
    fg_color="#0B1120"
)

scroll_frame.pack(fill="both", expand=True)
app.minsize(1400, 850)

# ==========================
# COLORS
# ==========================

BG = "#0B1120"
CARD = "#111827"
CARD2 = "#1F2937"
BLUE = "#2563EB"
GREEN = "#22C55E"
RED = "#EF4444"
YELLOW = "#FACC15"
TEXT = "#F8FAFC"

app.configure(fg_color=BG)

# ==========================
# HEADER
# ==========================

scroll_frame.pack(fill="both", expand=True)

header = ctk.CTkFrame(
    scroll_frame,
    height=90,
    fg_color=CARD,
    corner_radius=20
)

header.pack(fill="x", padx=20, pady=(20, 10))

loading_title = ctk.CTkLabel(
    header,
    text="🤖 AMAZON AI REVIEW ANALYZER",
    font=("Segoe UI", 30, "bold"),
    text_color=TEXT
)

loading_title.pack(pady=(12, 0))

subtitle = ctk.CTkLabel(
    header,
    text="Developed by Anshika Sharma",
    font=("Segoe UI", 15),
    text_color="lightgray"
)

subtitle.pack()

# ==========================
# NAVIGATION BAR
# ==========================

nav_frame = ctk.CTkFrame(
    header,
    fg_color="transparent"
)

nav_frame.pack(pady=(10,15))


home_btn = ctk.CTkButton(
    nav_frame,
    text="🏠 Home",
    width=120,
)

home_btn.pack(side="left", padx=8)


about_btn = ctk.CTkButton(
    nav_frame,
    text="ℹ About",
    width=120,
)

about_btn.pack(side="left", padx=8)


contact_btn = ctk.CTkButton(
    nav_frame,
    text="📞 Contact",
    width=120,
)

contact_btn.pack(side="left", padx=8)

# ==========================
# MAIN CONTAINER
# ==========================

main = ctk.CTkFrame(
    scroll_frame,
    fg_color=BG
)

main.pack(fill="both", expand=True, padx=20, pady=10)

# ==========================
# LEFT PANEL
# ==========================

left = ctk.CTkFrame(
    main,
    fg_color=CARD,
    corner_radius=20
)

left.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 12)
)

# ==========================
# RIGHT PANEL
# ==========================

right = ctk.CTkFrame(
    main,
    width=360,
    fg_color=CARD,
    corner_radius=20
)

right.pack(
    side="right",
    fill="y"
)

# ==========================
# REVIEW TITLE
# ==========================

review_title = ctk.CTkLabel(
    left,
    text="📝 ENTER PRODUCT REVIEW",
    font=("Segoe UI", 22, "bold")
)

review_title.pack(
    anchor="w",
    padx=25,
    pady=(20, 10)
)

# ==========================
# REVIEW TEXTBOX
# ==========================

textbox = ctk.CTkTextbox(
    left,
    height=280,
    font=("Consolas", 16),
    corner_radius=15
)

textbox.pack(
    fill="x",
    padx=25,
    pady=(0, 15)
)

textbox.insert(
    "1.0",
    "Type or paste your Amazon product review here..."
)

# ==========================
# BUTTON FRAME
# ==========================

button_frame = ctk.CTkFrame(
    left,
    fg_color="transparent"
)

button_frame.pack(
    fill="x",
    padx=20,
    pady=(0,15)
)

analyze_btn = ctk.CTkButton(
    button_frame,
    text="🔍 Analyze Review",
    width=180,
    height=45,
    fg_color=BLUE,
    font=("Segoe UI",16,"bold"),
)

analyze_btn.pack(side="left", padx=8)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=130,
    height=45,
    fg_color="#EF4444",
    hover_color="#EE9090",
    font=("Segoe UI",16,"bold"),
)

clear_btn.pack(side="left", padx=8)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=130,
    height=45,
    fg_color="#0EA5E9",
    hover_color="#3F5763",
    font=("Segoe UI",16,"bold"),
)

copy_btn.pack(side="left", padx=8)


save_btn = ctk.CTkButton(
    button_frame,
    text="💾 Save",
    width=130,
    height=45,
    fg_color="#22C55E",
    hover_color="#3F6C50",
    font=("Segoe UI",16,"bold"),
)

save_btn.pack(side="left", padx=8)

trend_btn = ctk.CTkButton(
    button_frame,
    text="📊 Analyze Trends",
    width=180,
    height=45,
    fg_color="#9333EA",
    hover_color="#81619D",
    command=show_trends
)

trend_btn.pack(side="left", padx=10)

# ==========================
# AI RESULT CARD
# ==========================

result_frame = ctk.CTkFrame(
    left,
    fg_color=CARD2,
    corner_radius=20,
    height=260
)

result_frame.pack(fill="x", padx=20, pady=(10,20))

result_title = ctk.CTkLabel(
    result_frame,
    text="📊 AI ANALYSIS RESULT",
    font=("Segoe UI",22,"bold")
)

result_title.pack(pady=(20,10))

emoji = ctk.CTkLabel(
    result_frame,
    text="🤖",
    font=("Segoe UI",60)
)

emoji.pack()

prediction = ctk.CTkLabel(
    result_frame,
    text="Waiting for Prediction...",
    font=("Segoe UI",30,"bold")
)

prediction.pack(pady=(5,5))

confidence = ctk.CTkLabel(
    result_frame,
    text="Confidence : -- %",
    font=("Segoe UI",18)
)

confidence.pack()

progress = ctk.CTkProgressBar(
    result_frame,
    width=520,
    height=15,
    progress_color=GREEN
)

progress.pack(pady=20)

progress.set(0)

# ==========================
# RIGHT PANEL
# ==========================

analytics_title = ctk.CTkLabel(
    right,
    text="📈 LIVE ANALYTICS",
    font=("Segoe UI",22,"bold")
)

analytics_title.pack(pady=(20,15))

analytics_card = ctk.CTkFrame(
    right,
    fg_color=CARD2,
    corner_radius=20
)

analytics_card.pack(fill="x",padx=15)

word_label = ctk.CTkLabel(
    analytics_card,
    text="📝 Words : 0",
    font=("Segoe UI",18)
)

word_label.pack(anchor="w",padx=20,pady=(15,8))

char_label = ctk.CTkLabel(
    analytics_card,
    text="🔠 Characters : 0",
    font=("Segoe UI",18)
)

char_label.pack(anchor="w",padx=20,pady=8)

reading_label = ctk.CTkLabel(
    analytics_card,
    text="📖 Reading Time : 0 sec",
    font=("Segoe UI",18)
)

reading_label.pack(anchor="w",padx=20,pady=8)

prediction_time = ctk.CTkLabel(
    analytics_card,
    text="⚡ Prediction Time : --",
    font=("Segoe UI",18)
)

prediction_time.pack(anchor="w",padx=20,pady=8)

accuracy = ctk.CTkLabel(
    analytics_card,
    text="🎯 Model Accuracy : 94%",
    font=("Segoe UI",18)
)

accuracy.pack(anchor="w",padx=20,pady=8)

dataset = ctk.CTkLabel(
    analytics_card,
    text="📦 Dataset : Amazon Fashion",
    font=("Segoe UI",18)
)

dataset.pack(anchor="w",padx=20,pady=(8,15))

# ==========================
# STATUS CARD
# ==========================

status_card = ctk.CTkFrame(
    right,
    fg_color=CARD2,
    corner_radius=20
)

status_card.pack(fill="x",padx=15,pady=20)

status_title = ctk.CTkLabel(
    status_card,
    text="SYSTEM STATUS",
    font=("Segoe UI",18,"bold")
)

status_title.pack(pady=(15,8))

status = ctk.CTkLabel(
    status_card,
    text="🟢 AI READY",
    text_color=GREEN,
    font=("Segoe UI",22,"bold")
)

status.pack(pady=(0,15))

# ==========================
# LIVE CLOCK
# ==========================

clock_card = ctk.CTkFrame(
    right,
    fg_color=CARD2,
    corner_radius=20
)

clock_card.pack(fill="x",padx=15)

clock_title = ctk.CTkLabel(
    clock_card,
    text="🕒 CURRENT TIME",
    font=("Segoe UI",18,"bold")
)

clock_title.pack(pady=(15,10))

clock = ctk.CTkLabel(
    clock_card,
    text="",
    font=("Consolas",20,"bold")
)

clock.pack()

date_label = ctk.CTkLabel(
    clock_card,
    text="",
    font=("Segoe UI",16)
)

date_label.pack(pady=(5,15))

def update_clock():

    now = datetime.now()

    clock.configure(
        text=now.strftime("%I:%M:%S %p")
    )

    date_label.configure(
        text=now.strftime("%d %B %Y")
    )

    app.after(1000,update_clock)

update_clock()

# ==========================
# HISTORY
# ==========================

history_title = ctk.CTkLabel(
    right,
    text="📜 RECENT PREDICTIONS",
    font=("Segoe UI",20,"bold")
)

history_title.pack(pady=(25,10))

history_box = ctk.CTkTextbox(
    right,
    height=180,
    corner_radius=15,
    font=("Segoe UI",14)
)

history_box.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0,15)
)

history_box.insert(
    "1.0",
    "Prediction history will appear here..."
)

history_box.configure(state="disabled")

# ==========================================
# LOAD MODEL (Already loaded? Keep only one.)
# ==========================================
# If you already loaded these in Part 1,
# DO NOT write these two lines again.
#
# model = joblib.load("review_model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")

# ==========================================
# UPDATE WORD & CHARACTER COUNT
# ==========================================

def update_statistics(event=None):

    text = textbox.get("1.0", "end-1c")

    words = len(text.split())

    characters = len(text)

    reading = max(1, round(words / 200 * 60))

    word_label.configure(
        text=f"📝 Words : {words}"
    )

    char_label.configure(
        text=f"🔠 Characters : {characters}"
    )

    reading_label.configure(
        text=f"📖 Reading Time : {reading} sec"
    )


textbox.bind("<KeyRelease>", update_statistics)


# ==========================================
# ANALYZE REVIEW
# ==========================================

def analyze_review():

    review = textbox.get("1.0", "end-1c").strip()

    if review == "":

        messagebox.showwarning(
            "Warning",
            "Please enter a product review."
        )

        return

    status.configure(
        text="🟡 ANALYZING...",
        text_color=YELLOW
    )

    app.update()

    start = time.time()

    review_vector = vectorizer.transform([review])

    prediction_result = model.predict(review_vector)[0]

    probability = model.predict_proba(review_vector).max()

    end = time.time()

    total_time = end - start

    prediction_time.configure(
        text=f"⚡ Prediction Time : {total_time:.4f} sec"
    )

    progress.set(0)

    def animate_progress(value=0):

       if value <= probability:

        progress.set(value)

        app.after(15, animate_progress, value+0.02)

    animate_progress()

    confidence.configure(
        text=f"Confidence : {probability*100:.2f}%"
    )

    if prediction_result == "Positive":

        emoji.configure(text="😊")

        prediction.configure(
            text="POSITIVE REVIEW",
            text_color=GREEN
        )

        result_frame.configure(
            fg_color="#063B2C"
        )

    else:

        emoji.configure(text="😞")

        prediction.configure(
            text="NEGATIVE REVIEW",
            text_color=RED
        )

        result_frame.configure(
            fg_color="#4A1010"
        )

    status.configure(
        text="🟢 COMPLETED",
        text_color=GREEN
    )

    update_history(review, prediction_result)


# ==========================================
# HISTORY
# ==========================================

history_data = []


def update_history(review, result):

    global history_data

    short_review = review[:45]

    if len(review) > 45:
        short_review += "..."

    icon = "😊" if result == "Positive" else "😞"

    history_data.insert(
        0,
        f"{icon} {result} | {short_review}"
    )

    history_data = history_data[:10]

    history_box.configure(state="normal")

    history_box.delete("1.0", "end")

    for item in history_data:

        history_box.insert(
            "end",
            item + "\n\n"
        )

    history_box.configure(state="disabled")


# ==========================================
# CLEAR
# ==========================================

def clear_review():

    textbox.delete("1.0", "end")

    emoji.configure(text="🤖")

    prediction.configure(
        text="Waiting for Prediction...",
        text_color="white"
    )

    confidence.configure(
        text="Confidence : -- %"
    )

    progress.set(0)

    result_frame.configure(
        fg_color=CARD2
    )

    word_label.configure(
        text="📝 Words : 0"
    )

    char_label.configure(
        text="🔠 Characters : 0"
    )

    reading_label.configure(
        text="📖 Reading Time : 0 sec"
    )

    prediction_time.configure(
        text="⚡ Prediction Time : --"
    )

    status.configure(
        text="🟢 AI READY",
        text_color=GREEN
    )


# ==========================================
# COPY RESULT
# ==========================================

def copy_result():

    result = prediction.cget("text")

    app.clipboard_clear()

    app.clipboard_append(result)

    messagebox.showinfo(
        "Copied",
        "Prediction copied to clipboard."
    )


# ==========================================
# SAVE RESULT
# ==========================================

def save_result():

    review = textbox.get("1.0", "end-1c")

    result = prediction.cget("text")

    confidence_text = confidence.cget("text")

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text File", "*.txt")
        ]
    )

    if file:

        with open(file, "w", encoding="utf-8") as f:

            f.write("AMAZON AI REVIEW ANALYZER\n\n")

            f.write("Review\n")
            f.write("-"*50 + "\n")
            f.write(review + "\n\n")

            f.write("Prediction\n")
            f.write("-"*50 + "\n")
            f.write(result + "\n")
            f.write(confidence_text)

        messagebox.showinfo(
            "Saved",
            "Prediction saved successfully."
        )

# ==========================================
# BUTTON COMMANDS
# ==========================================

analyze_btn.configure(
    command=analyze_review
)

clear_btn.configure(
    command=clear_review
)

copy_btn.configure(
    command=copy_result
)

save_btn.configure(
    command=save_result
)


# ==========================================
# PLACEHOLDER TEXT
# ==========================================

PLACEHOLDER = "Type or paste your Amazon product review here..."

def clear_placeholder(event):
    if textbox.get("1.0", "end-1c") == PLACEHOLDER:
        textbox.delete("1.0", "end")

def restore_placeholder(event):
    if textbox.get("1.0", "end-1c").strip() == "":
        textbox.insert("1.0", PLACEHOLDER)

textbox.bind("<FocusIn>", clear_placeholder)
textbox.bind("<FocusOut>", restore_placeholder)

# ==========================================
# KEYBOARD SHORTCUTS
# ==========================================

app.bind("<Control-Return>", lambda e: analyze_review())
app.bind("<Escape>", lambda e: clear_review())

# ==========================================
# FOOTER
# ==========================================

footer = ctk.CTkFrame(
    scroll_frame,
    height=45,
    fg_color=CARD,
    corner_radius=15
)

footer.pack(fill="x", padx=20, pady=(0,15))

footer_label = ctk.CTkLabel(
    footer,
    text="Amazon AI Review Analyzer  |  Machine Learning Project  |  Developed by Anshika Sharma",
    font=("Segoe UI",14)
)

footer_label.pack(pady=10)

# ==========================================
# STARTUP ANIMATION
# ==========================================

status.configure(
    text="🟡 INITIALIZING AI...",
    text_color=YELLOW
)

app.update()

app.after(
    1200,
    lambda: status.configure(
        text="🟢 AI READY",
        text_color=GREEN
    )
)

# ==========================================
# HOVER EFFECTS
# ==========================================

def hover_blue(e):
    analyze_btn.configure(fg_color="#1D4ED8")

def leave_blue(e):
    analyze_btn.configure(fg_color=BLUE)

analyze_btn.bind("<Enter>", hover_blue)
analyze_btn.bind("<Leave>", leave_blue)

def hover_red(e):
    clear_btn.configure(fg_color="#DC2626")

def leave_red(e):
    clear_btn.configure(fg_color=RED)

clear_btn.bind("<Enter>", hover_red)
clear_btn.bind("<Leave>", leave_red)

def hover_green(e):
    save_btn.configure(fg_color="#16A34A")

def leave_green(e):
    save_btn.configure(fg_color=GREEN)

save_btn.bind("<Enter>", hover_green)
save_btn.bind("<Leave>", leave_green)

# ==========================================
# WINDOW ICON (OPTIONAL)
# ==========================================

# app.iconbitmap("icon.ico")

# ==========================================
# INITIAL STATISTICS
# ==========================================

update_statistics()


# ==========================
# NAVIGATION FUNCTIONS
# ==========================

def home_page():
    app.focus_force()
    textbox.focus_set()


def about_project():

    about = ctk.CTkToplevel(app)
    about.title("About Project")
    about.geometry("700x550")
    about.resizable(False, False)

    about.configure(fg_color="#0B1120")

    title = ctk.CTkLabel(
        about,
        text="🤖 AMAZON AI REVIEW ANALYZER",
        font=("Segoe UI", 26, "bold"),
        text_color="white"
    )
    title.pack(pady=(20,10))

    info = """
Project Description

Amazon AI Review Analyzer is a Machine Learning based desktop
application that analyzes Amazon product reviews.

The system predicts whether a customer review is:

• 😊 Positive
• 😞 Negative

It also provides:

✔ Confidence Score
✔ Estimated Star Rating
✔ Review Statistics
✔ Prediction History
✔ Trend Analysis (Bar Chart & Pie Chart)
✔ Live Analytics Dashboard

Technologies Used

• Python
• CustomTkinter
• Scikit-Learn
• Pandas
• Matplotlib
• Joblib

Machine Learning Model

• TF-IDF Vectorizer
• Multinomial Naive Bayes Classifier

Dataset

Amazon Fashion Product Reviews

Objective

To help customers and businesses understand
customer opinions by automatically analyzing
product reviews using Artificial Intelligence.

Developed By

Anshika Sharma
"""

    textbox = ctk.CTkTextbox(
        about,
        width=630,
        height=350,
        font=("Segoe UI",15)
    )

    textbox.pack(padx=20, pady=10)

    textbox.insert("1.0", info)

    textbox.configure(state="disabled")

    close_btn = ctk.CTkButton(
        about,
        text="Close",
        width=140,
        command=about.destroy
    )

    close_btn.pack(pady=20)


def contact_us():

    contact = ctk.CTkToplevel(app)
    contact.title("Contact")
    contact.geometry("650x500")
    contact.resizable(False, False)

    contact.configure(fg_color="#0B1120")

    # ==========================
    # TITLE
    # ==========================

    title = ctk.CTkLabel(
        contact,
        text="📞 CONTACT INFORMATION",
        font=("Segoe UI", 26, "bold"),
        text_color="white"
    )

    title.pack(pady=(20,15))

    # ==========================
    # CONTACT DETAILS
    # ==========================

    info = """
👩‍💻 Developer

Anshika Sharma

📧 Email

anshika_email@gmail.com


💻 Technologies Used

• Python
• CustomTkinter
• Machine Learning
• Scikit-Learn
• Pandas
• Matplotlib


🤖 Project

Amazon AI Review Analyzer



🙏 Thank You for using this project!
"""

    textbox = ctk.CTkTextbox(
        contact,
        width=560,
        height=300,
        font=("Segoe UI",16)
    )

    textbox.pack(padx=20, pady=10)

    textbox.insert("1.0", info)

    textbox.configure(state="disabled")

    # ==========================
    # CLOSE BUTTON
    # ==========================

    close_btn = ctk.CTkButton(
        contact,
        text="Close",
        width=150,
        command=contact.destroy
    )

    close_btn.pack(pady=20)

# ==========================================
# CONNECT BUTTONS
# ==========================================

home_btn.configure(command=home_page)

about_btn.configure(command=about_project)

contact_btn.configure(command=contact_us)

analyze_btn.configure(command=analyze_review)

clear_btn.configure(command=clear_review)

copy_btn.configure(command=copy_result)

save_btn.configure(command=save_result)


# Smooth Fade In Animation
app.attributes("-alpha", 0)

def fade_in(alpha=0):
    if alpha < 1:
        alpha += 0.05
        app.attributes("-alpha", alpha)
        app.after(25, fade_in, alpha)

fade_in()

# =====================================
# LOADING SCREEN
# =====================================

loading = ctk.CTkToplevel()

loading.geometry("500x300")

loading.title("Loading")

loading.configure(fg_color="#0B1120")

loading.resizable(False, False)

loading.grab_set()

title = ctk.CTkLabel(
    loading,
    text="🤖 AMAZON AI REVIEW ANALYZER",
    font=("Segoe UI",24,"bold")
)

title.pack(pady=(40,20))

loading_text = ctk.CTkLabel(
    loading,
    text="Loading AI Model...",
    font=("Segoe UI",18)
)

loading_text.pack()

loading_progress = ctk.CTkProgressBar(
    loading,
    width=350
)

loading_progress.pack(pady=25)

loading_progress.set(0)

percent = ctk.CTkLabel(
    loading,
    text="0%",
    font=("Segoe UI",16)
)

percent.pack()

def load():

    for i in range(101):

        loading_progress.set(i/100)

        percent.configure(text=f"{i}%")

        loading.update()

        time.sleep(0.02)

    loading.destroy()

    app.deiconify()

threading.Thread(target=load).start()



# ==========================================
# RUN APPLICATION
# ==========================================

app.mainloop()