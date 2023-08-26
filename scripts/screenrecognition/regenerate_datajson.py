import os
import json

def get_directories(path):
    abs_path = os.path.join(os.path.dirname(__file__), path)
    directories = [d for d in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path, d))]
    return directories

def write_to_json(data, filename):
    abs_filename = os.path.join(os.path.dirname(__file__), filename)
    with open(abs_filename, 'w') as f:
        json.dump(data, f)

path = '../../downloads/ds'
directories = get_directories(path)
write_to_json(directories, '../../downloads/ds/customdata.json')
