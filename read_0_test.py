from brukeropusreader import read_file
import matplotlib.pyplot as plt

FIN = "irdata/MC01-01.0"
opus_data = read_file(FIN)

ab_x = opus_data.get_range("AB")
abs = opus_data["AB"][0:len(ab_x)]

plt.plot(opus_data.get_range("AB"), abs)
plt.show()

