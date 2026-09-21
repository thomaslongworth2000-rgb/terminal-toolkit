names = ["Tom", "James", "Matthew", "Aaron", "Peter", "John", "Paul", "George", "Ringo"]


# writing
with open("notes.txt", "w") as f:
    f.write(", ".join(names))

# reading
with open("notes.txt", "r") as f:
    contents = f.read()
    print(contents) 