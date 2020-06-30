import sys

if __name__ == "__main__":

    
    outFileQ = open(sys.argv[1].replace(".qu", ".ne.qu"),"w")
    outFileR = open(sys.argv[2].replace(".re", ".ne.re"),"w")
    
    with open(sys.argv[1]) as textfile1, open(sys.argv[2]) as textfile2: 
        for x, y in zip(textfile1, textfile2):
            x = x.strip()
            y = y.strip()
            if len(x) > 0 and len(y) > 0:
                outFileQ.write(x + "\n")
                outFileR.write(y + "\n")
            else:
                print(".")
            print("\n")
    outFileQ.close();
    outFileR.close();