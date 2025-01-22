contents =["afds", "faeew", "dvdfdf"]
filenames =["doc.txt", "report.txt", "presentation.txt"]

for item, content in zip(filenames, contents):
    file = open(f"files/{item}", 'w')

    file.write(content)
