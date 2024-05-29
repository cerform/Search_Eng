import mammoth

def process_docx(file):
    with open(file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        return result.value  # The converted HTML
