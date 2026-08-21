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


# Reflection about X-axis
R = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])


# Apply reflection
transformed = R @ homogeneous_points


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


# Reflected
plt.plot(
    new_x,
    new_y,
    'ro-',
    label='Reflection about X-axis'
)


# X-axis
plt.axhline(
    0,
    color='black',
    linewidth=1
)


plt.title("2D Reflection using Homogeneous Coordinates")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.axis("equal")

plt.legend()

plt.show()
