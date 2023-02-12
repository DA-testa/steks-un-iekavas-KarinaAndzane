from collections import namedtuple
import requests
url = 'https://github.com/DA-testa/steks-un-iekavas-KarinaAndzane/blob/3aa98b6e74eccc5a98ba17e606ee8147dc6b5ff7/test/2'


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            # Process opening bracket, write your code here
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char,next):
                return i+1
            else:  opening_brackets_stack.pop()

    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return (opening_brackets_stack[-1].position)


def main():

    # mode=input()
    # if mode=='F':
    #     text=requests.get(url).text
    # if mode=='I':
    #     text = input()


    text=input()
    
    if text[0]=="I":
        text=input()
        
        from collections import namedtuple
import requests
url = 'https://github.com/DA-testa/steks-un-iekavas-KarinaAndzane/blob/3aa98b6e74eccc5a98ba17e606ee8147dc6b5ff7/test/2'


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            # Process opening bracket, write your code here
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char,next):
                return i+1
            else:  opening_brackets_stack.pop()

    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return (opening_brackets_stack[-1].position)


def main():

    # mode=input()
    # if mode=='F':
    #     text=requests.get(url).text
    # if mode=='I':
    #     text = input()


    text=input()
    
    if text[0]=="I":
        text.input()
#         if len(text)<3:
#            text="   "
#         text=text[2:]
#          pass
       
    if text[0]=="F":
        text=requests.get(url).text

    mismatch = find_mismatch(text)
    
    print(mismatch)

   
    # Printing answer, write your code here

if __name__ == "__main__":
    main()
       
    if text[0]=="F":
        text=requests.get(url).text

    mismatch = find_mismatch(text)
    
    print(mismatch)

   
    # Printing answer, write your code here

if __name__ == "__main__":
    main()

