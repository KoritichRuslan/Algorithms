import matplotlib.pyplot as plt

x_coords = []
y_coords = []

# не забудьте додати текстовий файл в директорію
with open("DS9.txt", "r") as file:
    for line in file:
        x, y = map(int, line.split())
        x_coords.append(x)
        y_coords.append(y)

plt.figure(figsize = (9.6, 5.4)) # розмір полотна в дюймах - 100 пікселів на дюйм

plt.scatter(x_coords, y_coords, c = 'blue')

plt.title("Візуалізація точок")
plt.xlabel("X")
plt.ylabel("Y")

output_img = "result.png"
plt.savefig(output_img)
plt.show()

print(f"Графік збережено у файл {output_img}")