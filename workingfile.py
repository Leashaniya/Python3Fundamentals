#connected with the file workingfile.txt
def find():
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
       
def add():
    acronym=input("what acronym you want to add \n")
    definition=input("what is the definition \n")

    with open ('workingfile.txt ','a') as file:
        file.write(acronym+' - '+definition+'\n')

def main():
    #ask they want to find or add acronymn
    choice=input("do you want to add or find acronym: \n")
    if choice=='F':
        find()
    elif choice=='A':
        add()

main()
