# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells =list(map(lambda item: item +'!!!', spells))
shout = list(map(lambda x: {spells.index(x) : x }, spells))

# Print the result
print(shout_spells)
print(shout)
