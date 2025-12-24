import os

# 1. Define the path to your messy folder
# r"" tells Python to treat backslashes as normal text
folder_path = r"C:\Users\Anurag Tiwari\Desktop\test_cleaner"

print(f"Targeting folder: {folder_path}")

# 2. Check if it exists
if os.path.exists(folder_path):
    print("✅ Folder found! Here is what is inside:")
    print("-" * 30)
    
    # 3. Get the list of files
    files = os.listdir(folder_path)
    
    for file in files:
        # Print the name of the file
        print(file)
        
    print("-" * 30)
    print(f"Total files found: {len(files)}")

else:
    print("❌ Error: I cannot find the folder.")
    print("Double check: Is it named exactly 'test_cleaner' and is it on your Desktop?")