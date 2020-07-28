import pyshorteners as ps
import clipboard

clipboard.copy(ps.Shortener().tinyurl.short(input("Enter URL: ")))
print("\n--> {}\nShort URL is copied to clipboard".format(clipboard.paste()))
