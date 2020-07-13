from sqlalchemy import create_engine, MetaData, Table, select, and_, desc, func, case

metadata = MetaData()
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])
result = connection.execute(stmt).first()

for key in result.keys():
    print(key, getattr(result, key))