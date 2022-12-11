from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DNA(Base):
    __tablename__ = "dna_bases"
    nucleotide = Column(String(1), primary_key=True)

    def __str__(self):
        return f"{self.nucleotide}"


class RNA(Base):
    __tablename__ = "rna_bases"
    nucleotide = Column(String(1), primary_key=True)
    corr_dna_base = Column(String(1), ForeignKey("dna_bases.nucleotide"), nullable=False)

    def __str__(self):
        return f"{self.nucleotide}"


class AminoAcid(Base):
    __tablename__ = "amino_acids"
    amino_acid = Column(String(5), primary_key=True)


class Gencode(Base):
    __tablename__ = "gencode"
    nuc1 = Column(String(1), ForeignKey("rna_bases.nucleotide"), primary_key=True)
    nuc2 = Column(String(1), ForeignKey("rna_bases.nucleotide"), primary_key=True)
    nuc3 = Column(String(1), ForeignKey("rna_bases.nucleotide"), primary_key=True)
    amino_acid = Column(String(5), ForeignKey("amino_acids.amino_acid"), nullable=False)
