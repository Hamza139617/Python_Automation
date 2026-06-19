from pymupdf import open, Pixmap, csRGB
import builtins
import sys
import os


def watermarking():
    pdfName = input("Please enter the name of the pdf")

    if os.path.exists(pdfName):
        print(" file exists ")
    else:
        print(" file doesn't exist ")
        sys.exit(1)
    
    
    document = open(pdfName)

    for pageIndx in range(len(document)):
        page = document[pageIndx]

        page.insert_image(page.bound(), filename="watermark.png", overlay=True)
    


    document.save("newDocument.pdf")
    
    

    


def mergeFiles():

    num = int(input("Enter the number of files to merge"))
    documents = []
    while(num > 0):
        try:
            documents.append(open(input("Enter the name of the pdf or the complete path to it : ")))
            num -= 1
        except Exception as e:
            print(f"Exception : {e}")
            break # stop in order to avoid corrupting important data
    
    num += 1

    while(num < len(documents)):
        documents[0].insert_pdf(documents[num])
        num += 1
    
    documents[0].save("result.pdf")

    
def splitFiles():
    
    docName = input("Enter the name of the document which you want to split ")

    if(os.path.exists(docName)):
        print("file exists")
    else:
        print("file doesn't exist")
        sys.exit(1)
    
    
    index = 0
   
    document = open("document.pdf")

    while(index < len(document)):
        result = (document[index]).search_for("Invoice")

        if result:
            splitDocument = open()
            splitDocument.insert_page(pno=0,
                                      text = document[index].get_text())
            splitDocument.save(f"splitted{index}.pdf")
            splitDocument.close()
        
        index += 1



def extractData():

    document = open("dataDocument.pdf")

    ## extracting the images first

    t = 0

    for i in range(len(document)):
        page = document[i]
        image_list = page.get_images()

        if(not(image_list)):
            continue
        
        for img in image_list:
            xref = img[0]
            pix = Pixmap(document, xref)

            if pix.n - pix.alpha > 3:
                pix = Pixmap(csgRGB, pix)
            
            pix.save(f"image{t}.png")
            pix = None
            t += 1
    
    t = 0

    with builtins.open("newFile.txt", "w") as file:
        for i in range(len(document)):
            page = document[i]

            tabs = page.find_tables()

            if (not(tabs.tables)):
                continue
        
            for table in tabs.tables:
                for item in table.extract():
                    for data in item:
                        if data == None:
                            continue

                        file.write(data + " \n")
            
    
        file.write("\n Stored all of the tables \n")

        for page in document:
            link = page.first_link

            while link:
                file.write(link.uri + "\n")
                link = link.next
    
    


def redactContent():

    document = open("birds.pdf")

    for page in document:

        instances = page.search_for("bird")

        for inst in instances:
            page.add_redact_annot(inst, fill=(0, 0, 0))

        page.apply_redactions()

    document.save('redacted_document.pdf')
    document.close()


def extractMetaData():

    pdfName = input("Enter the name of the pdf whose meta data you want to extract : ")

    if (not(os.path.exists(pdfName))):
        print("Please enter a valid path name : ")
        sys.exit(1)

    document = open(pdfName)

    with builtins.open("metaDataFile.txt", "w") as file:
        
        for item in document.metadata.values():
            if item == None:
                continue

            file.write(item)
            file.write("\n")

       
    
    document.close()

    
    


def main():

    choice = int(input("Enter the operation to perform : \n 1 merging files.\n 2 splitting files\n 3 Extracting data \n 4 Watermarking \n 5 Redacting sensitive content \n 6 Extracting meta data "))

    match choice:
        case 1:
            mergeFiles()
        
        case 2:
            splitFiles()

        case 3:
            extractData()

        case 4:
            watermarking()

        case 5:
            redactContent()

        case 6:
            extractMetaData()

        
        case _:
            print("Entered invalid data")



if __name__ == "__main__":
    main()