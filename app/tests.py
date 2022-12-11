from script import *

transcribe_correct_test_cases = {
    'ATTTGGCTACTAACAATCTA': 'AUUUGGCUACUAACAAUCUA',
    'GTTGTAATGGCCTACATTA': 'GUUGUAAUGGCCUACAUUA',
    'CAGGTGGTGTTGTTCAGTT': 'CAGGUGGUGUUGUUCAGUU',
    'GCTAACTAAC': 'GCUAACUAAC',
    'GCTAACTAACATCTTTGGCACTGTT': 'GCUAACUAACAUCUUUGGCACUGUU',
    'TATGAAAAACTCAAA': 'UAUGAAAAACUCAAA',
    'CCCGTCCTTGATTGGCTTGAAGAGAAGTTT': 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
}

convert_rna_to_protein_test_cases = {
    'AUUUGGCUACUAACAAUCUA': 'IWLLTI',
    'GUUGUAAUGGCCUACAUUA': 'VVMAYI',
    'CAGGUGGUGUUGUUCAGUU': 'QVVLFS',
    'GCUAACUAAC': 'AN.',
    'GCUAACUAACAUCUUUGGCACUGUU': 'AN.HLWHC',
    'UAUGAAAAACUCAAA': 'YEKLK',
    'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU': 'PVLDWLEEKF'
}


def test_convert_dna_to_rna(Session: sqlalchemy.orm.sessionmaker):
    failed_tests = 0
    for key, expected in transcribe_correct_test_cases.items():
        got = convert_dna_to_rna(Session, key)
        if not (expected == got):
            print(f'invalid convert_dna_to_rna result for {key}; expected {expected}, got {got}')
            failed_tests += 1
    print(f'Number of failed tests of convert_dna_to_rna:{failed_tests}')


def test_convert_rna_to_protein(Session: sqlalchemy.orm.sessionmaker):
    failed_tests = 0
    for key, expected in convert_rna_to_protein_test_cases.items():
        got = convert_rna_to_protein(Session, key)
        if not (expected == got):
            print(f'invalid rna_to_protein result for {key}; expected {expected}, got {got}')
            failed_tests += 1
    print(f'Number of failed tests of convert_rna_to_protein:{failed_tests}')
