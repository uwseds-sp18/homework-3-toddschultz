"""
Homework 3
Todd Schultz
"""


def create_dataframe(pathname):
    """ 
    Create dataframe from the database file
    Syntax
    df = create_dataframe(pathname)
    Inputs
    name = path name to the folder containing class.db
    Outputs
    df = constructed dataframe from the database file
    """
    import os
    import sqlite3
    import pandas as pd
    
	# Test for valid path name
    if not os.path.isdir(pathname):
        raise ValueError('Invalid path provided.')
	
    # create full file name and test for valid database
    dbname = 'class.db'
    dbname = os.path.join(pathname, dbname)
    if not os.path.isfile(dbname):
        raise ValueError('File ''class.db'' not found in specified path.')
    
    # establish database connection
    try:
        conn = sqlite3.connect(dbname)
    except ValueError:
        print("Could not connect to database file.")
    
    # Create, execute, and append query results
    sqltxt = "select video_id, category_id, 'ca' as language from CAvideos;"
    df = pd.read_sql_query(sqltxt, conn)
    
    sqltxt = "select video_id, category_id, 'de' as language from DEvideos;"
    df = df.append(pd.read_sql_query(sqltxt, conn))
    
    sqltxt = "select video_id, category_id, 'fr' as language from FRvideos;"
    df = df.append(pd.read_sql_query(sqltxt, conn))
    
    sqltxt = "select video_id, category_id, 'gb' as language from GBvideos;"
    df = df.append(pd.read_sql_query(sqltxt, conn))
    
    sqltxt = "select video_id, category_id, 'us' as language from USvideos;"
    df = df.append(pd.read_sql_query(sqltxt, conn))
    
    # close connection to database
    conn.close()
    
    return df
