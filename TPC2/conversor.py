import re

with open("input.md", "r", encoding="utf-8") as md:
    text = md.read()

    
# Cabeçalhos
text = re.sub(r'^(#)\s+(.+)$', r'<h1>\2</h1>', text, flags=re.MULTILINE)
text = re.sub(r'^(##)\s+(.+)$', r'<h2>\2</h2>', text, flags=re.MULTILINE)
text = re.sub(r'^(###)\s+(.+)$', r'<h3>\2</h3>', text, flags=re.MULTILINE)
    
# Bold
text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
text = re.sub(r'\_\_(.+?)\_\_', r'<b>\1</b>', text)
    
# Itálico
text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    
# Lista numerada
text = re.sub(r'^(?=\d+\. )(.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)
text = re.sub(r'((<li>.+\n)+)', r'<ol>\1</ol>', text)
    
# Imagem
text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', text)

# Link
text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    
with open("index.html", "w") as f:
    f.write(text)

