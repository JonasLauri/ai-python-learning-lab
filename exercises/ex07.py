# Exercise 3 — File Organizer Simulation

files = [
    "photo.jpg",
    "report.docx",
    "notes.txt",
    "video.mp4",
    "script.py",
    "presentation.pptx",
]

# Group files by category into dict
dict_files = {}

for file in files:
    if file.endswith((".jpg", ".png")):
        dict_files.setdefault("images", []).append(file)
    elif file.endswith((".mov", ".mp4", ".mkv")):
        dict_files.setdefault("videos", []).append(file)
    elif file.endswith((".html", ".py", ".css", ".c")):
        dict_files.setdefault("code", []).append(file)
    elif file.endswith((".txt", ".pdf", "docx")):
        dict_files.setdefault("documents", []).append(file)
    else:
        dict_files.setdefault("other", []).append(file)

# Print how many files are in each group.
# print(
#     f"There are {len(dict_files['images'])} image files,"
#     f" {len(dict_files['videos'])} video files,"
#     f" {len(dict_files['code'])} code files,"
#     f" {len(dict_files['documents'])} documents files,"
#     f" {len(dict_files['other'])} other files"
# )

# Print all file names neatly under each category.
for category, files in dict_files.items():
    print(f"{category.capitalize()} ({len(files)} files):")
    for file in files:
        print(" -", file)
