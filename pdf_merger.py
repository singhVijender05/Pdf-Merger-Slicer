import PyPDF2
#python program to merge,split pdf files 

def pdf_merger():
    merger=PyPDF2.PdfMerger() #create a instance of merger class , it will merge all pdfs
    
    #add pdfs to list by path to start merge process
    all_pdf_string=input('enter all pdf paths seperated by space')
    pdf_list=all_pdf_string.split(' ')

    output_file=input('enter output file name to be set')


    # for pdf_file in pdf_list:
    #     currentFile=open(pdf_file,'rb') #open in read binary form
    #     cfileContent=PyPDF2.PdfReader(currentFile) #attach content to a object named cfileContent
    #     merger.append(cfileContent) #send cfile content to merger to merge
    #     currentFile.close() #close file
    # merger.write('merged.pdf')  #create merged pdf

    #more concise way
    try:
        for pdf_file in pdf_list:
            with open(pdf_file,'rb') as currentFile:
                merger.append(currentFile)
        merger.write(output_file)
    except:
        print('error opening pdfs either pdf does\'t exists or been corrupted')

