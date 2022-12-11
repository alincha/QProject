from data.create import Session, RNA, AminoAcid, Gencode


def convert_dna_to_rna(dna):
    rna = ''
    with Session() as session:
        for base in dna:
            rna_base = session.query(RNA).filter(RNA.corr_dna_base == base).one()
            rna += rna_base.nucleotide
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
    with Session() as session:
        for codon in codons:
            gencode_row = session.query(Gencode).filter(Gencode.nuc1 == codon[0],
                                                        Gencode.nuc2 == codon[1],
                                                        Gencode.nuc3 == codon[2]).one()
            protein.append(gencode_row.amino_acid)

    return ''.join(protein)
