
#Genoma B subtilis
sequence_file = 'Bsubtilis.gb'


subtilis_gene_set = set()
subtilis_gene_list = []


with open(sequence_file) as file:
    for line in file:
#        line = line.rstrip()
#        print(line)
        if '/gene=' in line:
            line = line.strip()
            gene = line[7:-1]
            print(line)
            print(gene)
            subtilis_gene_set.add(gene)
            subtilis_gene_list.append(gene)
    pass

#Genome coli
sequence_file = 'Ecoli.gb'


Ecoli_gene_set = set()
Ecoli_gene_list = []


with open(sequence_file) as file:
    for line in file:
#        line = line.rstrip()
#        print(line)
        if '/gene=' in line:
            line = line.strip()
            gene = line[7:-1]
            print(line)
            print(gene)
            Ecoli_gene_set.add(gene)
            Ecoli_gene_list.append(gene)
    pass