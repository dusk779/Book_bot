
def main():


    PATH_TO_BOOK='Books/frankenstein.txt'

    with open(PATH_TO_BOOK,'r')as f:
        file_content=f.read()

    print(file_content)

if __name__ == "__main__" :
    main()






