import re
from weasyprint import HTML

def split_code_snippets(filename):
    with open(filename, 'r') as file:
        script_content = file.read()
    code_snippets = re.findall(r"-----(.*?)-----", script_content, re.DOTALL)
    return code_snippets

def create_pdf(questions, filename):
    html_content = "<html><body>"
    for question in questions:
        match = re.search(r'[.:?]', question)
        first_punctuation_index = match.start() if match else -1
        bold_sentence = question[:first_punctuation_index + 1] if first_punctuation_index != -1 else question
        remaining_question = question[first_punctuation_index + 1:].replace("\n", "<br>")
        html_content += f"<p><mark><u><strong>{bold_sentence}</strong></u></mark><div style='white-space: pre-wrap;'>{remaining_question}</div></p><br><hr>"
        

    html_content += "</body></html>"

    HTML(string=html_content).write_pdf(filename)


filename = "log.txt"  
code_snippets = split_code_snippets(filename)
filename = input("Enter filename for pdf: ")
create_pdf(code_snippets,filename)

