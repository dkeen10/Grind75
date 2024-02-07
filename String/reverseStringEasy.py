def reverseString(string):
    reversedString = string[::-1]
    return reversedString
    

def main():
    string = "hello"
    print(reverseString(string))


if __name__ == "__main__":
    main()