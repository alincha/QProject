import data.create
import tests

if __name__ == '__main__':
    data.create.init_db()

    tests.test_convert_dna_to_rna()
    # tests.test_convert_rna_to_protein()
