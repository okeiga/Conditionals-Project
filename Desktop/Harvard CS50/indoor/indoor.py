comment=input ("Write any word or number that comes in mind ")
if comment ==(comment.isnumeric()):
    print(int(comment))
else:
    print(comment.lower())