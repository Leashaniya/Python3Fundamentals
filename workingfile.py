#connected with the file workingfile.txt

lookup=input("what software acronym would ypu like to look up: \n")
found=False
with open('workingfile.txt') as file:
    for line in file:
        if lookup in line:
            print(line)
            found=True
            break
    
    if not found:
        print("acronymn doesn't exist")
       