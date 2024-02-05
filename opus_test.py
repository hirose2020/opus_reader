
from brukeropusreader import read_file

FILENAME = "irdata/MC01-01.0"

opus_data = read_file(FILENAME)

print(f"Data fields: " f"{list(opus_data.keys())}")

ab_x = opus_data.get_range("AB")
# the "AB" data can contain more null values at the end (at least 1)
# so the getting useful data requires slicing the array:
abs = opus_data["AB"][0:len(ab_x)]
print(f"Absorption spectrum range: " f"{ab_x[0]} {ab_x[-1]}")
print(f"Absorption elements num: " f'{len(abs)}')

import matplotlib.pyplot as plt

print("Plotting AB")
plt.plot(opus_data.get_range("AB"), abs)
plt.show()

print("Plotting interpolated AB")
plt.plot(*opus_data.interpolate(ab_x[0], ab_x[-1], 100))
plt.show()
