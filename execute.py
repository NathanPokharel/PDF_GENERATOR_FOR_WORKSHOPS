import re

def split_code_snippets(filename):
    with open(filename, 'r') as file:
        script_content = file.read()
    code_snippets = re.findall(r"'''(.*?)'''", script_content, re.DOTALL)
    return code_snippets

filename = input("Enter your python filename: ")  
code_snippets = split_code_snippets(filename)
for index,snippet in enumerate(code_snippets):
    print("-----")
    print(snippet)
    exec(snippet)
    print("-----")

