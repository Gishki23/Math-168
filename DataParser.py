def Parser(file):
    #two dictionaries to make ASIN -> Co-Purchase and ASIN -> Product Group
    ASIN2Similar = {}
    ASIN2Group = {}

    f = open(file, "r")
    fullText = f.read()
    f.close()

    products = fullText.split("\n\n")[1:]
    
    for prod in products:
        ASIN = ""
        Group = ""
        Similar = []

        temp = prod.split("\n")
        temp = [value.split(" ") for value in temp]

        #this is really janky ngl will probably need to take a look at it later TT
        for value in temp:
            if value[0] == "ASIN:":
                ASIN = value[1]
            elif len(value) >= 6 and value[2] == "similar:":
                Similar = value[5::2]
            elif len(value) >= 4 and value[2] == "group:":
                Group = value[3]
        
        ASIN2Similar[ASIN] = Similar
        ASIN2Group[ASIN] = Group

    return ASIN2Similar, ASIN2Group


if __name__ == "__main__":
    Sim, Group = Parser("amazon-meta.txt")
    i = 0

    for key in Sim:
        print(key, Group[key], Sim[key])

        i += 1
        if i == 10:
            break