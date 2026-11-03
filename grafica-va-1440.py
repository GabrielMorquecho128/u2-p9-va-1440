# Marco Gabriel Morquecho Acosta NC 1440
# 6 Pie chart
import matplotlib.pyplot as plt

# used to show part-to-whole relationships/data

# data
materias = ['Matematicas', 'Español', 'Ingles', 'MachineL', 'VisionA']
calificaciones = [90, 85, 95, 88, 100]

plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')
plt.title("Pie Chart Example NC 1440")
plt.xlabel("Materias")
plt.ylabel("Calificaciones")

plt.show()

print("Marco Gabriel Morquecho Acosta NC 1440")
