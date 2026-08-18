import re
def read_file(filename):
    file=open(filename,'r')
    f=file.read()
    print(f)
    file.close()

def write_file(filename):
    file=open(filename,'w')
    write=input("Enter text you want to add in the text file : \n")
    file.write(write)
    file.close()

def search_in_file(filename):
    pattern=input("Enter the pattern to search: ")
    file=open(filename,'r')
    f=file.read()
    result=re.findall(pattern,f)
    if result:
        print("found")
        for i in result:
            print(i)
    else:
        print("not found")
    file.close()

def find_emails(filename):
    text = read_file(filename)
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(pattern, text)
    print("\nEmail Addresses:")
    for email in emails:
        print(email)

def find_phone_numbers(filename):
    text = read_file(filename)
    pattern = r"\b\d{10}\b"
    phones = re.findall(pattern, text)
    print("\nPhone Numbers:")
    for phone in phones:
        print(phone)

def format_file(filename):
    file=open(filename,'r')
    f=file.read()
    edited_text=re.sub(r'\s+', ' ', f).strip()
    file.close()
    file = open(filename, 'a')
    file.write(edited_text)
    file.close()
    print("Text has been formatted")
    print(edited_text)

def replace_in_file(filename):
    old = input("Enter the text that is to be replaced : ")
    new = input("Enter the new text : ")
    file=open(filename,'r')
    f=file.read()
    new_text=re.sub(old, new, f)
    file.close()
    file = open(filename, 'a')
    file.write(new_text)
    file.close()
    print("Replaced successfully ")
    print(new_text)

def main_menu():
    fh=input("Enter the filename with extension : ")
    print("This program contains following functions")
    print("1.Read a file \n 2.Write in a file \n 3.Search in a file \n 4.Find Email \n5.Find phone no. \n 6.Format a file  \n 7.Replace the old content of a file with new \n 8.Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        read_file(fh)
    elif ch==2:
        write_file(fh)
    elif ch==3:
        search_in_file(fh)
    elif ch==4:
        find_emails(fh)
    elif ch==5:
        find_phone_numbers(fh)
    elif ch==6:
        format_file(fh)
    elif ch==7:
        replace_in_file(fh)
    elif ch==8:
        return False
    else:
        print("Invalid choice")
    return True

flag = True

while flag:
    flag = main_menu()