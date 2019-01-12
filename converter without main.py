#import os
#os.chdir(r'C:\Users\ravil\OneDrive\Desktop') #use if file is present in other directory

#importing Library
import pydicom

#Reading ttfm & bmode files present in the same directory
ttfm = pydicom.read_file('ttfm.dcm')
bmode = pydicom.read_file('bmode.dcm')

#opening new text documents
text_ttfm = open('converted_ttfm.txt','w')
text_bmode = open('converted_bmode.txt','w')

#Writing dcm files in text format by converting it into string
text_ttfm.write(str(ttfm))
text_bmode.write(str(bmode))

#Printing & closing text files
print(text_ttfm,text_bmode)
text_ttfm.close()
text_bmode.close()
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










            
            
            
            
            
            
            
            
            
    
    
    
