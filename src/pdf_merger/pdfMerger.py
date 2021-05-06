########
#imports
########
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
import argparse
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
    parser = argparse.ArgumentParser(description='Merge pdf documents.')
    parser.add_argument("-g", "--gui", help="provides a graphical user interface", action="store_true")
    parser.add_argument("-d", "--directory", type=str,  help="merges all pdfs in a given directory")
    args = parser.parse_args()

    if args.gui:
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
    elif args.directory:
        """
        Merge all pdfs in a given directory
        """
        print("provided directory: {}".format(args.directory))
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
                if check == 0 or i == 3:
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
