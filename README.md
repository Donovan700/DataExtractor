# 🧾 XML Data Extractor GUI

This project is a simple Python GUI application that allows users to extract and display structured data from an XML file. It uses `Tkinter` for the interface and parses the XML using Python’s built-in `xml.etree.ElementTree`. The app can display XML data from a default file or from user input.

## 📂 Features

- 🔍 Load and parse XML data from a file (`test.xml`)
- ✍️ Extract XML content from a text area
- 🖥️ Display extracted data in a scrollable text box
- 🚫 Graceful error handling
- 💡 Simple and intuitive user interface

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/xml-extractor-gui.git
cd xml-extractor-gui
```
2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source venv/bin/activate  # On Windows: env\Scripts\activate
```
3. Install Dependencies
Make sure pip is up-to-date:

```bash
pip install --upgrade pip
```
Then install the required packages:

```bash
pip install -r requirements.txt
```
4. Run the Application
```bash
python Main.py
```
🧰 Requirements
The required Python packages are listed in requirements.txt. Main ones include:

tkinter (comes with Python standard library)

openpyxl (if you plan to export to Excel)

flask (if you plan to extend with a web API)

Extract.py (custom script to extract and structure XML data)

📁 Project Structure
graphql
.
├── Main.py               # Main entry point
├── Extract.py            # Custom XML parsing logic
├── test.xml              # Example XML file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🖼️ Interface Preview
(You can include a screenshot here if available)

💡 Usage
Launch the app.

Paste XML content or use the default file (test.xml).

Click on "Extract from input" or "Extract from 'test.xml'".

The result will be displayed in the output area.