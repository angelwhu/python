import sys

out_file = open("out.txt", "w")

def processfile(filename):
    i = 0;
    strbuff = "";

    for line in open(filename):
        if i%5 == 0 :
            out_file.write(strbuff + "\n");   
            strbuff = "";
        strbuff = strbuff + line.strip() + ",";

        i = i + 1

    out_file.write(strbuff + "\n");   

    
if __name__ == "__main__":
    processfile(sys.argv[1]);
