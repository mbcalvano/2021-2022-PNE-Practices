FOLDER = "../Session-04/"

gene = input("Choose a gene: ")
f = open(FOLDER + gene + ".txt")
print(f.read())