from collections import defaultdict

tree = lambda: defaultdict(tree)


users = tree()
users['harold']['username'] = 'chopper'
users['matt']['password'] = 'hunter2'
