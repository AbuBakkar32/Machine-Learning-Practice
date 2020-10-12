from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    Get Page: {pdf.getPage(1)}
    """

    print(txt)
    return information


if __name__ == '__main__':
    path = 'MyCV.pdf'
    extract_information(path)


#################################################
# Rotate PDF
# def rotate_pages(pdf_path):
#     pdf_writer = PdfFileWriter()
#     pdf_reader = PdfFileReader(pdf_path)
#     # Rotate page 90 degrees to the right
#     page_1 = pdf_reader.getPage(0).rotateClockwise(90)
#     pdf_writer.addPage(page_1)
#     # Rotate page 90 degrees to the left
#     page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
#     pdf_writer.addPage(page_2)
#     # Add a page in normal orientation
#     pdf_writer.addPage(pdf_reader.getPage(2))
#
#     with open('rotate_pages.pdf', 'wb') as fh:
#         pdf_writer.write(fh)
#
#
# if __name__ == '__main__':
#     path = 'MyCV.pdf'
#     rotate_pages(path)


##################################################
# # Merge PDF
# def merge_pdfs(paths, output):
#     pdf_writer = PdfFileWriter()
#
#     for path in paths:
#         pdf_reader = PdfFileReader(path)
#         for page in range(pdf_reader.getNumPages()):
#             # Add each page to the writer object
#             pdf_writer.addPage(pdf_reader.getPage(page))
#
#     # Write out the merged PDF
#     with open(output, 'wb') as out:
#         pdf_writer.write(out)
#
#
# if __name__ == '__main__':
#     paths = ['document1.pdf', 'document2.pdf']
#     merge_pdfs(paths, output='merged.pdf')

######################################
# Encript PDF

# def add_encryption(input_pdf, output_pdf, password):
#     pdf_writer = PdfFileWriter()
#     pdf_reader = PdfFileReader(input_pdf)
#
#     for page in range(pdf_reader.getNumPages()):
#         pdf_writer.addPage(pdf_reader.getPage(page))
#
#     pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
#                        use_128bit=True)
#
#     with open(output_pdf, 'wb') as fh:
#         pdf_writer.write(fh)
#
#
# if __name__ == '__main__':
#     add_encryption(input_pdf='reportlab-sample.pdf',
#                    output_pdf='reportlab-encrypted.pdf',
#                    password='twofish')
