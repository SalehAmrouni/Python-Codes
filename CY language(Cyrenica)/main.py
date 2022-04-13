def file(filename):
    global data
    data = open("test.cy", 'r').read()
    #print(data)


def lex(filecontents):
    global tokens
    global data
    tokens = []
    tok = ""
    string = ""
    strings=0
    num=""

    filecontents = list(filecontents)
    state = 0
    printingwait = False

    for char in filecontents:
        tok += char

        print(tok)
        if tok == " ":
            tok = ""
        elif tok == "print":
            print("found print")
            tokens.append("Print:")
            #print(tmp[0])
            tok = ""




        # elif tok == '(':
        #    print("par found")

        #    tok = ""
        #if char == '1' or tok == '2' or tok == '3' or tok == '4' or tok == '5' or tok == '6' or tok == '7' or tok == '8' or tok == '9' or tok == '0':
        #   num+= tok
        #
        #    tok=""
        #    #print(num)
        #    #rint(num+".num")

        elif char == '\'':
            print("string found")
            strings+=1
            #print(strings)

            if state==0:
                state = 1
            elif state == 1:
                #print("string found")
                state = 0
                string=""
                if strings >= 1:
                    string+= tok
                    tokens.append("string:" + string + 'r')
                    print(string)
                    strings=0
                    string=""
                    tok=""


        elif char == '\"':
            print("string found")
            strings+=1
            #print(strings)

            if state==0:
                state = 1
            elif state == 1:
                #print("string found")
                state = 0
                string=""
                if strings >= 1:
                    string+= tok
                    tokens.append("string:" + string + 'r')

                    print(string)


                    strings=0
                    string=""
                    tok=""
        elif state == 1:
            string+=tok
            tok=""

        elif tok == "\n":
            print("found indent")
            tok=""
        if tok == '1' or tok == '2' or tok == '3' or tok == '4' or tok == '5' or tok == '6' or tok == '7' or tok == '8' or tok == '9' or tok == '0':
            print("NUM")
            num+= tok

            tok=""

            #rint(num+".num")

        print(num+"r")





def parse(toks):
    i=0
    while(i <len(toks)):
        i+=1
        #print(toks[i])
        print(toks)
        #print()


def run():
    global tokens

    global data
    file("test.cy")
    lex(data)
    parse(tokens)


run()
