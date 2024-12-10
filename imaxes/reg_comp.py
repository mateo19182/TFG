import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for deep learning publications
deep_learning_data = [
    ("2024", 724),
    ("2023", 742),
    ("2022", 631),
    ("2021", 571),
    ("2020", 384),
    ("2019", 264),
    ("2018", 141),
    ("2017", 73),
    ("2016", 29),
    ("2015", 13),
    ("2014", 7),
    ("2013", 4),
    ("2012", 2),
    ("2010", 1),
    ("2009", 1),
    ("2000", 1),
]

# Data for classic publications
classic_data = [
    ("2024", 1553),
    ("2023", 1784),
    ("2022", 2026),
    ("2021", 2203),
    ("2020", 2177),
    ("2019", 2345),
    ("2018", 2326),
    ("2017", 2573),
    ("2016", 2562),
    ("2015", 2615),
    ("2014", 2588),
    ("2013", 2909),
    ("2012", 2780),
    ("2011", 2545),
    ("2010", 2454),
    ("2009", 2680),
    ("2008", 2495),
    ("2007", 2238),
    ("2006", 1952),
    ("2005", 1609),
    ("2004", 1297),
    ("2003", 1055),
    ("2002", 788),
    ("2001", 719),
    ("2000", 641),
    ("1999", 575),
    ("1998", 501),
    ("1997", 479),
    ("1996", 392),
    ("1995", 311),
    ("1994", 278),
    ("1993", 213),
    ("1992", 188),
    ("1991", 161),
    ("1990", 115),
]

# Convert to DataFrames
df_deep = pd.DataFrame(deep_learning_data, columns=["Year", "Publications"])
df_classic = pd.DataFrame(classic_data, columns=["Year", "Publications"])

# Ensure numeric sorting of years
df_deep["Year"] = df_deep["Year"].astype(int)
df_classic["Year"] = df_classic["Year"].astype(int)

df_deep = df_deep.sort_values("Year")
df_classic = df_classic.sort_values("Year")

# Set a "beautiful" style
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(16, 9))

# Plot classic and deep learning lines
sns.lineplot(data=df_classic, x="Year", y="Publications", label="Rexistro de imaxe clásico", color="#1f77b4", linewidth=5)
sns.lineplot(data=df_deep, x="Year", y="Publications", label="Rexistro de imaxe baseado en aprendizaxe profundo", color="#ff7f0e", linewidth=5)

# Add annotations and labels
plt.title("Comparación no número de publicacións entre rexistro de imaxe clásico e baseado en aprendizaxe profundo", fontsize=20, pad=20)
plt.xlabel("Ano", fontsize=16)
plt.ylabel("Número de publicacións", fontsize=16)

# Emphasize certain parts
plt.xlim(df_classic["Year"].min(), df_deep["Year"].max()+1)
plt.ylim(0, max(df_classic["Publications"].max(), df_deep["Publications"].max())+100)

# Rotate x-ticks if necessary
plt.xticks(rotation=45, ha="right")

# Remove spines for a cleaner look
sns.despine()

plt.tight_layout()
plt.show()
plt.savefig()