
##create a database table in RAM named roster that
##includes the fields 'name', 'species', and IQ

import sqlite3

#conn=sqlite3.connect(':memory:')
with sqlite3.connect(':memory:') as conn:
    c=conn.cursor()

c.execute("create table Roster(Name text, Species text, IQ int);")

##populate your new table with the following values:
##1 Jean-Baptiste Zorg, Human, 122
##2 Korben Dallas, Meat Popsicle, 100
##3 Ak'not, Mangalore, -5
RosterValues=(
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Ak\'not', 'Mangalore', -5)
    )

c.executemany("insert into Roster values(?,?,?)", RosterValues)

c.execute("select* from Roster")
print 'whole table:'
for row in c.fetchall():
    print row
                     
##update the species of korben dallas to be human
c.execute("update Roster set Species='Human' where Name='Korben Dallas'")

##display the names and iqs of everyone in the table
##who is classified as human
c.execute("select Name, IQ from Roster where Species='Human'")
print ''
print 'updated humans:'
for row in c.fetchall():
    print row
