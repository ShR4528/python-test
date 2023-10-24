import pandas as pd

# Чтение данных из файла сетевого трафика
data = pd.read_csv('data.csv')

# Вывод первых 5 строк данных
print(data.head())

# Общее количество записей
total_records = len(data)
print("Общее количество записей:", total_records)

# Количество уникальных источников и назначений
unique_sources = data['Источник'].nunique()
unique_destinations = data['Назначение'].nunique()
print("Количество уникальных источников:", unique_sources)
print("Количество уникальных назначений:", unique_destinations)

# Суммарное количество пакетов
total_packets = data['Количество пакетов'].sum()
print("Суммарное количество пакетов:", total_packets)

# Статистика трафика по источникам
source_traffic_stats = data.groupby('Источник')['Количество пакетов'].sum().sort_values(ascending=False)
print("Статистика трафика по источникам:")
print(source_traffic_stats)
