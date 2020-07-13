from sqlalchemy import create_engine, MetaData, Table, select, and_, desc, func

metadata = MetaData()
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

# stmt = select([census])
# stmt = stmt.where(census.columns.state.startswith('NEw'))
# for result in connection.execute(stmt):
#     print(result.state, result.pop2000)


# states = ['New York', 'California', 'Texas']
# stmt = select([census])
# stmt = stmt.where(census.columns.state.in_(states))
#
# for result in connection.execute(stmt):
#     print(result.state, result.pop2000)


# stmt = select([census])
# stmt = stmt.where(
#     # The state of California with a non-male sex
#     and_(census.columns.state == 'California',
#          census.columns.sex != 'M'
#          )
# )
#
# for result in connection.execute(stmt):
#     print(result.age, result.sex)


# *********************** Ordering Query Result *********************

#### Order by Single Columns
# stmt = select([census.columns.state])
# rev_stmt = stmt.order_by(desc(census.columns.state))
# rev_results = connection.execute(rev_stmt).fetchall()
# print(rev_results[:10])


#### Order by Multiple Columns
# stmt = select([census.columns.state, census.columns.age])
# stmt = stmt.order_by(census.columns.state, desc(census.columns.age))
# results = connection.execute(stmt).fetchall()
# print(results[0:20])


# *********************** Count Sum And Grouping Data *********************

# stmt = select([func.count(census.columns.state.distinct())])
# distinct_state_count = connection.execute(stmt).scalar()
# print(distinct_state_count)


# stmt = select([census.columns.state, func.count(census.columns.age)])
# stmt = stmt.group_by(census.columns.state)
# results = connection.execute(stmt).fetchall()
# print(results)


# pop2008_sum = func.sum(census.columns.pop2008).label('population')
# stmt = select([census.columns.state, pop2008_sum])
# stmt = stmt.group_by(census.columns.state)
# results = connection.execute(stmt).fetchall()
#
# print(results)
# print(results[0].keys())









