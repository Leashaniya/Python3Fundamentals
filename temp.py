#ask the user what acronym they want to add
#then ask the user for the definition
#open the file
#write the new acronym and definition to the file 

#connected with the file workingfile.txt


acronym=input("what acronym you want to add \n")
definition=input("what is the definition \n")

with open ('workingfile.txt ','a') as file:
    file.write(acronym+' - '+definition+'\n')