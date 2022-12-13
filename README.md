This is a basic bioinformatics project written in Python3. It can convert sequence of DNA to RNA and RNA to protein.	

INPUT AND OUTPUT

To use the app, you need to enter 2 arguments in the command line.

The first argument is the type of conversion.

Enter "transcribe" (without quotes) to convert DNA to RNA. After that, put a space, then a DNA sequence in uppercase, then hit Enter.

Output will be an RNA sequence as an uppercase string.

Enter "translate" (without quotes) to convert RNA to protein. After that, put a space, then an RNA sequence in uppercase, then hit Enter.

Output will be a protein sequence as an uppercase string, using single letter amino acid notation.

An example of a command line input:

$ python app/main.py translate AUGGGGGCCAAA 

Output: 

MGAK


STRUCTURE

All project files are in the app folder.

The central files are main.py and script.py.

The project creates an SQLite database usig SQLAlchemy. All database-related files live in app/data.

Database address is stored in the config.py as DATABASE_URI.

Test cases live in test.py.




