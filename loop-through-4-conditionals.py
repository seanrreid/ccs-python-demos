title = "Green Lantern Corp"
counter = 0
while counter < len(title):
    # print out every other letters, but leave out spaces
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter = counter + 1
