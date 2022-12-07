# Belajar keyword argumen list

def create_html(tag, text):
    html = f"<{tag}>{text}</{tag}>"
    return html

html = create_html("p", "Hello Python")
print(html)