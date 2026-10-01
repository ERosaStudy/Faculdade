import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = np.array([1,2,3,4,5])
# y = x * 2

# plt.xlabel('Valores de X')
# plt.ylabel("Valores de Y")
# plt.title('Gráfico de linhas')

# plt.plot(x,y,'ro--',linewidth=1, markersize=20)
# ##plt.show()


# ##DUAS RETAS NO MESMO GRÁFICO

# y2 = x*x
# plt.plot(x,y, 'g--o',x,y2,'r--h')

# ##plt.show()


dfpaises = pd.read_csv('paises.csv', delimiter=';')

paises = dfpaises.nlargest(6, 'Area (sq. mi.)')
print(len(dfpaises))
plt.scatter(paises['Country'],paises['Area (sq. mi.)'], color='red', marker='o', s=00)
plt.show()