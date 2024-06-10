from PyPDF2 import PdfReader, PdfWriter 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from io import BytesIO

def add_image_to_pdf(input_pdf, buffer_image, x, y):
    # Read the existing PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Go through all the pages in the existing PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        # Create a new PDF with ReportLab
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        rendered_image = ImageReader(buffer_image)

        can.drawImage(rendered_image, x, y, 100, 100)
        can.save()

        # Move to the beginning of the BytesIO buffer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Merge the new page with the existing page
        page.merge_page(new_page)
        writer.add_page(page)

    # Create a BytesIO object to hold the output PDF
    output_pdf_stream = BytesIO()
    writer.write(output_pdf_stream)
    output_pdf_stream.seek(0)

    return output_pdf_stream