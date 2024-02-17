import re

def markdown_to_html(markdown):
    
    # Cabeçalhos
    markdown = re.sub(r'^(#)\s+(.+)$', r'<h1>\2</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^(##)\s+(.+)$', r'<h2>\2</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^(###)\s+(.+)$', r'<h3>\2</h3>', markdown, flags=re.MULTILINE)
    
    # Bold
    markdown = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'\_\_(.+?)\_\_', r'<b>\1</b>', markdown)
    
    # Itálico
    markdown = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown)
    
    # Lista numerada
    markdown = re.sub(r'^(?=\d+\. )(.+)$', r'<li>\1</li>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'((<li>.+\n)+)', r'<ol>\1</ol>', markdown)
    
    # Imagem
    markdown = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # Link
    markdown = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown)
    
    return markdown


markdown_text = ""

with open("input.md", "r", encoding="utf-8") as md_file:
    markdown_text = md_file.read()

html_output = markdown_to_html(markdown_text)


with open("index.html", "w") as f:
    f.write(html_output)

