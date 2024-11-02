answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
filtered = answer.strip().lower()
if filtered == "42":
    print("yes")
elif filtered == "forty-two":
    print("yes")
elif filtered == "forty two":
    print("yes")
else:
    print("no")



