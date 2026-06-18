import pymupdf

doc_a = pymupdf.open("birds.pdf")
doc_b = pymupdf.open("machine.pdf")

doc_a.insert_pdf(doc_b)
doc_a.save("a+b.pdf")
    