import tkinter as tk
from tkinter import ttk
from Extract import extract_data_from_xml

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Data Extractor")
fenetre.geometry("1200x700")
fenetre.configure(bg="#f4f4f4")

# ---------- Fonctions ----------

def extract_me():
    try:
        data = extract_data_from_xml("test.xml")
        result_text = ""
        for item in data:
            result_text += (
                f"Produit : {item['id']}\n"
                f"Prix : {item['channelName']}\n"
                f"Type : {item['payloadType']}\n"
                f"Message : {item['messageType']}\n"
                f"Status : {item['status']}\n"
                f"Création : {item['creationTime']}\n"
                f"Dernière modification : {item['lastChange']}\n"
                "----------------------------------------\n"
            )
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, result_text)
    except Exception as e:
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, f"Erreur : {str(e)}")


def quit_app():
    fenetre.quit()


def print_text():
    try:
        elem = input_textbox.get("1.0", "end-1c")
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, str(elem))
    except Exception as e:
        result_textbox.insert(tk.END, f"Erreur : {str(e)}")


def extract_from_input():
    try:
        input_data = input_textbox.get("1.0", "end-1c")
        data = extract_data_from_xml(input_data)
        result_text = ""
        for item in data:
            result_text += (
                f"Produit : {item['id']}\n"
                f"Prix : {item['channelName']}\n"
                f"Type : {item['payloadType']}\n"
                f"Message : {item['messageType']}\n"
                f"Status : {item['status']}\n"
                f"Création : {item['creationTime']}\n"
                f"Dernière modification : {item['lastChange']}\n"
                "----------------------------------------\n"
            )
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, result_text)
    except Exception as error:
        result_textbox.insert(tk.END, f"Erreur : {str(error)}")

# ---------- UI Layout ----------

# Section Input
input_frame = tk.LabelFrame(fenetre, text="Input XML File Path or Content", bg="#f4f4f4", padx=10, pady=10)
input_frame.pack(fill="x", padx=20, pady=10)

input_textbox = tk.Text(input_frame, height=3, font=("Arial", 12))
input_textbox.pack(fill="x", expand=True)

# Section des boutons
button_frame = tk.Frame(fenetre, bg="#f4f4f4")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Extract from 'test.xml'", command=extract_me, width=20, bg="#FFD700").pack(side="left", padx=10)
tk.Button(button_frame, text="Extract from input", command=extract_from_input, width=20, bg="#90EE90").pack(side="left", padx=10)
tk.Button(button_frame, text="Show Input Text", command=print_text, width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="Quit", command=quit_app, width=10, bg="#FF7F7F").pack(side="left", padx=10)

# Section Résultat
result_frame = tk.LabelFrame(fenetre, text="Results", bg="#f4f4f4", padx=10, pady=10)
result_frame.pack(fill="both", expand=True, padx=20, pady=10)

result_textbox = tk.Text(result_frame, wrap="word", font=("Courier", 11))
result_textbox.pack(fill="both", expand=True)

# Lancer l'application
fenetre.mainloop()
