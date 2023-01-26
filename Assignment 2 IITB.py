#file handling


#to read and write  - r+

#cursor in the beginning
#overrides the existing data if write command is given before read command
#raise an error if file is not already existing



'''
f=open("data.txt","r+")
print(f.read()) #read and print only the data that was already existing 
f.write("\n python is intresting \n")
f.close()
'''



'''since cursor is in the begging it reads the existing data first
and then writes what is told so it wont print the current
data on idle but new written changes will be visible in file. '''



#to write and read  - w+

#over rides existing data
#create file if it doesnt already exists

'''
f=open("data+.txt","w+")
f.write("i am limitless\n")
f.seek(0)
print(f.read())
f.close()
'''


'''
if seek is not used the output on idle will be empty because existing data has been erased and
after writing cursor is at the end of what was recently written, so nothing will be read

therefore f.seek(0) would be used before the read , to make the cursor go back to the
beginning of the file to print on idle what had been written
'''


#to read and write together - a+


#doesnt rides existing data
#creates a file if it doesnt already exists
#cursor is at the end of the file ,use of read before write prints nothing on idle
#not using seek before read would print nothing on idle as cursor is at the end of what was written.

'''
f=open("data+.txt","a+")
f.write("\n i am financially independent\n")
f.seek(0)
print(f.read())
f.close()
'''

 
