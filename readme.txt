TidyDLs - Download Organizer

TidyDLs is a utility application designed to automatically organize your Downloads folder by moving files into appropriate subfolders based on their file types. 

Features:
- Automatically monitors the Downloads folder for new files.
- Moves files into predefined subfolders such as Images, Documents, Music, Videos, Archives, Disk Images, Applications, 3D Print files, and Torrents.
- Ignores temporary (.tmp) files until they are fully downloaded.
- Ensures files are moved only when they are ready to avoid download interruptions.
- Handles file name conflicts by appending a counter to the file name.

Setup Instructions:
1. Ensure you have Python installed on your system.
2. Install the required Python package `watchdog` using pip:
	pip install watchdog
3. Place the TidyDLs script (`TidyDLs.py`) in a convenient location.

Usage Instructions:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the TidyDLs script.
3. Run the script using Python:
	python TidyDLs.py
4. The application will start monitoring your Downloads folder and automatically organize files as they are downloaded.

Customization:
- You can customize the file type to folder mapping by modifying the `file_types` dictionary in the script.

Example:
file_types = {
'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.html'],
'Music': ['.mp3', '.wav', '.aac'],
'Videos': ['.mp4', '.mkv', '.flv', '.avi'],
'Archives': ['.zip', '.rar', '.tar', '.gz'],
'Disk Image': ['.iso'],
'Application': ['.exe', '.msix', '.msi'],
'3D Print': ['.stl', '.3mf', '.dxf', '.f3d', '.step'],
'Torrent': ['.torrent']
}


Support:
- For issues or questions, please contact [info@sk4nk77.com].

Enjoy a clutter-free Downloads folder with TidyDLs!
