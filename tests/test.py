from quickpathstr import Filepath

# MAIN ENTRYPOINT
def main():
    test = Filepath(fr"C:\Users\myself\Desktop\MyFile.txt")
    
    print(test.complete)
    print(test.directory)
    print(test.name)
    print(test.root)
    print(test.extension)

# TOP LEVEL SCRIPT ENTRYPOINT
if __name__ == '__main__':
    main()
