import pyttsx3
import PyPDF2
import sys, getopt, os

def main(argv):
    inputfile = ''
    inputpage = 1


    try:
        opts, args  = getopt.getopt(argv,"hi:p:",["ifile=","pnum="])

    except getopt.GetoptError as e:
        print("Something went wrong...")
        print('ab.py -i <inputfile> -o <pagenumber>')
        print(e)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('ab.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-p', '--pnum'):
            inputpage = int(arg)
        else:
            print("Flag {o} not defined".format(o=opt))
            sys.exit()

    print("Input File: {i}, page {p}".format(i=inputfile, p=inputpage))

    readings = os.listdir('readings')
    if inputfile not in readings:
        print('Please make sure {r} is in the `readings` folder'.format(r=inputfile))
        sys.exit(2)

    print("Starting audiobook reader...")
    read_file_aloud(inputfile, inputpage)
    print("Finished reading.")




def read_file_aloud(fn, pnum):
    full_fn = "readings/" + fn
    pdf = open(full_fn, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdf)
    pages = pdfReader.numPages

    if pnum >= pages:
        print("Trying to read from a page that doesn't exist. There are only {m} pages found in the pdf `{fn}`".format(m=pages, fn=full_fn))
        print("  Hint: Use a number less than {m}".format(m=pages))
    else:
        print("Starting to read {n} of {m}".format(n=pnum, m=pages))
    
    print("initializing speaker...")
    speaker = pyttsx3.init()

    print("Getting page... {p}".format(p=pnum))
    page = pdfReader.getPage(pnum)

    print("Getting text:")
    text = page.extractText()
    print(text)
    
    print("\n\nSpeaking...")
    speaker.say(text)
    speaker.runAndWait()



if __name__ == "__main__":
    main(sys.argv[1:])
