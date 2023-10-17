import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
# local_filename = "Pima_Indians.csv"
#
# response = requests.get(url)
# with open(local_filename, 'wb') as file:
#     file.write(response.content)


df = pd.read_csv('Pima_Indians.csv', header=None)
df.columns = ['Number of times pregnant', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test.'
    , 'Diastolic blood pressure (mm Hg)', 'Triceps skinfold thickness (mm)', '2-Hour serum insulin (mu U/ml)',
              'Body mass index (weight in kg/(height in m)^2)', 'Diabetes pedigree function', 'Age (years)',
              'infection']

df["infection"] = df['infection'].replace(1, "Infected").replace(0, "Not Infected")

print(df)

features=df.columns
for column in features[:-1]:
    plt.figure()  # Create a new figure for each histogram
    df[column].plot(kind='hist', title="Histogram")  # Plot the histogram
    plt.xlabel(column)  # Set the x-axis label
    plt.ylabel('Intensity')  # Set the y-axis label
    plt.show()
