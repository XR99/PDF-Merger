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
    Merges pdf documents and saves them in given Location
    """
    pdfOut = PdfFileMerger()
    pdfIn = pdfInput()
    if len(pdfIn) < 2:
        print("no input")
        return
    save = saveLocation()
    if not save:
        print("no output location")
        return
    for elem in pdfIn:
        pdfOut.append(elem)
    pdfOut.write(save)
##########################################################################
def pdfInput():
    """
    Asks for pdf documents as Input
    @return tuple with filepaths
    """
    Tk().withdraw()
    files = askopenfilenames(title="Choose files", filetypes =[('pdf file', '*.pdf')])
    return files


##########################################################################
def saveLocation():
    """
    asks for save location and document name
    @return filepath
    """
    Tk().withdraw()
    fileName = asksaveasfilename(title='Choose a filename', defaultextension='.pdf', filetypes =[('pdf file', '*.pdf')])
    return fileName


if __name__ == "__main__":
    main()
