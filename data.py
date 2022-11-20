gencode = {}
for key in ['UUC', 'UUU']:
    gencode[key] = 'F'
for key in ['UUA', 'UUG', 'CUA', 'CUG', 'CUC', 'CUU']:
    gencode[key] = 'L'
for key in ['UCA', 'UCG', 'UCU', 'UCC']:
    gencode[key] = 'S'
for key in ['UAU', 'UAC']:
    gencode[key] = 'Y'
for key in ['UAA', 'UAG', 'UGA']:
    gencode[key] = '.'
for key in ['UGU', 'UGC']:
    gencode[key] = 'C'
gencode['UGG'] = 'W'
gencode['AUG'] = 'M'
for key in ['CCA', 'CCG', 'CCC', 'CCU']:
    gencode[key] = 'P'
for key in ['CAU', 'CAC']:
    gencode[key] = 'H'
for key in ['CAA', 'CAG']:
    gencode[key] = 'Q'
for key in ['CGA', 'CGG', 'CGC', 'CGU', 'AGG', 'AGA']:
    gencode[key] = 'R'
for key in ['AUA', 'AUU', 'AUC']:
    gencode[key] = 'I'
for key in ['ACA', 'ACC', 'ACG', 'ACU']:
    gencode[key] = 'T'
for key in ['AAC', 'AAU']:
    gencode[key] = 'N'
for key in ['AAA', 'AAG']:
    gencode[key] = 'K'
for key in ['AGC', 'AGU']:
    gencode[key] = 'S'
for key in ['AGG', 'AGA']:
    gencode[key] = 'R'
for key in ['GUA', 'GUU', 'GUC', 'GUG']:
    gencode[key] = 'V'
for key in ['GCA', 'GCU', 'GCC', 'GCG']:
    gencode[key] = 'A'
for key in ['GAU', 'GAC']:
    gencode[key] = 'D'
for key in ['GAA', 'GAG']:
    gencode[key] = 'E'
for key in ['GGA', 'GGG', 'GGC', 'GGU']:
    gencode[key] = 'G'
