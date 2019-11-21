""" reading the file dna.fasta and creating the dictionary which contains:
    - names of a genes as keys 
    - DNA as values """
with open('dna.fasta', 'r+') as dna_file:
    dna_dictionary = {}
    for line in dna_file:
        if line[0] == ">":
            gene = line.strip()
            dna_dictionary[gene] = ''
        else:
            dna_dictionary[gene] += f'{line.strip()}'


def count_nucleotides(dna):
    """returning the dictionary which contains:
    - names of a genes as keys 
    - number of each nucleotide as values
    (if we have DNA as dictionary) """
    num_of_nucleotides = {}
    for gene in dna: 
        num_of_nucleotides_gene = '' # number of each nucleotide for the gene
        for nucleotide in 'ATGC':
            if nucleotide in 'ATG':	
                num_of_nucleotide = dna[gene].count(nucleotide)
                num_of_nucleotides_gene += f'{nucleotide}' \
                                           f' - {num_of_nucleotide}, '
            else:
                num_of_nucleotide = dna[gene].count(nucleotide)
                num_of_nucleotides_gene += f'{nucleotide}' \
                                           f' - {num_of_nucleotide}'
        num_of_nucleotides[gene] = num_of_nucleotides_gene
    return num_of_nucleotides


def translate_from_dna_to_rna(dna):
    """returning the dictionary which contains:
    - names of a genes as keys 
    - RNA as values
    (if we have DNA as dictionary) """
    dna_to_rna = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'} # DNA to RNA mapping
    rna = {}
    for gene, dna_code in dna.items():
        rna_code = ''
        for nucleotide in dna_code:
            for nucleotide_dna in dna_to_rna:
                if nucleotide == nucleotide_dna:
                    rna_code += f'{dna_to_rna[nucleotide_dna]}'
        rna[gene] = rna_code
    return(rna)


def translate_rna_to_protein(rna):
    """returning the dictionary which contains:
    - names of a genes as keys 
    - proteins as values
    (if we have RNA as dictionary) """
    codon_to_protein_dict = {} # dictionary for translation codons to proteins
    with open('./rna_codon_table.txt', 'r') as codon_to_protein: 
        for line in codon_to_protein:
            line = line.split() 
            for elem in line: 
                if line.index(elem) % 2 == 0:
                    codon_to_protein_dict[elem] = line[line.index(elem) + 1]

    protein = {}
    for gene, rna_code in rna.items():
        protein_gene = '' # proteins for the gene
        j = 0
        for i in range(0, int(len(rna_code)/3)):
            protein_gene += codon_to_protein_dict[rna_code[j : j + 3 : 1]]
            j += 3
        protein[gene] = protein_gene
    return(protein)


""" writing the statistics of nucleotides in dna to separate file """
nucleotides_statistic = count_nucleotides(dna_dictionary)
with open('1_Statistics_of_nucleotides.txt', 'w') as num_of_nucleotides_file:
    for gene, num_of_nucleotides_gene in nucleotides_statistic.items():
        num_of_nucleotides_file.write(f'{gene}: {num_of_nucleotides_gene}\n')


""" writing the results of DNA to RNA translation to separate file """
rna_results = translate_from_dna_to_rna(dna_dictionary)
with open('2_DNA_to_RNA_translation.txt', 'w') as rna_file:
    for gene, rna_code in rna_results.items():
        rna_file.write(f'{gene}\n{rna_code}\n')


""" writing the results of RNA to protein translation to separate file """
protein_results = translate_rna_to_protein(rna_results)
with open('3_RNA_to_protein_translation.txt', 'w') as protein_file:
    for gene, protein_gene in protein_results.items():
        protein_file.write(f'{gene}\n{protein_gene}\n')