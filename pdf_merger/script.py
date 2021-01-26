########
#imports
########
from PyPDF2 import PdfFileReader, PdfFileMerger
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename

########
#Variables
########


########
#script
########

##########################################################################
def main():
    """
    """
    pdfOut = PdfFileMerger()
    pdfIn = pdfInput()
    for elem in pdfIn:
        pdfOut.append(elem)
    save = saveLocation()
    pdfOut.write(save)
##########################################################################
def pdfInput():
    """
    """
    Tk().withdraw()
    files = askopenfilenames(title="Choose files", filetypes =[('pdf file', '*.pdf')])
    return files


##########################################################################
def saveLocation():
    """
    """
    Tk().withdraw()
    fileName = asksaveasfilename(title='Choose a filename', defaultextension='.pdf', filetypes =[('pdf file', '*.pdf')])
    return fileName


if __name__ == "__main__":
    main()
