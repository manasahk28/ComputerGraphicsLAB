import matplotlib.pyplot as plt
import numpy as np
import math


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


# Rotation angle
angle = 45

theta = math.radians(angle)


# Rotation matrix
R = np.array([
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta),  math.cos(theta), 0],
    [0, 0, 1]
])


# Apply rotation
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


# Rotated
plt.plot(
    new_x,
    new_y,
    'ro-',
    label='Rotated 45°'
)


plt.title("2D Rotation using Homogeneous Coordinates")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.axis("equal")

plt.legend()

plt.show()