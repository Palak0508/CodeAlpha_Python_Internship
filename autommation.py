import os
import shutil

def automate_file_movement():
    print("Task 3: Task Automation")
    
    user_path = os.environ['USERPROFILE']
    source_dir = os.path.join(user_path, 'OneDrive', 'Desktop', 'MyPhotos')
    target_dir = os.path.join(user_path, 'OneDrive', 'Desktop', 'JpgFolder')

    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print("Source folder created. Please put .jpg files in: " + source_dir)
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    files = os.listdir(source_dir)
    moved_count = 0

    for file_name in files:
        if file_name.lower().endswith(".jpg"):
            source_file = os.path.join(source_dir, file_name)
            target_file = os.path.join(target_dir, file_name)
            
            shutil.move(source_file, target_file)
            print("Moved: " + file_name)
            moved_count += 1

    print("\nAutomation Complete")
    print("Total files moved: " + str(moved_count))

if __name__ == "__main__":
    automate_file_movement()