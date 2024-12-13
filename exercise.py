import sqlite3
import pandas as pd

conn = sqlite3.connect('books.db')
curs = conn.cursor()

pd.read_sql('SELECT last FROM authors ORDER BY last DESC', conn)

pd.read_sql('SELECT title FROM titles ORDER BY title ASC', conn)

pd.read_sql('SELECT title, copyright, isbn, FROM titles INNER JOIN author_ISBN ON isbn = authors.isbn ORDER BY title ASC')

curs = curs.execute("""INSERT INTO authors (first, last) VALUES ('Jon', 'Spansail')""")

#adding new title for author into isbn table and titles
curs = curs.execute("""INSERT INTO author_ISBN (isbn) VALUES ('3128987601')""")
curs = curs.execute("""INSERT INTO tables (isbn, title, edition, copyright) VALUES ('3128987601', 'Renegade: The Jason Dent Story', '1', '2024 Bloodmoon LTSS')""")