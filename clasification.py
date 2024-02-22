

# Instalamos el paquetes corrplot que contiene funciones para visualizar la matriz de correlación.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('homeLoanAproval.csv')

# Visualizamos las primeras 5 filas del dataset
plt.scatter(data['ApplicantIncome'], data['LoanAmount'], marker='o')
plt.title('ApplicantIncome vs LoanAmount')
plt.xlabel('ApplicantIncome')
plt.ylabel('LoanAmount')

plt.show()