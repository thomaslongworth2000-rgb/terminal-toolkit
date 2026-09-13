shopping = ["milk", "bread", "eggs"]

print(shopping[0])        # milk — counting starts at 0
print(len(shopping))      # 3

shopping.append("cheese") # add to the end
shopping.remove("bread")  # take one out

for item in shopping:
    print(item)
