# SQLight #

SQL Wrapper for Python

[My Discord](https://discordapp.com/users/731128007388823592/ "Moritz⚜#6969")

## Instructions ##

### Install: ###

```py
pip install sqlight
# or
pip install -i https://test.pypi.org/simple/ sqlight
```

### Information: ###

```
# Database object
Database.connect() -> None: connect to database
Database.close() -> None: close database
Database.table() -> Table: create Table object
Database.get_tables() -> list: list all Tables

# Table object
Table.get_attributes() -> list: list all row names
Table.fetch_all() -> list: get content of table
Table.fetch_rows(list | str) -> list: get rows
Table.insert(dict) -> None: instert data into table
Table.delete() -> None: delete table
```

### Run Program: ###

```py
# import webmath and asyncio
import asyncio
from sqlight import sqlight

# connect to db
db = sqlight.Database("database.db")
asyncio.run(db.connect())

# connect to table
mytable = asyncio.run(db.table("tablename"))

# get content of table
content = asyncio.run(mytable.fetch_all())
print(content)
```

### OUTPUT: ###
```py
[(0, 'id', 'INTEGER', 0, None, 0), (1, 'text', 'TEXT', 0, None, 0), (2, 'other', 'TEXT', 0, None, 0)]
```

## Ride the space skyway home to 80s Miami ##
