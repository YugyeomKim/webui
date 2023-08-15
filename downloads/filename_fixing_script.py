import os

PATHNAME = 'ds'

directory = os.path.join(os.path.dirname(__file__), PATHNAME)

for folder in os.listdir(directory):
    folder_path = os.path.join(directory, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.endswith('.png'):
                new_file_name = 'mobile-screenshot.png'
                os.rename(file_path, os.path.join(folder_path, new_file_name))
            elif file.endswith('.json'):
                new_file_name = 'mobile.json'
                os.rename(file_path, os.path.join(folder_path, new_file_name))
