def add_acronym():
    acronym = input ('What acronym do you want to add?\n')
    definition = input ('What is the definition?')

    with open('Acronyms.txt', 'a') as file:
        file.write(acronym+' - '+definition+'\n')

def find_acronym():
    look_up= input('What Amadeus acronym would you like to look up?\n')

    found = False

    try:
        with open('Acronyms.txt') as file:                          # With statement automatically closes the file when the block of code finishes.   
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    
    except FileNotFoundError as e:                                  # If the Acronyms.txt file gets deleted or renamed accidentally then we print "File not found"
        print('File not found')
        return                                                      # return prevents from running the next if statement

    if not found:
        print('The acronym does not exist')

def main():
    choice = input('Do you want to Find(F) or Add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

if __name__ == "__main__":
    main()
                
            