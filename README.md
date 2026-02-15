## 📂 File Automation Script

A Python-based file organizer that automatically sorts files in the Downloads folder into categorized subfolders based on file extensions.

## 🚀 Overview

This script scans the user's Downloads directory and automatically moves files into organized folders such as:

Images
Applications
Documents
PDFs
Webpages
Presentations
Archives
Others

## It uses:

pathlib for path handling
shutil for file operations
Exception handling for safe execution

## 🛠 Features

Automatically detects file extensions
Moves files to categorized folders
Creates destination folders if they don’t exist
Handles common errors:
File not found
Permission errors
Unexpected system errors
Clean OOP-based structure

## 📁 Folder Structure Created

Inside the Downloads directory, the script organizes files into:

Downloads/
 ├── Images/
 ├── Applications/
 ├── Docs/
 ├── PPTs/
 ├── Webpages/
 ├── PDFs/
 ├── Archives/
 └── Others/

## 📌 Supported File Types

File Type	Destination Folder
.jpg, .png	Images
.apk, .exe	Applications
.pdf	PDFs
.html	Webpages
.pptx	PPTs
.docx	Docs
.zip	Archives
Other types	Others

## 🧠 How It Works

Sets Downloads folder as source.
Ensures required folders exist.
Iterates through files in Downloads.
Detects file extension.
Moves file to corresponding folder.
Handles errors safely without crashing.

## ▶️ How To Run

1️⃣ Clone the repository
git clone <your-repo-url>
2️⃣ Navigate into project folder
cd file-automation
3️⃣ Run the script
python file_automation.py

## ⚠️ Notes

The script only scans one level inside Downloads.
It ignores folders (only moves files).
Make sure no files are open while running the script.
Tested on Windows.

## 🧱 Built With

Python 3.x
pathlib
shutil

## 📈 Future Improvements

Add duplicate file handling
Add logging system
Add dry-run mode
Make extension rules configurable
Add recursive scanning

## 👨‍💻 Author

Medhansh
Built as part of a structured Python learning roadmap.