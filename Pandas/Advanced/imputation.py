import pandas as pd
import datawig

data = pd.read_csv("train.csv")

df_train, df_test = datawig.utils.random_split(data)

# Initialize a SimpleImputer model
imputer = datawig.SimpleImputer(
    input_columns=['Pclass', 'SibSp', 'Parch'],  # column(s) containing information about the column we want to impute
    output_column='Age',  # the column we'd like to impute values for
    output_path='imputer_model'  # stores model data and metrics
)

# Fit an imputer model on the train data
imputer.fit(train_df=df_train, num_epochs=50)

# Impute missing values and return original dataframe with predictions
imputed = imputer.predict(df_test)
