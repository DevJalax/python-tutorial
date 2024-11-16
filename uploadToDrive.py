from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Authenticate using credentials.json
SCOPES = ['https://www.googleapis.com/auth/drive']
creds = service_account.Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
service = build("drive", "v3", credentials=creds)

def create_folder(folder_name, parent_id=None):
    """Create a folder in Google Drive."""
    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
    }
    if parent_id:
        file_metadata["parents"] = [parent_id]

    folder = service.files().create(body=file_metadata, fields="id").execute()
    return folder.get("id")

def upload_file(file_path, folder_id):
    """Upload a file to a specific Google Drive folder."""
    file_name = os.path.basename(file_path)
    file_metadata = {
        "name": file_name,
        "parents": [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    service.files().create(body=file_metadata, media_body=media, fields="id").execute()

def main():
    # Define local source directory
    source_directory = "/path/to/your/files"  # Change this to your local directory containing files
    
    # File extensions for photos and videos
    photo_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
    video_extensions = {".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"}
    
    # Create "pics" and "videos" folders in Google Drive
    pics_folder_id = create_folder("pics")
    videos_folder_id = create_folder("videos")

    # Process files in the source directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file_name)

            if extension.lower() in photo_extensions:
                print(f"Uploading photo: {file_name}")
                upload_file(file_path, pics_folder_id)
            elif extension.lower() in video_extensions:
                print(f"Uploading video: {file_name}")
                upload_file(file_path, videos_folder_id)

if __name__ == "__main__":
    main()
