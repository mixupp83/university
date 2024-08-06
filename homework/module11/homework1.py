import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Пример с requests
response = requests.get('https://api.github.com')

print(f"Status Code: {response.status_code}")

print(f"Response Content: {response.json()}")


# Пример с pandas
data = pd.read_csv('data.csv')

print("Типы данных столбцов:", data.dtypes)

if 'phoneNumber' in data.columns:
    data['phoneNumber'] = pd.to_numeric(data['phoneNumber'], errors='coerce')
    data = data.dropna(subset=['phoneNumber'])
    average_phone_number = data['phoneNumber'].mean()
    print(f"Average Phone Number: {average_phone_number}")
else:
    print("Столбец 'phoneNumber' не найден в данных.")



# Пример с matplotlib и numpy
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')

plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()