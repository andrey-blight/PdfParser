import PyPDF2
import io
from PIL import Image
import pytesseract

def extract_images_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text_result = []

        for page_number, page in enumerate(pdf_reader.pages):
            # Проверяем наличие XObject
            if "/XObject" in page["/Resources"]:
                xObject = page["/Resources"]["/XObject"].get_object()

                for obj in xObject:
                    if xObject[obj]["/Subtype"] == "/Image":
                        width = xObject[obj]["/Width"]
                        height = xObject[obj]["/Height"]
                        data = xObject[obj].get_data()

                        # Проверка формата цвета
                        color_space = xObject[obj]["/ColorSpace"]
                        mode = "RGB" if color_space == "/DeviceRGB" else "P"

                        try:
                            # Создаем изображение
                            image = Image.frombytes(mode, (width, height), data)
                            # Распознаем текст
                            text = pytesseract.image_to_string(image, lang="eng")
                            text_result.append(text)
                        except Exception as e:
                            print(f"Ошибка обработки изображения на странице {page_number + 1}: {e}")

    return "\n".join(text_result)


# Укажите путь к PDF
pdf_path = "test.pdf"
result_text = extract_images_from_pdf(pdf_path)
print(result_text)