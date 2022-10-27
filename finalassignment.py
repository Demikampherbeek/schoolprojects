import re
import sys 
 
PATTERN = ["/s{5}","/s{10}"]
NUCLEOTIDES = ["a","t","c","g"]



def clustering_lines(filename):
    definition = ""

    with open(filename) as file:
        for line in file:
            line = line.strip('\n')
            if 'DEFINITION' in line:
                definition = "".join(map(str,line[0:]))
        print(definition)

        with open("text.txt","w") as file:
            file.write(definition)




def main():
    clustering_lines('/homes/dckampherbeek/Downloads/CFTR_mRNA.gb')

main()

