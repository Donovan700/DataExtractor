from flask import Flask, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Charger le fichier XML
tree = ET.parse("messages-2023-08-30_000000-2023-08-30_235959.xml")
root = tree.getroot()

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = []
    for cwp_message in root.findall(".//cwp_message"):
        message_id = cwp_message.find(".//id").text
        channel_name = cwp_message.find(".//channelName").text
        # payload_type = cwp_message.find(".//payloadType").text
        message_type = cwp_message.find(".//messageType").text
        status = cwp_message.find(".//status").text
        creation_time = cwp_message.find(".//creationTime").text
        last_changed = cwp_message.find(".//lastChanged").text
        # Ajoutez d'autres données que vous souhaitez extraire
        message_data = {
            "message_id": message_id,
            "channel_name": channel_name,
            # "payload_type": payload_type,
            "message_type": message_type,
            "status": status,
            "creation_time": creation_time,
            "last_changed": last_changed
            # Ajoutez d'autres données ici
        }
        messages.append(message_data)
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
