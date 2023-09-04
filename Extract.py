import xml.etree.ElementTree as ET
import openpyxl

def extract_data_from_xml(xml_file_path):
    try:
        # Parsez le fichier XML
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Liste pour stocker les données extraites
        extracted_data = []

        # Parcourez les éléments et extrayez les données
        for item in root.findall(".//cwp_message"):
            message_id = item.find(".//id").text
            channel_name = item.find(".//channelName").text
            payload_type = item.find(".//payloadType").text
            message_type = item.find(".//messageType").text
            status = item.find(".//status").text
            creation_time = item.find(".//creationTime").text
            last_changed = item.find(".//lastChanged").text
            extracted_data.append({"id": message_id,"channelName":channel_name,"payloadType":payload_type,"messageType":message_type,"status":status,"creationTime":creation_time,"lastChange":last_changed})

        return extracted_data
    except ET.ParseError:
        print("Erreur de parsing XML.")
        return None

def extract_data_from_excel(file_path, sheet_name):
    try:
        # Ouvrez le fichier Excel
        wb = openpyxl.load_workbook(file_path)

        # Sélectionnez la feuille de travail (worksheet) que vous souhaitez lire
        ws = wb[sheet_name]

        # Liste pour stocker les données extraites
        extracted_data = []

        # Parcourez les lignes et colonnes de la feuille de travail
        for row in ws.iter_rows(values_only=True):
            row_data = []
            for cell in row:
                row_data.append(cell)
            extracted_data.append(row_data)

        # Fermez le fichier Excel
        wb.close()

        return extracted_data
    except Exception as e:
        print("Erreur lors de l'extraction des données :", str(e))
        return None

if __name__ == '__main__':
    array = extract_data_from_xml("messages-2023-08-30_000000-2023-08-30_235959.xml")
    print(array[0])

    data = extract_data_from_excel("test.xlsx", "feuille1")
    if data:
        for row in data:
            print(row)
    else:
        print("Échec de l'extraction des données.")
