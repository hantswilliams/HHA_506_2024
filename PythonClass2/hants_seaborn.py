# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

sns.get_dataset_names()

# Load an example dataset
tips = sns.load_dataset("tips")

titantic = sns.load_dataset("titanic")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

titantic.to_csv('titanic.csv', index=False)

