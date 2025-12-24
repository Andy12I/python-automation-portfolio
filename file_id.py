import os

folder_path = r"C:\Users\Anurag Tiwari\Desktop\test_cleaner"
files = os.listdir(folder_path)

print(f"Scanning {len(files)} files...")
print("-" * 30)

for file in files:
    # This magic line splits the name from the extension
    filename, extension = os.path.splitext(file)
    
    # We print them separately to prove we have them captured
    # Only print if there is actually an extension (ignore folders)
    if extension:
        print(f"File: {filename}   --->   Type: {extension}")