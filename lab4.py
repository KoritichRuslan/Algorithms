import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.ndimage import label
import matplotlib.patches as patches

# не забудьте додати текстовий файл в директорію
with open('DS9.txt', 'r') as file:
    data = np.array([list(map(int, line.split())) for line in file])

x_coords, y_coords = data[:, 0], data[:, 1]

grid = np.zeros((y_coords.max() + 1, x_coords.max() + 1))
grid[y_coords, x_coords] = 1
labeled_grid, features_number = label(grid)

centroids = [
    np.argwhere(labeled_grid == label_num).mean(axis=0)[::-1]
    for label_num in range(1, features_number + 1)
]
centroids = np.array(centroids)

vor = Voronoi(centroids)

fig, ax = plt.subplots(figsize=(12, 6), dpi=80)
ax.set_xlim(0, 960)
ax.set_ylim(0, 540)
ax.scatter(x_coords, y_coords, c="black", alpha=0.1, s=1)

for centroid in centroids:
    ax.add_patch(patches.Circle((centroid[0], centroid[1]), radius=2.5, color='red', zorder=10))

voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=0.5)

plt.axis('off')
plt.savefig("result2.png")
plt.show()