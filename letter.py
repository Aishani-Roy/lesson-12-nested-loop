word=input("enter word")
character=input("enter character")
count=0
for letter in word:
    if letter==character:
        count+=1
print(f"{character} appeared {count} many times in {word}")
