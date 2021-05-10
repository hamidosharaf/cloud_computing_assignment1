sympols = ["," ,".","'" ,"\"","?"]

book1 =  open("Beyond the Wall of Sleep.txt" , encoding="utf8")
cont = book1.read().lower()
for i in sympols:
    cont = cont.replace(i , "" , cont.count(i))
words = cont.split()
unique_words_1= set(words)
book1.close()

book2 = open("Jane Austin’s Pride and Prejudice.txt" , encoding="utf8")
cont = book2.read().lower()
for i in sympols:
    cont = cont.replace(i , "" , cont.count(i))
words = cont.split()
unique_words_2= set(words)
book2.close()


common_words = list(unique_words_1.intersection(unique_words_2))
print("The two books have ",len(common_words)," common words .")
x = str(input("do you want to print the words (Y/N)"))
if x =='Y':
    print(common_words)
    