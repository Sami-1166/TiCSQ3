import numpy
import pandas as pd

df = pd.read_csv("NaiveDataset.csv")

outlook = df['Outlook'].to_list()
temp = df['Temp.'].to_list()
humidity = df['Humidity'].to_list()
wind = df['Wind'].to_list()
play_tenis = df['Play Tennis'].to_list()

user_outlook = input("Enter Outlook: ")
user_temp = input("Enter Temperature: ")
user_humidity = input("Enter Humidity: ")
user_wind = input("Enter Wind: ")

target_yes = 0
target_no = 0
for i in range(len(play_tenis)):
    if play_tenis[i] == "Yes":
        target_yes += 1
    else:
        target_no += 1

target_yes_prob = target_yes / len(play_tenis)
target_no_prob = target_no / len(play_tenis)
print("----------------------------------")
print("Yes Probability in Target: ", target_yes_prob)
print("No Probability in Target: ", target_no_prob)
print("----------------------------------")

yes_probabilities = []
no_probabilities = []

count_yes = 0
count_no = 0

for i in range(4):
    list_of_features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    for j in range(14):
        if i == 0:
            if outlook[j] == user_outlook and play_tenis[j] == 'Yes':
                count_yes += 1
            elif outlook[j] == user_outlook and play_tenis[j] == 'No':
                count_no += 1
        elif i == 1:
            if temp[j] == user_temp and play_tenis[j] == 'Yes':
                count_yes += 1
            elif temp[j] == user_temp and play_tenis[j] == 'No':
                count_no += 1
        elif i == 2:
            if humidity[j] == user_humidity and play_tenis[j] == 'Yes':
                count_yes += 1
            elif humidity[j] == user_humidity and play_tenis[j] == 'No':
                count_no += 1
        elif i == 3:
            if wind[j] == user_wind and play_tenis[j] == 'Yes':
                count_yes += 1
            elif wind[j] == user_wind and play_tenis[j] == 'No':
                count_no += 1

    yes_probabilities.append(count_yes /(target_yes))
    no_probabilities.append(count_no / (target_no))

    print(f"{list_of_features[i]}: Yes Probability: {count_yes / target_yes}")
    print(f"{list_of_features[i]}: No Probability: {count_no / target_no}")
    print("----------------------")

    count_yes = 0
    count_no = 0

mul_yes = target_yes_prob * numpy.prod(yes_probabilities)
mul_no = target_no_prob * numpy.prod(no_probabilities)

yes = mul_yes / (mul_yes + mul_no)
no = mul_no / (mul_no + mul_yes)

print("-------------------------------------")
print("-------------------------------------")
print("Resultant Yes Probability", yes)
print("Resultant No Probability", no)

print("-------------------------------------")
print("-------------------------------------")

if yes > no:
    print("Play Tennis: Yes")
else:
    print("Play Tennis: No")
