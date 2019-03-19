item = "-----kakka-kikka"
indentation = 0
for character in item:
    if character == "-":
        indentation += 1
    else:
        break
jep = item.count("-")
print(indentation, jep)
