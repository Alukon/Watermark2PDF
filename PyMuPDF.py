import fitz
from fitz import Rect, open

input_file = "textPDF.pdf"
output_file = "textPDFNew.pdf"
barcode_file = "logo.png"
# определить позицию (верхний правый угол)
image_rectangle = fitz.Rect(450, 170, 550, 270)
# retrieve the first page of the PDF
file_handle = fitz.open(input_file)
first_page = file_handle[0]
# добавить изображение
first_page.insertImage(image_rectangle, filename=barcode_file)
file_handle.save(output_file)