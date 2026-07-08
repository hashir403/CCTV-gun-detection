import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
import shutil

# Email configuration
from_email = "test@gmail.com"
to_email = ["test@gmail.com"]
subject = "Security Alert: Threat Detected"
Detection = "Gun detection"
body = f"""
ThreatEye | Anomaly Detection System Alert
Detection Type: {Detection}
Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Attached are the relevant images and video footage.
"""
password = "rust bcfn kifn wwan"

# Folder paths
IMAGE_FOLDER = 'images'  # Folder for temporary images
VIDEO_FOLDER = 'videos'  # Folder for temporary videos
PERMANENT_STORAGE = 'permanent_storage'  # New folder for permanent storage
MAX_ATTACHMENT_SIZE = 25 * 1024 * 1024  # 25MB (Gmail limit)

def create_permanent_storage():
    if not os.path.exists(PERMANENT_STORAGE):
        os.makedirs(PERMANENT_STORAGE)
        print(f"Created permanent storage folder: {PERMANENT_STORAGE}")
        
    permanent_image_folder = os.path.join(PERMANENT_STORAGE, 'images')
    permanent_video_folder = os.path.join(PERMANENT_STORAGE, 'videos')
    
    if not os.path.exists(permanent_image_folder):
        os.makedirs(permanent_image_folder)
        
    if not os.path.exists(permanent_video_folder):
        os.makedirs(permanent_video_folder)

def copy_to_permanent_storage():
    """Copy files from temporary folders to permanent storage"""
    create_permanent_storage()  # Ensure folders exist
    
    permanent_image_folder = os.path.join(PERMANENT_STORAGE, 'images')
    permanent_video_folder = os.path.join(PERMANENT_STORAGE, 'videos')
    
    copied_files = []
    
    # Copy images
    if os.path.exists(IMAGE_FOLDER):
        for filename in os.listdir(IMAGE_FOLDER):
            src_path = os.path.join(IMAGE_FOLDER, filename)
            if os.path.isfile(src_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                dest_path = os.path.join(permanent_image_folder, filename)
                try:
                    shutil.copy2(src_path, dest_path)
                    copied_files.append(dest_path)
                    print(f"Copied to permanent storage: {dest_path}")
                except Exception as e:
                    print(f"Error copying {filename} to permanent storage: {str(e)}")
    
    # Copy videos
    if os.path.exists(VIDEO_FOLDER):
        for filename in os.listdir(VIDEO_FOLDER):
            src_path = os.path.join(VIDEO_FOLDER, filename)
            if os.path.isfile(src_path) and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                dest_path = os.path.join(permanent_video_folder, filename)
                try:
                    shutil.copy2(src_path, dest_path)
                    copied_files.append(dest_path)
                    print(f"Copied to permanent storage: {dest_path}")
                except Exception as e:
                    print(f"Error copying {filename} to permanent storage: {str(e)}")
    
    return copied_files

def create_email():
    """Create the email message with attachments"""
    msg = MIMEMultipart()
    msg['From'] = from_email
    # msg['To'] = to_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

def attach_files(msg, folder_path, is_image=True):
    """Attach files from specified folder to the email"""
    if not os.path.exists(folder_path):
        print(f"Warning: Folder not found - {folder_path}")
        return 0
    
    attached_count = 0
    for filename in sorted(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories and check file size
        if not os.path.isfile(file_path):
            continue
            
        file_size = os.path.getsize(file_path)
        if file_size > MAX_ATTACHMENT_SIZE:
            print(f"Warning: {filename} ({file_size/1024/1024:.1f}MB) exceeds size limit, skipping")
            continue

        try:
            with open(file_path, 'rb') as f:
                if is_image and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img = MIMEImage(f.read())
                    img.add_header('Content-Disposition', 'attachment', filename=filename)
                    msg.attach(img)
                    attached_count += 1
                    print(f"Attached image: {filename}")
                
                elif not is_image and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    msg.attach(part)
                    attached_count += 1
                    print(f"Attached video: {filename}")
                    
        except Exception as e:
            print(f"Error attaching {filename}: {str(e)}")
    
    return attached_count

def send_email(msg):
    """Send the email with SMTP"""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

def cleanup_folders():
    """Clean up both temporary folders after sending"""
    for folder in [IMAGE_FOLDER, VIDEO_FOLDER]:
        if not os.path.exists(folder):
            continue
            
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {str(e)}")

if __name__ == "__main__":
    print("Preparing email with attachments...")
    
    # First copy files to permanent storage
    print("Copying files to permanent storage...")
    copied_files = copy_to_permanent_storage()
    if not copied_files:
        print("Warning: No files were copied to permanent storage")
    
    # Then proceed with email as before
    msg = create_email()
    
    # Attach files from both temporary folders
    img_count = attach_files(msg, IMAGE_FOLDER, is_image=True)
    vid_count = attach_files(msg, VIDEO_FOLDER, is_image=False)
    
    if img_count == 0 and vid_count == 0:
        print("No files found to attach. Email not sent.")
    else:
        if send_email(msg):
            # Clean up only if email was sent successfully
            cleanup_folders()
            print("Cleanup complete.")