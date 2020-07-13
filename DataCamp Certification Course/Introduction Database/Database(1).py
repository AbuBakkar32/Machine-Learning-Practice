from sqlalchemy import create_engine, MetaData, Table

metadata = MetaData()
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

####### Basic SQL ##############

census = Table('census', metadata, autoload=True, autoload_with=engine)

print(repr(census))
print(census.columns.keys())
print(engine.table_names())

stmt = 'SELECT * FROM census'
result = connection.execute(stmt).fetchall()
print(result)

first_row = result[0]
print(first_row)
print(first_row.keys())
print(connection.execute(stmt).fetchmany(size=10))



