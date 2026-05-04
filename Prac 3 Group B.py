# Design and develop a distributed application to find the coolest/hottest year from the available weather data. Use weather data from the Internet and process it using Map Reduce.

data = [
    ("2001", 32), ("2001", 35),
    ("2002", 28), ("2002", 40),
    ("2003", 25), ("2003", 30)
]

# Map Phase
mapped = {}
for year, temp in data:
    mapped.setdefault(year, []).append(temp)

# Reduce Phase
avg_temp = {year: sum(vals)/len(vals) for year, vals in mapped.items()}

# Find hottest & coolest
hottest = max(avg_temp, key=avg_temp.get)
coolest = min(avg_temp, key=avg_temp.get)

print("Average Temps:", avg_temp)
print("Hottest Year:", hottest)
print("Coolest Year:", coolest)
