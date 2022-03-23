# while and for loops

# # while loop
# x = 0
# while (x<=5):
#     print(x)
#     x = x+1


# # for loop
# for x in range(4, 14):
#     print(x)


# Array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    # if (d=="Fri"): break # loop stops
    if (d=="Fri"): continue # skips d
    print(d)
