# write-html.py

f = open('summerSale.html','w')

message = """<html>
<head></head>
<body><p>Stay tuned for our amazing summer sale!</p></body>
</html>"""

f.write(message)
f.close()
