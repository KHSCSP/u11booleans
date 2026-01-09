# before running, make a prediction
# unhash each line and run again


print("\n--- part 1, using 'and' --- ")
print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)


print("\n--- part 2, using 'or' --- ")
print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)



print("\n--- part 3, weird ones! --- ")
print(True or 'bologna')
print(False or 'bologna')
print(True and 'yes')
print(False and 'yes')


# explaining those middle two from above...
if False or 'bologna':
    print("yep")
if True and 'yes':
    print("yep again")

print("\n--- any string (other than an empty string) is True ---")
print(bool("hello"))
print(bool(""))



print("\n\n--- parentheses matter (we'll fix this) ---")
happy = "yes"
fun = "no"
if happy == "yes" or happy == "y" and fun == "yes" or fun == "y":
    print("you're invited to the party!")
else:
    print("sorry, not invited")
