import os
import re

def normalize_filename(name):
    return re.sub(r" \(\d+\)(\.[^.]+)$", r"\1", name)

def remove_duplicates(path):
    list_files = []
    for folder, subfolders, files in os.walk(path):
        subfolders[:] = [d for d in subfolders if d != "$RECYCLE.BIN"]

        for file in files:
            normalized = normalize_filename(file)
            if normalized not in list_files:
                list_files.append(normalized)
            else:
                try:
                    file_path = os.path.join(folder, file)
                    # os.chmod(file_path, 0o777)
                    os.remove(file_path)
                    print(f'removed {file_path}')
                    if not os.listdir(folder):
                        os.rmdir(folder)
                        print(f'removed {folder}')
                except PermissionError:
                    print("accès refusé")

if __name__ == "__main__":
    remove_duplicates("D:\\")
