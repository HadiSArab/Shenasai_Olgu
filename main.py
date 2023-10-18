import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


###########################
#Donwload and save database and set as dataframe



# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
# local_filename = "Pima_Indians.csv"
#
# response = requests.get(url)
# with open(local_filename, 'wb') as file:
#     file.write(response.content)


df = pd.read_csv('Pima_Indians.csv', header=None)
df.columns = ['Number of times pregnant', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test'
    , 'Diastolic blood pressure (mm Hg)', 'Triceps skinfold thickness (mm)', '2-Hour serum insulin (mu U/ml)',
              'Body mass index (weight in kg/(height in m)^2)', 'Diabetes pedigree function', 'Age (years)',
              'infection']

df["infection"] = df['infection'].replace(1, "Infected").replace(0, "Not Infected")
print(df)


################################
#Plot all histograms
features = df.columns
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.ravel()
for i, column in enumerate(features[:-1]):
    # Calculate the current row and column
    ax = axes[i]
    # ax=axes[i]
    # ax.hist(df[column], bins=25, alpha=0.5, label='Infected', color='green')
    sns.histplot(df[column], color="b",label='Infected',ax=axes[i])
    ax.set_title("Feature histogram based on infection")
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('amount')
    ax.set_title("Historgram")
plt.show()


################################
#Plot base on class number
Infected = df[df['infection'] == "Infected"]
Not_Infected = df[df['infection'] == "Not Infected"]
special_features = [features[1], features[2], features[4], features[6]]
print(special_features)

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
for i, special in enumerate(special_features):
    ax = axes[i]
    # axes[i].hist(Infected[special], bins=25, alpha=0.5, label='Infected', color='green')
    sns.histplot(Infected[special], color="red", label='Infected', ax=axes[i])
    # axes[i].hist(Not_Infected[special], bins=25, alpha=0.5, label='Not Infected', color='black')
    sns.histplot(Not_Infected[special], color="green", label='Not Infected', ax=axes[i])
    ax.set_title("Feature histogram based on infection")
    axes[i].set_xlabel(special)
    axes[i].set_ylabel('amount')
    axes[i].legend()
plt.show()


################################
#Plot Probability Density Function (PDF)
mean = df.iloc[:, 5].mean()
var = df.iloc[:, 5].var()
print(f"mean of sixth feature is {mean} and variance is {var}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
pdf = df.iloc[:, 5]
df=df['Body mass index (weight in kg/(height in m)^2)']

sns.set(style="whitegrid")  # Optional, for styling
sns.kdeplot(pdf, color="b", ax=axes[0])
axes[0].set_xlabel(features[5])
axes[0].set_ylabel("amount")
axes[0].set_title("Probability Density Function (PDF)")

sns.histplot(pdf, color="r", ax=axes[1])
axes[1].set_xlabel(features[5])
axes[1].set_ylabel("amount")
axes[1].set_title("Histogram")

plt.tight_layout()
plt.show()
