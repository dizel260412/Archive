import os
import shutil
from datetime import datetime


def ivi(path):
    for i in os.listdir(path):
        files_path = os.listdir(fr'{path}\{i}')
        for file in files_path:
            ts = os.path.getmtime(fr'{path}\{i}\{file}')
            mod = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
            year = mod[:4]
            year_month = mod[:7]
            if year in os.listdir(path):
                if year_month in os.listdir(fr'{path}\{year}'):
                    if mod in os.listdir(fr'{path}\{year}\{year_month}'):
                        try:
                            shutil.move(fr'{path}\{i}\{file}', fr'{path}\{year}\{year_month}\{mod}')
                        except:
                            os.remove(fr'{path}\{i}\{file}')
                    else:
                        os.mkdir(fr'{path}\{year}\{year_month}\{mod}')
                        shutil.move(fr'{path}\{i}\{file}', fr'{path}\{year}\{year_month}\{mod}')
                else:
                    os.mkdir(fr'{path}\{year}\{year_month}')
                    os.mkdir(fr'{path}\{year}\{year_month}\{mod}')
                    shutil.move(fr'{path}\{i}\{file}', fr'{path}\{year}\{year_month}\{mod}')
            else:
                os.mkdir(fr'{path}\{year}')
                os.mkdir(fr'{path}\{year}\{year_month}')
                os.mkdir(fr'{path}\{year}\{year_month}\{mod}')
                shutil.move(fr'{path}\{i}\{file}', fr'{path}\{year}\{year_month}\{mod}')
        os.rmdir(fr'{path}\{i}')


def main():
    path = r'C:\Users\datel3\OneDrive - IKEA\Desktop\New folder'
    ivi(path)


if __name__ == '__main__':
    main()
