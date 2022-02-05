def main():
    task = input('Enter the written text in text editor: ')
    lst = []

    for i in range(len(task)):
        item = task[i]
        if item == '<' : # if item is <, remove latest item in lst
            lst.pop()
        else:
            lst.append(item) # add to lst if item is not <
            
    output = ''.join(lst)
    print(output)
    
if __name__ == '__main__':
    main()