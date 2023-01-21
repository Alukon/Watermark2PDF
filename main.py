# pip install PyPDF2
import PyPDF2

input_file = 'textPDF.pdf'
output_file = 'textPDF1.pdf'
watermark_file = 'logo.pdf'

with open(input_file, 'rb',) as file_input:
    pdf = PyPDF2.PdfReader(file_input)

    with open(watermark_file, 'rb') as file_watermark:
        watermark = PyPDF2.PdfReader(file_watermark)

        first_page = pdf.getPage(0)
        first_page_watermark = watermark.getPage(0)

        first_page.mergePage(first_page_watermark)

        pdf_writer = PyPDF2.PdfWriter()

        pdf_writer.addPage(first_page)

        with open(output_file, 'wb') as file_output:
            pdf_writer.write(file_output)