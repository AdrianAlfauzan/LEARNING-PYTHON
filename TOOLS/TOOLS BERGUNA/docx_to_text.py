from docx import Document


def docx_to_text(docx_file):
    doc = Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


if __name__ == "__main__":
    docx_file = "D:/BELAJAR FT MY CODING/BELAJAR PYTHON/TOOLS/TOOLS BERGUNA/3411221020_AdrianMusaAlfauzan_MODUL_2_JavaIdentifier_Literal_dan_Operator.docx"
    text = docx_to_text(docx_file)
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(text)
