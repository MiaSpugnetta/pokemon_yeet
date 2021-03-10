from pokemon import game_logic
import pandas as pd
import matplotlib.pyplot as plt


# Check bias

outcome_dict = {
                "WE WON HAHAHAHAHAHAHAHAHAHAHAHA": 0,
                "IT'S A DRAW": 0,
                "WE LOST BECAUSE WE ARE LOSERS": 0
                }

# Call the function a number of times and record the outcome to outcome_dict
for i in range(100):
    outcome = game_logic()
    outcome_dict[outcome] += 1

#print(outcome_dict)

# Create a DataFrame from the outcome_dict
df = pd.DataFrame({'outcome': outcome_dict.keys(), 'value': outcome_dict.values()})

# Plot the DataFrame
df.plot(x="outcome", y="value", fontsize=5, rot=0, kind='bar')
plt.show()

print(df)
