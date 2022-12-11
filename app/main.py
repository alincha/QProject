import data.create
import sys
import script

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        exit(1)
    op, arg = args

    Session = data.create.init_db()
    if op == 'transcribe':
        print(script.convert_dna_to_rna(Session, arg))
    elif op == 'translate':
        print(script.convert_rna_to_protein(Session, arg))
    else:
        exit(1)

    # tests.test_convert_dna_to_rna(Session)
    # tests.test_convert_rna_to_protein(Session)
