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


#function to slice pdf using page limit(partition factor)
#for example if total page in original pdf are 25 and you select partition factor as 5 then 5 pdfs of 5 pages each will be generated
def splitpdf(input_file,page_limit):
    #configure pdf reader
    pdf_reader=PyPDF2.PdfReader(input_file)
    #now this pdfReader can access all the content or you can say pages
    total_pages=len(pdf_reader.pages)
    
    for start in range(0,total_pages,page_limit):
        end=start+page_limit
        if(total_pages<end):
            end=total_pages
        output_file=f'output_{start}-{end}.pdf' #name output file
        pdf_writer=PyPDF2.PdfWriter()
        for i_page in range(start,end):
            page=pdf_reader.pages[i_page]
            pdf_writer.add_page(page) #add page to writer
        with open(output_file,"wb") as outputFile:
            # now writer will write all the pages to output file
            pdf_writer.write(outputFile)
        print(f'created output file as {output_file}')


