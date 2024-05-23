import os
#alle submappen osiris wordt omgezet in Osiris
def rename_osiris_folders(root_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == 'osiris':
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, 'Osiris')
                os.rename(old_path, new_path)
                count += 1
    return count

if __name__ == "__main__":
    root_directory = input("Voer het pad in waarin gezocht moet worden: ")
    if os.path.isdir(root_directory):
        changed_count = rename_osiris_folders(root_directory)
        print(f"Aantal aangepaste mappen: {changed_count}")
    else:
        print(f"Het opgegeven pad '{root_directory}' is geen geldige map.")
