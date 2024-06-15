"""
Author: Abu Bakkar Siddikk
Date: 2024-06-14
Description: String Formatting
"""

# https://docs.python.org/3/library/string.html#formatspec
# https://towardsdatascience.com/apply-functions-to-pandas-dataframe-using-map-apply-applymap-and-pipe-9571b1f1cb18
# https://www.geeksforgeeks.org/python-map-function/
# https://www.geeksforgeeks.org/python-apply-function/
# https://www.geeksforgeeks.org/python-applymap-function/
# https://www.geeksforgeeks.org/python-pipe-function/
# https://www.geeksforgeeks.org/python-lambda-function/
# https://www.geeksforgeeks.org/python-filter-function/
# https://www.geeksforgeeks.org/python-reduce-function/
# https://www.geeksforgeeks.org/python-zip-function/
# https://www.jcchouinard.com/pandas-excel/
# https://www.jcchouinard.com/30-days-of-pandas/
# https://towardsdatascience.com/3-methods-for-aggregating-data-with-python-pandas-14ceb75b6f6e
# https://towardsdatascience.com/create-a-butterfly-chart-easily-using-plotly-aa3d43ba410d
# https://medium.com/@avinashchandrana/comparison-of-matplotlib-vs-seaborn-and-plotly-on-a-dataset-for-beginners-92a7e8197dc6
import decimal

text = "hello world"
print(f"{text:^20}")

number = 1234567890
print(f"{number:,}")

number = 123
print(f"{number:08}")

number = 254.3463
print(f"{f'${number:.3f}':}")


# x, y = "Hello", "World"
#
# print(f"{x} {y}")  # 39.6 nsec per loop - Fast!
# print(x + " " + y)  # 43.5 nsec per loop
# print(" ".join((x, y)))  # 58.1 nsec per loop
# print("%s %s" % (x, y))  # 103 nsec per loop
# print("{} {}".format(x, y))  # 141 nsec per loop
# print(Template("$x $y").substitute(x=x, y=y))  # 1.24 usec per loop - Slow!


value = decimal.Decimal("42.12345")
print(f"output: {value:{0}.{3}}")

value = decimal.Decimal("42.12345")
print(f'Result: {value:{"4.3" if value < 100 else "8.3"}}')

value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.3"}}')


print(f"{(lambda x: x**2)(3)}")
