#practicing the os module with real-world example (moving a file from one folder to another)
#3 step process-> read contents of the file, paste it into the folder file destination one and lasats delete the original file from old location

import os

def clean_workspace():
    # 1. Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🧹 Starting Simple Workspace Cleaner...\n")
    
    current_dir = os.getcwd()
    
    archive_folder = os.path.join(current_dir, "safe_archive")
    if not os.path.exists(archive_folder):
        os.mkdir(archive_folder)
        print("📁 Created 'safe_archive' directory.")
        
    print("-" * 40)
    
    all_files = os.listdir('.')
    
    for file in all_files:
        if file == "temp_system_error.log":
            print(f"🔍 Found target file: {file}")
            
            old_path = os.path.join(current_dir, file)
            new_path = os.path.join(archive_folder, file)
            
            with open(old_path, "r") as original_file:
                file_content = original_file.read()
                
            with open(new_path, "w") as archived_file:
                archived_file.write(file_content)
                

            os.remove(old_path)
            
            print(f"🚀 Successfully moved '{file}' into 'safe_archive/' using pure OS commands!")

    print("-" * 40)
    print("✅ Process complete.")

if __name__ == "__main__":
    # Setup step: Create a quick dummy log file to test our script on
    with open("temp_system_error.log", "w") as f:
        f.write("Error code 502: Server timeout.")
        
    # Run the script
    clean_workspace()