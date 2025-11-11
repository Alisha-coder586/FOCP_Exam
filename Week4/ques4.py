str=input("Enter a string: ")
# str="Hey how are you\n"
def remove_last(str):
    print(str)
    if len(str)>1:
        str=str.strip()
        str=str[:-1]
    else:
        str=str
    print(str)
    return str
remove_last(str)