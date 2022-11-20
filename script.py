from data import gencode


def convert_dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    return rna


def convert_rna_to_protein(rna):
    codons = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        if len(codon) != 3:
            break
        else:
            codons.append(codon)
    protein = []
    for codon in codons:
        protein.append(gencode[codon])
    return ''.join(protein)
