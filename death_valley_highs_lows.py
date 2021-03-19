import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates, and high and low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			try:
				high = int(row[4])
				low = int(row[5])
				dates.append(current_date)
			except ValueError:
				print(f"Missing data for {current_date}")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)