import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the mapping of file types to folders
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

# Define the Downloads folder path dynamically
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.files_to_move = {}

    def on_created(self, event):
        if not event.is_directory:
            print(f"TidyDLs: File created: {event.src_path}")
            self.files_to_move[event.src_path] = time.time()

    def on_modified(self, event):
        if not event.is_directory:
            print(f"TidyDLs: File modified: {event.src_path}")
            self.files_to_move[event.src_path] = time.time()

    def check_files_to_move(self):
        current_time = time.time()
        for file_path, last_modified in list(self.files_to_move.items()):
            if current_time - last_modified > 5:  # 5 seconds threshold
                self.move_file(file_path)
                del self.files_to_move[file_path]

    def move_file(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()
        print(f"TidyDLs: File extension: {file_extension}")

        if file_extension == '.tmp':
            print(f"TidyDLs: Ignoring temporary file: {file_path}")
            return

        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(downloads_folder, folder)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                destination_path = os.path.join(destination_folder, os.path.basename(file_path))
                destination_path = self.get_unique_destination(destination_path)

                try:
                    shutil.move(file_path, destination_path)
                    print(f"TidyDLs: Moved: {file_path} to {destination_path}")
                except Exception as e:
                    print(f"TidyDLs: Failed to move {file_path}: {e}")
                break
        else:
            print(f"TidyDLs: No matching folder for file extension: {file_extension}")

    def get_unique_destination(self, destination_path):
        base, extension = os.path.splitext(destination_path)
        counter = 1
        while os.path.exists(destination_path):
            destination_path = f"{base} ({counter}){extension}"
            counter += 1
        return destination_path

def move_existing_files():
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        if os.path.isfile(item_path):
            _, file_extension = os.path.splitext(item_path)
            file_extension = file_extension.lower()

            if file_extension == '.tmp':
                print(f"TidyDLs: Ignoring temporary file: {item_path}")
                continue

            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(downloads_folder, folder)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    destination_path = os.path.join(destination_folder, os.path.basename(item_path))
                    destination_path = DownloadEventHandler().get_unique_destination(destination_path)

                    try:
                        shutil.move(item_path, destination_path)
                        print(f"TidyDLs: Moved existing file: {item_path} to {destination_path}")
                    except Exception as e:
                        print(f"TidyDLs: Failed to move {item_path}: {e}")
                    break
            else:
                print(f"TidyDLs: No matching folder for existing file extension: {file_extension}")

if __name__ == "__main__":
    # Move existing files before starting the observer
    move_existing_files()

    event_handler = DownloadEventHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=False)
    observer.start()
    print("TidyDLs: Monitoring started...")

    try:
        while True:
            time.sleep(1)
            event_handler.check_files_to_move()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
