import os
import zipfile
import shutil

def extract_zip(file, extract_to="data"):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def cleanup_data_folder(folder="data"):
    """
    Safely deletes and recreates the 'data' folder. Handles permission errors gracefully.
    """
    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
            print(f"✅ Deleted folder: {folder}")
        except PermissionError as e:
            print(f"⚠️ Permission denied: Could not delete '{folder}'. {e}")
        except Exception as e:
            print(f"⚠️ Error while deleting folder '{folder}': {e}")
    
    # Ensure folder exists even if deletion failed
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
            print(f"📁 Created folder: {folder}")
        except Exception as e:
            print(f"❌ Failed to create folder '{folder}': {e}")
