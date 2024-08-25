
def main():


    PATH_TO_BOOK='Books/frankenstein.txt'
    count=0

    with open(PATH_TO_BOOK,'r')as f:
        file_content=f.read()

    words = file_content.split()
    mydict={}

    for char in file_content:
        if char in mydict:
            mydict[char]+=1
        else:
            mydict[char]=1

    count=len(words)
    print(count)

    for char,count in mydict.items():
        print(f"{char} appears {count} times")





if __name__ == "__main__" :
    main()






