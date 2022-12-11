from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from data.db import Base, DNA, RNA, AminoAcid, Gencode

engine: Engine = create_engine("sqlite:///app/data/gencode.db")  # echo=True
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)

    with Session() as session:
        if session.query(DNA.nucleotide).count() != 0:
            return

        dna_bases = [
            DNA(nucleotide='A'),
            DNA(nucleotide='G'),
            DNA(nucleotide='C'),
            DNA(nucleotide='T'),
        ]
        session.add_all(dna_bases)

        rna_bases = [
            RNA(nucleotide='A', corr_dna_base='A'),
            RNA(nucleotide='G', corr_dna_base='G'),
            RNA(nucleotide='C', corr_dna_base='C'),
            RNA(nucleotide='U', corr_dna_base='T'),
        ]
        session.add_all(rna_bases)

        amino_acids = [
            AminoAcid(amino_acid='A'),
            AminoAcid(amino_acid='V'),
            AminoAcid(amino_acid='I'),
            AminoAcid(amino_acid='L'),
            AminoAcid(amino_acid='F'),
            AminoAcid(amino_acid='Y'),
            AminoAcid(amino_acid='M'),
            AminoAcid(amino_acid='C'),
            AminoAcid(amino_acid='T'),
            AminoAcid(amino_acid='S'),
            AminoAcid(amino_acid='H'),
            AminoAcid(amino_acid='K'),
            AminoAcid(amino_acid='R'),
            AminoAcid(amino_acid='W'),
            AminoAcid(amino_acid='G'),
            AminoAcid(amino_acid='D'),
            AminoAcid(amino_acid='E'),
            AminoAcid(amino_acid='Q'),
            AminoAcid(amino_acid='N'),
            AminoAcid(amino_acid='P'),
            AminoAcid(amino_acid='.'),
        ]
        session.add_all(amino_acids)

        gencode_map = {
            "A": {
                "A": {
                    "A": "K",
                    "G": "K",
                    "C": "N",
                    "U": "N"
                },
                "G": {
                    "A": "R",
                    "G": "R",
                    "C": "S",
                    "U": "S"
                },
                "C": {
                    "A": "T",
                    "G": "T",
                    "C": "T",
                    "U": "T"
                },
                "U": {
                    "A": "I",
                    "C": "I",
                    "U": "I",
                    "G": "M"
                }
            },
            "G": {
                "A": {
                    "A": "E",
                    "G": "E",
                    "C": "D",
                    "U": "D"
                },
                "G": {
                    "A": "G",
                    "G": "G",
                    "C": "G",
                    "U": "G"
                },
                "C": {
                    "A": "A",
                    "G": "A",
                    "C": "A",
                    "U": "A"
                },
                "U": {
                    "A": "V",
                    "G": "V",
                    "C": "V",
                    "U": "V"
                }
            },
            "C": {
                "A": {
                    "A": "Q",
                    "G": "Q",
                    "C": "H",
                    "U": "H"
                },
                "G": {
                    "A": "R",
                    "G": "R",
                    "C": "R",
                    "U": "R"
                },
                "C": {
                    "A": "P",
                    "G": "P",
                    "C": "P",
                    "U": "P"
                },
                "U": {
                    "A": "L",
                    "G": "L",
                    "C": "L",
                    "U": "L"
                }
            },
            "U": {
                "A": {
                    "A": ".",
                    "G": ".",
                    "C": "Y",
                    "U": "Y"
                },
                "G": {
                    "A": ".",
                    "G": "W",
                    "C": "C",
                    "U": "C"
                },
                "C": {
                    "A": "S",
                    "G": "S",
                    "C": "S",
                    "U": "S"
                },
                "U": {
                    "A": "L",
                    "G": "L",
                    "C": "F",
                    "U": "F"
                }
            }
        }
        gencode = []  # list[Gencode]
        for first_base, submap in gencode_map.items():
            for second_base, subsubmap in submap.items():
                for third_base, amino_acid in subsubmap.items():
                    gencode.append(
                        Gencode(nuc1=first_base, nuc2=second_base,
                                nuc3=third_base, amino_acid=amino_acid))
        session.add_all(gencode)
        session.commit()
