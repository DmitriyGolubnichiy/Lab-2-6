# Директория для запуска C:/Users/varel/OneDrive/Рабочий стол/lab_5 information
def fileInfo():
        import os
        import datetime

        print("Напишите директорию файлов: ")
        direction = input()
        directory = os.listdir(direction)

        file = open("information.txt", 'w', encoding="UTF-8")

        for element in range(len(directory)):

                curr_el = directory[element]

                size = os.path.getsize(direction + f"\\" + curr_el)

                creation_timestamp = os.path.getctime(direction + f"\\" + curr_el)
                creation_date = datetime.datetime.fromtimestamp(creation_timestamp)

                splitword = os.path.splitext(curr_el)
                file_name = splitword[0]
                file_format = splitword[1]

                file.write(str(element+1) + ".Название файла:" +  file_name + ";\n  Формат файла:" + file_format + ";\n  Размер файла:" + str(size)
                           + ";\n  Дата создания файла:" + str(creation_date) + ";\n\n")

fileInfo()