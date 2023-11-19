from PIL import Image

"Директория фото: C:/Users/varel/PycharmProjects/pythonProject/Chapa.jpg"
def ImageDirection():
    img_formats = [".png", ".jpg", ".ico"]
    ChooseFormat = int(input("Введите, в какой формат хотите преобразовать картинку: 0-png, 1-jpg, 2-ico\n"))

    img = Image.open("C:/Users/varel/PycharmProjects/pythonProject/Chapa.jpg")
    img_directory = "C:/Users/varel/PycharmProjects/pythonProject/Chapa.jpg"
    SplitDirectory = img_directory.split(".")
    new_image = SplitDirectory[0] + img_formats[ChooseFormat]
    img.save(new_image)

ImageDirection()
