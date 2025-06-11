import wget
import os
import zipfile
import shutil
import stat
class Update():
    def update():
        wget.download("https://github.com/KrajZajd/systoom/archive/refs/heads/main.zip")
        with zipfile.ZipFile("systoom-main.zip", 'r') as zip_ref:
            zip_ref.extractall("./")
        os.remove("systoom-main.zip")
        os.remove("./systoom-main/uzivatele.csv")
        for filename in os.listdir("./systoom-main"):
            src_path = os.path.join("./systoom-main", filename)
            dst_path = os.path.join("./", filename)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
        for root, dirs, files in os.walk("./systoom-main", topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.chmod(file_path, stat.S_IWRITE)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.chmod(dir_path, stat.S_IWRITE)
                os.rmdir(dir_path)
        os.chmod("./systoom-main", stat.S_IWRITE)
        os.rmdir("./systoom-main")