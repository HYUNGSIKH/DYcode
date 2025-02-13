##############################################################################
# DYENG - TIMESERIES PLOTTING PYTHON CODE (파고-주기-파향 시계열 그림 코드)
# 1. 시간포맷 확인 (기본 2023-05-20 23:00. 다를경우 데이터 수정 또는 코드 수정)   
# 2. plotting 할 그림의 시간대 설정 (ex. 2023.05.01 00:00 ~ 2023.05.12 23:00)
# 3. 수정이 필요할 경우, 각각의 주석을 참조해서 수정할 것
##############################################################################
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

#Total Font style
plt.rcParams['font.family'] = 'Times New Roman'

# load data file name Data Format
# data format  =  2023-05-01 0:00	0.417	5.05	167.6
file_path = 'input.dat'  
data_time = []  # time (ex. 2023-05-01 0:00)
data_H = []     # wave Height (ex. 0.417)
data_T = []     # wave period (ex. 5.05)
data_dir = []   # wave direction (ex. 167.6)

# Define the start and end date for the plot
# sample file = 2023.05.01 00:00 ~ 2023.05.12 23:00
# ex.   start_date = datetime.datetime(2023, 5,  9,  0, 0) => 2023.05.09 00:00
#       end_date =   datetime.datetime(2023, 5, 12, 23, 0) => 2023.05.12 23:00
start_date = datetime.datetime(2023, 5,  1,  0, 0)
end_date =   datetime.datetime(2023, 5, 12, 23, 0)

with open(file_path, 'r') as file:
    for line in file:
        columns = line.split('\t')
        if len(columns) >= 4:
            try:
                time=datetime.datetime.strptime(columns[0],
                                                '%Y-%m-%d %H:%M') # date format
                if start_date <= time <= end_date:
                    H_value = float(columns[1]);
                    T_value = float(columns[2]);
                    D_value = float(columns[3]);
                    data_time.append(time);
                    data_H.append(H_value);
                    data_T.append(T_value);
                    data_dir.append(D_value);
            except ValueError:
                print(f"Error parsing line: {line.strip()}")

# figure size x:y = 15:5 size
fig, ax1 = plt.subplots(figsize=(15, 5))

# First axis (Wave Height)
ax1.set_xlabel('Time', fontsize=14)
ax1.set_ylabel('Wave Height(m, $H_{1/3}$)', color='k', fontsize=14)
line1, = ax1.plot(data_time, data_H, color='blue', label='Wave Height')
ax1.tick_params(axis='y', labelcolor='k', labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_ylim(0, 8)      # ylim 0 ~ 8m
ax1.set_yticks([i for i in range(0, 9)])

# Second axis (Wave Period)
ax2 = ax1.twinx()
ax2.set_ylabel('Wave Period(sec, $T_{1/3}$)', color='k', fontsize=14)
line2, = ax2.plot(data_time, data_T, color='red', label='Wave Period')
ax2.tick_params(axis='y', labelcolor='k', labelsize=12)
ax2.set_ylim(0, 16)     # ylim 0 ~ 16sec
ax2.set_yticks([i * 2 for i in range(9)])

# Third axis (Wave Direction)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 50))
# ax3.set_ylabel('Wave Direction', color='k', fontsize=14)
line3 = ax3.scatter(data_time, data_dir, color='green', label='Wave Direction', s=12)  # 점의 크기를 12으로 설정
ax3.set_ylim(0, 360)
ax3.set_yticks([i * 45 for i in range(9)])
ax3.set_yticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N'], fontsize=12)
ax3.tick_params(axis='y', labelcolor='k')

plt.legend(handles=[line1, line2, line3], loc='upper right', fontsize=14)
ax1.grid(True)

# Change date format here
ax1.set_xlim(start_date, end_date)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('´%y-%m-%d %H:%M'))  
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

plt.tight_layout()
plt.savefig('output.png', dpi=300)
plt.show()