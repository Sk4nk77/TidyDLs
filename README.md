
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

'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.ico', '.webp', '.psd'],

'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xlsm', '.xlsb', '.pptx', '.csv', '.html', '.odt', '.rtf', '.md', '.ppt', '.xls', '.epub'],

'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff'],

'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.webm', '.mpeg', '.mpg'],

'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz'],

'Disk Image': ['.iso', '.img', '.vmdk', '.bin', '.cue', '.dmg', '.vhd'],

'Application': ['.exe', '.msix', '.msi', '.apk', '.bat', '.com', '.jar', '.cmd', '.gadget'],

'3D Print': ['.stl', '.3mf', '.dxf', '.f3d', '.step', '.obj', '.iges'],

'Torrent': ['.torrent']
}

Setting Up a Scheduled Task to Run TidyDLs Automatically:
1. Create a Batch File:
   - Open a text editor and paste the following line:
     ```
     python "C:\path\to\your\TidyDLs.py"
     ```
   - Save this file with a `.bat` extension, e.g., `run_tidyDLs.bat`.

2. Open Task Scheduler:
   - Press `Windows + S` and type `Task Scheduler`, then press `Enter`.

3. Create a New Task:
   - In Task Scheduler, click on `Create Basic Task...` in the right-hand panel.
   - Name the task (e.g., "Run TidyDLs") and provide a description.
   - Click `Next`.

4. Set the Trigger:
   - Choose when you want the task to start. For continuous monitoring, select `When the computer starts` or `When I log on`.
   - Click `Next`.

5. Set the Action:
   - Select `Start a program` and click `Next`.
   - Click `Browse` and navigate to the batch file you created earlier (`run_tidyDLs.bat`).
   - Click `Next`.

6. Finish the Task Setup:
   - Review the settings and click `Finish`.

7. Configure Task Properties (Optional but Recommended):
   - Find your task in the Task Scheduler Library, right-click it, and select `Properties`.
   - In the `General` tab, select `Run whether user is logged on or not` and `Run with highest privileges`.
   - In the `Settings` tab, make sure `Allow task to be run on demand` is checked.
   - Click `OK`.

Support:
- For issues or questions, please contact [info@sk4nk77.com].

Enjoy a clutter-free Downloads folder with TidyDLs!
