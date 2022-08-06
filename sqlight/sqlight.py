import aiosqlite

class Table:
    """
    Table class
    ...

    Attributes
    ----------
    connection : aiosqlite.Connection
        Connection to the database
    name : str
        Name of the table

    Methods
    ----------
    fetch_all()
        Fetch all rows from the table
    fetch_row(row: str)
        Fetch a row from the table
    insert(data: dict)
        Insert a row into the table
    """
    
    def __init__(self, connection, name) -> None:
        """
        Parameters
        ----------
        connection : aiosqlite.Connection
            Connection to the database
        name : str
            Name of the table
        """
        
        self.connection = connection
        self.name = name
        
    async def get_attributes(self) -> list:
        """
        Get the attributes of the table
        
        Returns
        ----------
        list
        """
        cursor = await self.connection.execute(f"PRAGMA table_info({self.name})")
        return await cursor.fetchall()

    async def fetch_all(self) -> list:
        """
        Fetches all rows from the table
        
        Returns
        ----------
        list
        """
        
        cursor = await self.connection.execute(f"SELECT * FROM {self.name}")
        return await cursor.fetchall()
    
    async def fetch_rows(self, rows: list | str) -> list:
        """
        Fetches rows from the table
        
        Parameters
        ----------
        rows : list
        
        Returns
        ----------
        list
        """
        if isinstance(rows, list):
            rows = ", ".join(rows)
            
        cursor = await self.connection.execute(f"SELECT {rows} FROM {self.name}")
        return await cursor.fetchall()
    
    async def insert(self, data: dict) -> None:
        """
        Inserts a row into the table
        
        Parameters
        ----------
        data: dict
        
        Returns
        ----------
        None
        """
        
        keys = ", ".join(["?"] * len(data))
        await self.connection.execute(f"INSERT INTO {self.name} VALUES ({keys})", tuple((data.values())))
        await self.connection.commit()
    
    async def delete(self) -> None:
        """
        Delete the database
        
        Returns
        ----------
        None
        """
        
        await self.connection.execute(f"DROP TABLE IF EXISTS {self.name}")
        await self.connection.commit()
        await self.connection.close()

class Database:
    """
    Database class
    ...

    Attributes
    ----------
    path : str
        Path to the database

    Methods
    ----------
    connect()
        Connect to the database
    table(name: str)
        Get a table object
    get_tables()
        Get all tables in the database
    """
    
    def __init__(self, path: str) -> None:
        """
        Parameters
        ----------
        path : str
            Path to the database
        """
        
        self.path = path
    
    async def connect(self) -> None:
        """
        Connect to the database

        Returns
        ----------
        None
        """
        
        self.connection = await aiosqlite.connect(self.path)
        
    async def close(self) -> None:
        """
        Close the database connection
        
        Returns
        ----------
        None
        """
        
        await self.connection.close()
        
    async def table(self, name: str) -> Table:
        """
        Get a table object
                
        Parameters
        ----------
        name : str
        
        Returns
        ----------
        Table
        """
        
        return Table(self.connection, name)

    async def get_tables(self) -> list:
        """
        Get all tables in the database

        Returns
        ----------
        list
        """
        
        cursor = await self.connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return await cursor.fetchall()