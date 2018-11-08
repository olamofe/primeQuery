def primeQuery(n, first, second, values, queries):
    #def treezyx(n, first, second, value, node):
    if n != len(values):
        raise ValueError("number of nodes and values not equal")
    else:
        node = queries
        value = values
        pairs = []
        for x, y in zip(first, second):
            pair = [x,y]
            pairs.append(pair)
        dic = {}
        for index in range(1, n+1):
            dic[index] = []

        tmp = []
        savedpairs = []
        print(pairs)
        for x in pairs:
            savedpairs.append(x)
        #print("pairs before while loop ", pairs)
        while savedpairs != []:
            pairtmp = savedpairs
            #print("while loop of pairs", pairtmp)
            for x in pairtmp:
                if 1 in x:
                    if x.index(1) == 0:
                        rootchild = x[1]
                        pairtmp.remove(x)
                        pairs.remove(x)

                    else:
                        rootchild = x[0]
                        pairtmp.remove(x)
                        pairs.remove(x)

                    tmp.append(rootchild)
                else:
                    pairtmp.remove(x)
            
            savedpairs = pairtmp
        dic[1] = tmp
        #print(dic)
        index = 1
        #print("dic ", dic, " and pairs ", pairs)
        def createdic(index, dic, listy):
            stack = []
            tmp = []
            currentlist = dic.get(index)
            if currentlist == []:
                return
            for x in currentlist:
                stack.append(x)
            while(stack != []):
                for node in stack[::-1]:
                    index = 0
                    while index < len(listy):
                        nodepairs = listy[index]
                        if node in nodepairs:
                            if nodepairs.index(node) == 0:
                                nodecomp = nodepairs[1]
                            else:
                                nodecomp = nodepairs[0]
                            tmp.append(nodecomp)
                            listy.remove(nodepairs)

                            index -= 1
                        index += 1
                    dic[node] = tmp
                    createdic(node, dic, listy)
                    stack.pop()
                    tmp = []
            print(dic)
            return dic
        treex = createdic(index, dic, pairs)

        tmpdic = {}
        for keys, values in treex.items():
            tmpdic[keys] = values

        #print(dic)

        #prime = countNode(tmpdic, node, value)
        #print(prime)
        #print(node, " ",queries, "in function global")
        tmp = []
        for node in queries:
            #print("in for loop", node, queries)
            global countex
            global primecounter
            countex = 0
            primecounter = 0
            def prime(x):
                primelist = [2, 3, 5, 7]
                stack = [True]
                if x == 1 or x == 0:
                    return False
                if x in primelist:
                    return True
                for ele in primelist:
                    if(x%ele == 0):
                        stack.insert(0, False)
                        stack.pop

                if stack[0] == False:
                    return False
                else:
                    return True
            def countNode(dic, node, value):
                #print("in countNode", node, value)
                global countex
                global primecounter
                #print("countex ", countex, " primecounter ", primecounter, " in countNode for node", node)

                #print(node, value)
                if(node not in dic.keys()):
                    print(node, " not in dic tmp is ",tmp )
                    pass
                else:
                    valueAtNode = dic.get(node)
                    valueinsidenode = value[node-1]

                    if(prime(valueinsidenode) == True):
                        primecounter += 1

                    stack = []
                    if valueAtNode == []:
                         return primecounter

                    for x in valueAtNode:
                        stack.append(x)
                    while stack != []:
                        for x in stack[::-1]:
                            countex = countex + 1
                            countNode(dic, x, value)
                            stack.pop()
                return primecounter
            
            if(node in dic.keys()):
                prime = countNode(tmpdic, node, value)
                #print(prime, " prime appended for", node )
                tmp.append(prime)
        
        total = ""
        for x in tmp:
            if x!=" ":
                x = str(x)
                total = total + x
        tmp = total
        tmp = tmp.split()    
        tmp = '\n'.join(tmp)
        print(tmp)
        return tmp