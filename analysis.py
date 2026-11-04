import pandas as pd
import matplotlib.pyplot as plt

def analyze_sensor_data(csv_path='sample_aqi_data.csv'):
    df = pd.read_csv(csv_path)
    print(df.describe())
    df.plot(x='timestamp', y=['pm25', 'pm10'], kind='line')
    plt.title('PM2.5 and PM10 Trends')
    plt.savefig('aqi_trends.png')
    print("Plot saved as aqi_trends.png")

if __name__ == '__main__':
    analyze_sensor_data()
