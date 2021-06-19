opened_file = open("23Left.txt")
from csv import reader
read_file = reader(opened_file, dialect="excel-tab")
data = list(read_file)
rsDict = {}
duplicates = 0

for line in data[1:]:
    rs = line[0]
    if rs in rsDict:
        rsDict[rs] += 1
        duplicates += 1
    else:
        rsDict[rs] = 1

opened_file = open("AncestryRight.txt")
read_file = reader(opened_file, dialect="excel-tab")
dataAncestry = list(read_file)

for line in dataAncestry[1:]:
    rs = line[0]
    if rs in rsDict:
        rsDict[rs] += 1
        duplicates += 1
    else:
        rsDict[rs] = 1
        chromosome = line[1]
        position = line[2]
        genotype = line[3]
        extrallele = line[4]
        genotype = genotype+extrallele
        formattedLine = [rs, chromosome, position, genotype]
        data.append(formattedLine)

#print(duplicates)

with open('combined.txt', 'w') as f:
    for line in data:
        f.write('\t'.join(line))
        f.write('\n')
