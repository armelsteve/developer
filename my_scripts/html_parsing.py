from requests_html import HTML

with open('file.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('p')

for i in match:
    print(i.text)

#removing emails in the list
match.pop(1)
match.pop(2)
print('###################################')
for i in match:
   print(i.text)