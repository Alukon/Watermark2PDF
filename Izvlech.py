import fitz  # Импорт PyMuPDF
doc = fitz.open("textPDF.pdf")  # Открываем документ
page = doc[0]  # Указываем номер нужной страницы
text = page.get_text()  # Извлекаем текст
print(text)  # Выводим его