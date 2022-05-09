import yadisk
import os

y = yadisk.YaDisk(token="AQAAAAA2TaanAADLW6u0VG_AJkudvaRaa-03QAQ")

def folder(path, name):

    y.mkdir(f"/{name}")   #  Запись пути где будет создана папка
    try:
        for address, dirs, files in os.walk(path):
            for dir in dirs:
                y.mkdir(f'/{name}/{dir}')
                print(f'Папка {dir} создана')
            for file in files:
                print(f'Файл {file} загружен')
                y.upload(f'{address}/{file}', f'/{name}/{file}')
    except:
        print("Такой файл есть")

if __name__ == '__main__':
    way = r"C:\Users\sergs.DESKTOP-I516LL5\Desktop\vs code\_"                       # Путь к папке которую переносим на YaDisk
    name = os.path.basename(way)    # Берем имя папки что бы с таким же именем создать на YaDisk
    folder(way, name)







