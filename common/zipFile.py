import os
import os.path
from zipfile import ZipFile


class Compress:
    @staticmethod
    def zip_file(file_i: str, file_o: str) -> None:
        with ZipFile(file_o, 'w') as z:
            z.write(file_i, arcname=(n := os.path.basename(file_i)))

    @staticmethod
    def zip_files(*files_i: str, file_o: str) -> None:
        with ZipFile(file_o, 'w') as z:
            for f in files_i:
                z.write(f, arcname=(n := os.path.basename(f)))

    @staticmethod
    def zip_dir(dir_i: str, file_o: str) -> None:
        dir_i_parent = os.path.dirname(dir_i)
        with ZipFile(file_o, 'w') as z:
            z.write(dir_i, arcname=(n := os.path.basename(dir_i)))
            for root, dirs, files in os.walk(dir_i):
                for fn in files:
                    z.write(
                        fp := os.path.join(root, fn),
                        arcname=(n := os.path.relpath(fp, dir_i_parent)),
                    )

    @staticmethod
    def zip_dirs(*dirs_i: str, file_o: str) -> None:
        prefix = os.path.commonprefix(dirs_i)
        with ZipFile(file_o, 'w') as z:
            for d in dirs_i:
                z.write(d, arcname=(n := os.path.relpath(d, prefix)))
                for root, dirs, files in os.walk(d):
                    for fn in files:
                        z.write(
                            fp := os.path.join(root, fn),
                            arcname=(n := os.path.relpath(fp, prefix)),
                        )


if __name__ == '__main__':
    path1 = os.path.join(r"C:\Users\96142\Desktop\TestProject", "test_case")
    path2 = os.path.join(r"C:\Users\96142\Desktop\TestProject", "temp")
    path3 = os.path.join(r"C:\Users\96142\Desktop\TestProject", "note")
    path4 = os.path.join(r"C:\Users\96142\Desktop\TestProject", "conftest.py")
    path6 = os.path.join(r"C:\Users\96142\Desktop\TestProject", "main.py")

    Compress.zip_dir(path1, file_o='../ttt.zip')
    Compress.zip_files(path4, path6, file_o='./33.zip')
