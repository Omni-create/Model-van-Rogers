import numpy as np
import matplotlib.pyplot as plt

# Data
bachelor_data = 75 + 71  # Bachelor studenten (eerste- en tweedejaars)
ad_data = 37 + 53  # AD studenten (eerste- en tweedejaars)
ad_deeltijd_data = 40  # AD deeltijd studenten (eerste- en tweedejaars samen)

# Innovatie model van Rogers - percentages
categories = ["Innovators", "Early Adopters", "Early Majority", "Late Majority", "Laggards"]
percentages = [2.5, 13.5, 34, 34, 16]

# Functie om studenten per categorie te berekenen
def calc_students(total_students, percentages):
    return [round(total_students * (p / 100)) for p in percentages]

# Bereken studenten per categorie voor elke groep
bachelor_students = calc_students(bachelor_data, percentages)
ad_students = calc_students(ad_data, percentages)
ad_deeltijd_students = calc_students(ad_deeltijd_data, percentages)
combined_students = calc_students(bachelor_data + ad_data + ad_deeltijd_data, percentages)


def plot_distribution(data, title, color):
    bars = plt.bar(categories, data, color=color)
    plt.title(title)
    plt.ylabel("Aantal Studenten")
    plt.grid(True)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

plt.figure(figsize=(14, 10))
# Bachelor studenten
plt.subplot(2, 2, 1)
plot_distribution(bachelor_students, "Bachelor Studenten", "blue")
# AD studenten
plt.subplot(2, 2, 2)
plot_distribution(ad_students, "AD Studenten", "green")
# AD deeltijd studenten
plt.subplot(2, 2, 3)
plot_distribution(ad_deeltijd_students, "AD Deeltijd Studenten", "red")

# Gecombineerde data van alle groepen
plt.subplot(2, 2, 4)
plot_distribution(combined_students, "Alle Studenten Gecombineerd", "purple")
plt.tight_layout()
plt.show()
