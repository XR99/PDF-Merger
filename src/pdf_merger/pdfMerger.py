########
#imports
########
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
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
    Merge pdfs a certain way based on given flag
    """
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("You need to provide a flag!")
        print("If you need help use flag -h or --help")
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Help for usage")
    elif sys.argv[1] == "-g":
        """
        Merge pdfs guided with gui filechooser
        """
        pdfIn = pdfInput()
        if len(pdfIn) < 2:
            print("You need to provide at least 2 Pdf documents!")
            return
        pdfOut = saveLocation()
        if pdfOut is None:
            print("You need to provide a save location!")
            return
        mergedPdf = merge(pdfIn)
        if merge is None:
            print("Error in merge occured!")
            return
        save(mergedPdf, pdfOut)
        print("Merge was successful")
        return
    elif sys.argv[1] == "-d":
        """
        Merge all pdfs in a given directory
        """
        if len(sys.argv) != 3:
            print("U need to provide a directory Path with this flag!")
            print("For usage use flag -h or --help")
            return

##########################################################################
def merge(input):
    """
    Merges pdf documents
    """
    pdfOut = PdfFileMerger()
    for elem in input:
        try:
            pdfOut.append(elem)
        except:
            pdfOut.close()
            return
    return pdfOut
##########################################################################
def save(pdf, location):
    """
    Saves a given pdf file at a given location
    """
    try:
        pdf.write(location)
    except:
        print("Error")
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
def decrypt(filePaths):
    """
    checks if given pdfs are encrypted and decrypts them if necessary 
    """
    pdfList = []
    for path in filePaths:
        try:
            pdfList.append(PdfFileReader(path))
        except:
            print("Cuold not create Pdf Object")
    for pdf in pdfList:
        if pdf.isEncrypted:
            print("Encrypted")
            inputDesc = "Provide password for{title}".format(pdf.getDocumentInfo().title)
            i = 0
            while True:
                passwd = input(inputDesc)
                check = pdf.decrypt(passwd)
                i += 1
                if check is 0 or i is 3:
                    break
    # need to put decrypted pdf in list?          
    return pdfList

###########################################################################
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
