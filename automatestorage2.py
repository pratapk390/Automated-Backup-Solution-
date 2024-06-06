import os
import tarfile
import logging
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime

# Configuration
LOCAL_DIRECTORY = "E:\log" # Local Diretory 
LOG_FILE = "Report.log"     #Report will be generated in text file 
CREDENTIALS_FILE = "credentials.json"  # Google drive authontication key in the JSON formate

# Logging configuration
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def create_tarfile(source_dir, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    logging.info(f"Created tar file: {output_filename}")

def upload_to_google_drive(local_file, drive):
    try:
        file_drive = drive.CreateFile({'parents': [{'id': '1uwpK_nJcYk9JcnO17enokGQ-HrMb7WpW'}]})
        file_drive.SetContentFile(local_file)
        file_drive.Upload()
        logging.info(f"Successfully uploaded {local_file} to Google Drive")
    except Exception as e:
        logging.error(f"Failed to upload {local_file} to Google Drive: {e}")

def authenticate_google_drive(credentials_file):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials_file)
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # Authenticate if they're not there
    elif gauth.access_token_expired:
        gauth.Refresh()  # Refresh them if expired
    else:
        gauth.Authorize()  # Initialize the saved creds
    gauth.SaveCredentialsFile(credentials_file)
    return GoogleDrive(gauth)

def main():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_filename = f"{LOCAL_DIRECTORY.rstrip(os.sep)}_{timestamp}.tar.gz"

    create_tarfile(LOCAL_DIRECTORY, tar_filename)
    
    drive = authenticate_google_drive(CREDENTIALS_FILE)
    upload_to_google_drive(tar_filename, drive)

    if os.path.exists(tar_filename):
        os.remove(tar_filename)
        logging.info(f"Removed temporary tar file: {tar_filename}")

if __name__ == "__main__":
    main()
