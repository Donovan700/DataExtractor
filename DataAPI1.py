import xml.etree.ElementTree as ET


tree = ET.parse("messages-2023-08-30_000000-2023-08-30_235959.xml")
root = tree.getroot()

def getAll():
    try:
        Array = []
        for cwp_message in root.findall(".//cwp_message"):
            # message_id = cwp_message.find(".//id").text
            # channel_name = cwp_message.find(".//channelName").text
            # payload_type = cwp_message.find(".//payloadType").text
            # message_type = cwp_message.find(".//messageType").text
            # status = cwp_message.find(".//status").text
            creation_time = cwp_message.find(".//creationTime").text
            # last_changed = cwp_message.find(".//lastChanged").text
            Array.append(creation_time)
        return Array
    except Exception as error:
        print("Error: ",error)


if __name__ == '__main__':
    tab = getAll()
    print(tab)

#     print(f"ID du message : {message_id}")
#     print(f"Nom du canal : {channel_name}")
#     print(f"Type de payload : {payload_type}")
#     print(f"Type de message : {message_type}")
#     print(f"Statut : {status}")
#     print(f"Heure de création : {creation_time}")
#     print(f"Heure de modification : {last_changed}")
#     print("\n")
