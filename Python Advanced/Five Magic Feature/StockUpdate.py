import yfinance as yf

# q = yf.Ticker("AAPL")
# # print(q.info['forwardPE'])
# # print(q.info['dividendRate'])
# # print(q.dividends)
# data = yf.download("AMZN AAPL GOOG", start="2017-01-01",
#                     end="2017-04-30", group_by='tickers')
#
# print(data)
#
# data_frame = q.history("1d")
# price = data_frame["Close"].values[0]
# print(f'Apple current stock price: {price} USD')

import pandas as pd

tickers_list = ["aapl", "goog", "amzn", "BAC", "BA"]  # example list
tickers_data = {}  # empty dictionary

for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)

    # convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Recent"]

    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp

print(tickers_data)
combined_data = pd.concat(tickers_data)
combined_data = combined_data.reset_index()
print(combined_data)

# del combined_data["level_1"] # clean up unnecessary column
# combined_data.columns = ["Ticker", "Attribute", "Recent"] # update column names
#
# combined_data


# employees = combined_data[combined_data["Attribute"]=="fullTimeEmployees"].reset_index()
# del employees["index"] # clean up unnecessary column
#
# employees


# employees_sorted = employees.sort_values('Recent',ascending=False)
# employees_sorted


# aapl_historical = aapl.history(period="max", interval="1wk")
# aapl_historical

# opt = aapl.option_chain(date='2020-07-24')
# print(opt.calls)
# print(opt.puts)