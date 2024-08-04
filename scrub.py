import os
import shutil
import hashlib
import uuid

def generate_unique_name(file_path):
    """Generate a unique name for the file based on its content."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    unique_name = hash_md5.hexdigest() + '_' + str(uuid.uuid4())
    return unique_name

def scrub_and_upload_files(src_dir, dest_dir, file_extensions):
    """
    Scrub files from the source directory and upload them to the destination directory.

    :param src_dir: Source directory containing backup disc CDs
    :param dest_dir: Destination directory to upload files
    :param file_extensions: List of file extensions to consider
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")

    for root, _, files in os.walk(src_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in file_extensions):
                src_file_path = os.path.join(root, file)
                unique_name = generate_unique_name(src_file_path)
                ext = os.path.splitext(file)[1]
                dest_file_path = os.path.join(dest_dir, unique_name + ext)

                if not os.path.exists(dest_file_path):
                    shutil.copy2(src_file_path, dest_file_path)
                    print(f"Copied {src_file_path} to {dest_file_path}")
                else:
                    print(f"File {dest_file_path} already exists. Skipping.")

    print("File scrubbing and uploading completed.")

# Example usage
source_directory = 'D:/'
destination_directory = 'G:/My Drive/Photo Backup'
file_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', 
                   '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']

scrub_and_upload_files(source_directory, destination_directory, file_extensions)
