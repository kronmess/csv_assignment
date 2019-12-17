import csv
from statistics import mean
from statistics import median
import numpy as np
import matplotlib.pyplot as plt
#1
with open('activity.csv','r')as f:
    data = csv.reader(f)
    mydict = {}
    for row in data:
        if row[0] != '0' and row[1] != 'date' and row[0] != 'NA':
            if row[1] not in mydict:
                mydict[row[1]] = [int(row[0])]
            else:
                mydict[row[1]].append(int(row[0]))
total_per_day = {}
mean_tot_perday = {}
median_per_day = {}
for key, value in mydict.items():
    total_per_day[key] = sum(value)
    mean_tot_perday[key] = round(mean(value),2)
    median_per_day[key] = median(value)
print(total_per_day)
print(mean_tot_perday)
print(median_per_day)

N = len(mydict)
meantotalperday = tuple(mean_tot_perday.values())
ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, meantotalperday, width)

plt.ylabel('Steps')
plt.title('Mean Total Step per Day')
plt.xticks(ind, tuple(mean_tot_perday.keys()))
plt.yticks(np.arange(0, 300, 20))

plt.show()

#2
with open('activity.csv','r') as file:
    datas = file.readlines()
    datas.pop(0)
    maximum_average = {'steps':0,'date1':'','date2':''}
    minute_data = {d:0 for d in [y.split(',')[2].split("\n")[0] for y in datas]}
    current_data = {}
    total_day = len([y for y in [z for z in datas]]) / len(minute_data.items())
    for data in datas:
        if not data.split(',')[0]=='NA':
            minute_data[data.split(',')[2].split('\n')[0]] += int(data.split(',')[0])
            if current_data.get('steps') == None:
                current_data['steps'] = data.split(',')[0]
                current_data['date'] = data.split(',')[1] +':'+ data.split(',')[2].split('\n')[0]
            else:
                if not current_data['steps'] =='NA':
                    step_difference = (int(data.split(',')[0]) - int(current_data['steps']))
                    if step_difference > maximum_average['steps']:
                        maximum_average['steps'] = step_difference
                        maximum_average['date1'] = current_data['date']
                        maximum_average['date2'] = data.split(',')[2].split('\n')[0]
                current_data['steps'] = data.split(',')[0]
                current_data['date'] = data.split(',')[1]+':'+ data.split(',')[2].split('\n')[0]
        else:
            current_data['steps'] = 'NA'
            current_data['date'] = data.split(',')[1] + ':' + data.split(',')[2].split('\n')[0]
    minute_data = {d:(y/total_day) for d,y in minute_data.items()}
    print(maximum_average)
    #print(minute_data)
    input('Please enter to show graph')
    plt.plot([y for y in minute_data.keys()],[z for z in minute_data.values()])
    plt.xlabel('Time Interval')
    plt.ylabel('Average number of steps')
    plt.show()

#3
with open('activity.csv','r')as f:
    data = csv.reader(f)
    na_counter = {'NA':0}
    new_dataset = {}
    for row in data:
        if row[1] != 'date':
            if row[0] == 'NA':
                na_counter['NA'] += 1
                if row[1] not in new_dataset:
                    new_dataset[row[1]] = [0]
                else:
                    new_dataset[row[1]].append(0)
            if row[0]!= 'NA':
                if row[1] not in new_dataset:
                    new_dataset[row[1]] = [int(row[0])]
                else:
                    new_dataset[row[1]].append(int(row[0]))
total_per_day2 = {}
mean_tot_perday2 = {}
median_per_day2 = {}
for key, value in new_dataset.items():
    total_per_day2[key] = sum(value)
    mean_tot_perday2[key] = round(mean(value),2)
    median_per_day2[key] = median(value)
#4

with open('activity.csv','r') as f:
    data = csv.reader(f)
    counter = 0
    steps = {}
    weekday={}
    weekend={}
    for row in data:
        if row[1] != 'date':
            if row[0] == 'NA':
                if row[1] not in steps:
                    steps[row[1]] = [0]
                    counter +=1
                    if counter == 8:
                        counter = 1
                    if counter <=5 and counter > 0:
                            weekday[row[1]] = [0]
                    elif counter > 5 and counter < 8:
                            weekend[row[1]] = [0]
                else:
                    steps[row[1]].append(0)
                    if row[1] in weekday:
                            weekday[row[1]].append(0)
                    elif row[1] in weekend:
                        weekend[row[1]].append(0)

            elif row[0] != 'NA':
                    if row[1] not in steps:
                        steps[row[1]] = [int(row[0])]
                        counter +=1
                        if counter == 8:
                            counter = 1
                        if counter <=5 and counter > 0:
                            weekday[row[1]] = [int(row[0])]
                        elif counter > 5 and counter < 8:
                            weekend[row[1]] = [int(row[0])] 
                    else:
                        steps[row[1]].append(int(row[0]))
                        if row[1] in weekday:
                            weekday[row[1]].append(int(row[0]))
                        elif row[1] in weekend:
                            weekend[row[1]].append(int(row[0]))
    print('weekday: ',weekday)
    print('\nweekend: ',weekend)
    p5 = plt.bar(minute_data.keys(),minute_data.values())
    plt.show()
    # i was unable to make the final graph for the weekdays and the weekends 