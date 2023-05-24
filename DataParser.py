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
        temp = [value.split() for value in temp]

        #this is a bit better I guess
        for value in temp:
            if not value:
                continue
            if value[0] == "ASIN:":
                if len(value) < 2:
                    raise Exception("No ASIN specified")
                ASIN = value[1]
            elif value[0] == "similar:" and len(value) > 2:
                Similar = value[2:]
            elif value[0] == "group:":
                if len(value) < 2:
                    raise Exception("No group specified")
                Group = value[1]
        
        #removes "discontinued" products
        if not Group:
            continue

        #removes products without an co-purchased items
        if not Similar:
            continue

        ASIN2Similar[ASIN] = Similar
        ASIN2Group[ASIN] = Group

    #remove products in copurchased list that we have no information on
    for ASIN in ASIN2Similar:
        temp = []
        for prod in ASIN2Similar[ASIN]:
            if prod in ASIN2Group:
                temp.append(prod)
        ASIN2Similar[ASIN] = temp

    return ASIN2Similar, ASIN2Group


if __name__ == "__main__":
    Sim, Group = Parser("amazon-meta.txt")
    i = 0

    for key in Sim:
        print(key, Group[key], Sim[key])

        i += 1
        if i == 10:
            break