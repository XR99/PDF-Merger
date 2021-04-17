########
#imports
########
from PyPDF2 import PdfFileMerger

########
#Variables
########

########
#script
########

##########################################################################
def main():
    """
    function of pdf merge given as script(without gui)
    """
    print("Still in production")
##########################################################################
def merge(input, save):
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
    Saves a given pdf file at a specific location
    """
    try:
        pdf.write(location)
    except:
        print("Error")


if __name__ == "__main__":
    main()
