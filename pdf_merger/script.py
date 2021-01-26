########
#imports
########
from PyPDF2 import PdfFileReader, PdfFileMerger

########
#script
########

def main():
    """
    """

    pdfOut = PdfFileMerger()
    pdfIn = pdfInput()
    save = saveLocation()

    for elem in pdfIn:
        pdfOut.append(elem)
    
    pdfOut.write(save)

def pdfInput():
    """
    """

def saveLocation():
    """
    """


if __name__ == "__main__":
    main()
