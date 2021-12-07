import os
import form

file_item = form['filename']

if file_item.filename:
    fn = os.path.basename(file_item.filename)

    open(fn, 'wb').write(file_item.file.read())
    message = "The file" " was uploaded successfully"
else:
    message = "no file was uploaded'"

print("""\
Content-Type: text/html\n
<html>
<body>
<p>%s</p>
</body>
<html> 
""" % (message,))
