# Spiderbook
### Simple, Facebook-like website (without the privacy-negation part) for members of the Spider network (found at arachnid.cc/network)

It will have a Python-based backend with an API for talking to a PostgreSQL database hosted in the author's house.

Reproduce the database:
- Create a database as the user `postgres` with the password `postgres` named "spiderbook"
- Login to `postgres`
- Run the file `db.sql` with the command `psql spiderbook -f db.sql`.
OR
- Create a database for the project
- Run the file `db.sql` with the command `psql {database_name} -f db.sql`
- Change the credentials located inside the `use_db()` function in `api.py` to what you made.