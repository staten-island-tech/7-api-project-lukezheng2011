import requests
import tkinter as tk

def get_character_house(character_name):
    response = requests.get("https://hp-api.onrender.com/api/characters")
    if response.status_code != 200:
        return None

    data = response.json()

    for character in data:
        if character["name"].lower() == character_name.lower():
            house = character["house"]
            if house:
                return house
            else:
                return "Invalid Character"

def find_house():
    name = entry.get().strip()
    if not name:
        result_label.config(text="Please enter a character name")
        return

    house = get_character_house(name)
    result_label.config(text=f"House: {house}")



window = tk.Tk()
window.title("Harry Potter Houses")
window.geometry("400x250")
window.resizable(False, False)

prompt = tk.Label(
    window,
    text="Enter a Harry Potter character's name:",
    font=("Times New Roman", 15)
)
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Times New Roman", 15), width=30)
entry.pack(pady=5)

result_label = tk.Label(
    window,
    text="",
    font=("Times New Roman", 15, "bold"),
    fg="blue"
)
result_label.pack(pady=15)

search_button = tk.Button(
    window,
    text="Find House",
    font=("Arial", 15),
    command=find_house
)
search_button.pack(pady=10)

window.mainloop()