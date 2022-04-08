import base64

id = 'admin'
pw = 'nimda'

for i in range(20):
    id = id.encode('ascii')
    id = base64.b64encode(id)
    id = id.decode('ascii')

    pw = pw.encode('ascii')
    pw = base64.b64encode(pw)
    pw = pw.decode('ascii')

id.replace('1', '!')
id.replace('2', '@')
id.replace('3', '$')
id.replace('4', '^')
id.replace('5', '&')
id.replace('6', '*')
id.replace('7', '(')
id.replace('8', ')')

pw.replace('1', '!')
pw.replace('2', '@')
pw.replace('3', '$')
pw.replace('4', '^')
pw.replace('5', '&')
pw.replace('6', '*')
pw.replace('7', '(')
pw.replace('8', ')')

print(id)
print(pw)