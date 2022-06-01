import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)
    print("iK BEN BEZIG")
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
        print("a")
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
        print("b")
    print("gedaan")

explore("C:/tmp/")