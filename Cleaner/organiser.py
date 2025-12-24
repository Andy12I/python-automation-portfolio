import os
import shutil  # <--- New Tool: This moves files!

# 1. The folder we are cleaning
folder_path = r"C:\Users\Anurag Tiwari\Desktop\test_cleaner"

# 2. The "Rule Book" (Which extension goes where?)
# I added the specific types I saw in your list (.cdr, .ai, .xlsx, etc.)
folders = {
    "Images":    [".jpg", ".jpeg", ".png", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".xlsm"],
    "Design":    [".cdr", ".ai", ".psd"],
    "Media":     [".mp3", ".mp4", ".m4a", ".wav"],
    "Archives":  [".zip", ".rar"]
}

print(f"Cleaning folder: {folder_path}")
print("-" * 30)

# 3. Loop through every file
for file in os.listdir(folder_path):
    
    # Get the extension (in lowercase so .JPG and .jpg both work)
    filename, ext = os.path.splitext(file)
    ext = ext.lower()
    
    # Skip if it's a folder (folders don't have extensions usually)
    if not ext:
        continue

    # 4. Find the correct home for this file
    found_category = False
    
    for category, extensions_list in folders.items():
        # If this file extension is in our list (e.g., is .jpg inside Images?)
        if ext in extensions_list:
            
            # A. Define the destination folder (e.g., .../test_cleaner/Images)
            target_folder = os.path.join(folder_path, category)
            
            # B. Create the folder if it doesn't exist yet
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                print(f"📁 Created new folder: {category}")
            
            # C. Define the full old path and full new path
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(target_folder, file)
            
            # D. Move it!
            shutil.move(old_path, new_path)
            print(f"Moved: {file}  >>>  {category}")
            found_category = True
            break # Stop checking other categories
            
    # Optional: If we didn't find a rule for it, put it in "Others"
    if not found_category:
        other_folder = os.path.join(folder_path, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)
            
        shutil.move(os.path.join(folder_path, file), os.path.join(other_folder, file))
        print(f"Moved: {file}  >>>  Others")

print("-" * 30)
print("✅ Cleaning Complete!")