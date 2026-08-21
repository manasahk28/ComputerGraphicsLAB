import matplotlib.pyplot as plt
import numpy as np


# Original triangle
points = np.array([
    [2, 2],
    [6, 2],
    [4, 6],
    [2, 2]
])


# Homogeneous coordinates
homogeneous_points = np.vstack(
    (points.T, np.ones(points.shape[0]))
)


# Scaling factors
Sx = 1.5
Sy = 1.5


# Scaling matrix
S = np.array([
    [Sx, 0, 0],
    [0, Sy, 0],
    [0, 0, 1]
])


# Apply scaling
transformed = S @ homogeneous_points


# Extract coordinates
new_x = transformed[0, :]
new_y = transformed[1, :]


# Plot
plt.figure(figsize=(8, 6))


# Original
plt.plot(
    points[:, 0],
    points[:, 1],
    'bo-',
    label='Original'
)


# Scaled
plt.plot(
    new_x,
    new_y,
    'ro-',
    label='Scaled'
)


plt.title("2D Scaling using Homogeneous Coordinates")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.axis("equal")

plt.legend()

plt.show()
