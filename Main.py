import tkinter as tk
from Extract import extract_data_from_xml

fenetre = tk.Tk()
fenetre.title("Data extractor")
fenetre.geometry("1200x600")


# Fonction à exécuter lorsque le bouton est cliqué
def extract_me():
    try:
        Data = extract_data_from_xml("test.xml")
        # Affichez les données dans le label
        result_text = ""
        for item in Data:
            result_text += f"Produit : {item['id']}, Prix : {item['channelName']}, Type : {item['payloadType']}, Message : {item['messageType']}, Status : {item['status']}, Creation : {item['creationTime']}, Edited Date : {item['lastChange']}\n"
        
        result_label.config(text=result_text)
    except Exception as e:
        print(e)
        result_label.config(text=f"Erreur : {str(e)}")

def quit():
    try:
        fenetre.quit()
    except Exception as err:
        print(err)

def PrintText():
    try:
        elem = Input.get("1.0", "end-1c")
        result_label.config(text=str(elem))
    except Exception as e:
        print(e)

def ExtractIt():
    try:
        InputText = Input.get("1.0","end-1c")
        Data = extract_data_from_xml(InputText)
        result_text = ""
        for item in Data:
            result_text += f"Produit : {item['id']}, Prix : {item['channelName']}, Type : {item['payloadType']}, Message : {item['messageType']}, Status : {item['status']}, Creation : {item['creationTime']}, Edited Date : {item['lastChange']}\n"
        result_label.config(text=result_text)
    except Exception as error:
        print(error)
        result_label.config(text=f"Error with {str(PrintText)} : {str(error)}")

#Affichage dans le Frame
ExtractInputBtn = tk.Button(fenetre, text="Extract Input", command=ExtractIt)
result_label = tk.Label(fenetre, text="", wraplength=1000)
Input = tk.Text(fenetre, width=20, height=2)
GetBtn = tk.Button(fenetre, text="Print", command=PrintText)
extractBtn = tk.Button(fenetre, text="Extract", command=extract_me)
QuitBtn = tk.Button(fenetre, text="Quit", command=quit)
ExtractInputBtn.pack()
Input.pack()
GetBtn.pack()
extractBtn.pack()
QuitBtn.pack()
result_label.pack()

fenetre.mainloop()