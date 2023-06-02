import pandas
import Utils
import datetime
import matplotlib.pyplot as plt


# Call File Data Frames
df1 = pandas.read_csv("~/df.csv", lineterminator='\n')
df2 = pandas.read_csv("~/df2.csv", lineterminator='\n')

list2 = []
for time in df1.Time:
    list2.append(Utils.time_formatter(time))

df1.Time = list2
df = df1.append(df2, ignore_index=True)

# Make Time Column Time Object
time_list = []
for time in df1.Time:
    time_list.append(Utils.turn_to_time(time, 31))
df1.Time = time_list

cc = datetime.date(2012, 1, 1)
xf = df1.loc[df1['Time'] > cc]
xf = xf.groupby('Time')['Labels'].mean()
plt.figure(figsize=(20, 10))
plt.plot(xf)
plt.show()
