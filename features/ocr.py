import easyocr


def text_recognition(file_path, text_file_name='ocr.txt'):
    reader = easyocr.Reader(["en", "ru"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    with open(text_file_name, "a", encoding='utf-8') as file:
        for line in result:
            file.write(f"{line}\n\n")

    return f"Result wrote into {text_file_name}"


if __name__ == "__main__":
    text_recognition(file_path='7609.png')
