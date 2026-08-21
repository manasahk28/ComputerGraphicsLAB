import matplotlib.pyplot as plt
import numpy as np


# Original triangle
points = np.array([
    [2, 2],
    [6, 2],
    [4, 6],
    [2, 2]
])


# Convert to homogeneous coordinates
homogeneous_points = np.vstack(
    (points.T, np.ones(points.shape[0]))
)


# Translation values
Tx = 5
Ty = 3


# Translation matrix
T = np.array([
    [1, 0, Tx],
    [0, 1, Ty],
    [0, 0, 1]
])


# Apply transformation
transformed = T @ homogeneous_points


# Extract X and Y
new_x = transformed[0, :]
new_y = transformed[1, :]


# Create figure
plt.figure(figsize=(8, 6))

# Original triangle
plt.plot(
    points[:, 0],
    points[:, 1],
    'bo-',
    label='Original'
)

# Translated triangle
plt.plot(
    new_x,
    new_y,
    'ro-',
    label='Translated'
)


plt.title("2D Translation using Homogeneous Coordinates")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.axis("equal")

plt.legend()

plt.show()