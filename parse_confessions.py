# import re

# hardcoding first confession number in file
number = 20584
confessions = []
with open('mit_confessions.txt', "r") as f:
    lines = f.readlines()
    in_confession = False
    confession = ""
    for line in lines:
        confession_number = "#" + str(number)
        if confession_number in line:
            # Found new confession, confession_number separated by confession
            # with space
            confession = line[len(confession_number) + 1:]
            number -= 1
            in_confession = True
        else:
            if in_confession:
                if "Comment" not in line:
                    confession += line
                else:
                    confessions.append(confession)
                    confession = ""
                    in_confession = False

f.close()
print(confessions)
# write to output
confessed = open('filtered_mit_confessions', "w")

for confession in confessions:
    confession = confession.replace("\n", "")
    confessed.write(confession + "\n")

confessed.close()
