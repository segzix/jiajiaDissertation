import fitz

def count_words_in_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return len(text.split())

pdf_file = "./build/Thesis.pdf"  # 替换为你的 PDF 文件路径
print("Word Count:", count_words_in_pdf(pdf_file))
