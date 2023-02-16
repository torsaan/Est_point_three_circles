import numpy as np
import matplotlib.pyplot as plt

p1 = np.array([263.774, 1379.875, 1843.735])    
p2 = np.array([741.441, 624.002, 1443.786])    
p3 = np.array([873.319, 8.275, 1660.090]) 

dist12 = np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
dist13 = np.sqrt((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2)
dist23 = np.sqrt((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2)

intersection_points = []

if dist12 < p1[2] + p2[2]:
    x1, y1, r1 = p1[0], p1[1], p1[2]
    x2, y2, r2 = p2[0], p2[1], p2[2]
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = np.sqrt(r1**2 - a**2)
    x3 = x1 + a*(x2-x1)/d
    y3 = y1 + a*(y2-y1)/d
    intersection_point1_12 = np.array([x3 + h*(y2-y1)/d, y3 - h*(x2-x1)/d])
    intersection_point2_12 = np.array([x3 - h*(y2-y1)/d, y3 + h*(x2-x1)/d])
    intersection_points.extend([intersection_point1_12, intersection_point2_12])
    print(intersection_point2_12)

if dist13 < p1[2] + p3[2]:
    x1, y1, r1 = p1[0], p1[1], p1[2]
    x2, y2, r2 = p3[0], p3[1], p3[2]
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = np.sqrt(r1**2 - a**2) 
    x3 = x1 + a*(x2-x1)/d
    y3 = y1 + a*(y2-y1)/d
    intersection_point1_13 = np.array([x3 + h*(y2-y1)/d, y3 - h*(x2-x1)/d])
    intersection_point2_13 = np.array([x3 - h*(y2-y1)/d, y3 + h*(x2-x1)/d])
    intersection_points.extend([intersection_point1_13, intersection_point2_13])
    print(intersection_point2_13)
    
    if dist23 < p2[2] + p3[2]:
        x1, y1, r1 = p2[0], p2[1], p2[2]
        x2, y2, r2 = p3[0], p3[1], p3[2]
        d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        a = (r1**2 - r2**2 + d**2) / (2*d)
        h = np.sqrt(r1**2 - a**2)
        x3 = x1 + a*(x2-x1)/d
        y3 = y1 + a*(y2-y1)/d
        intersection_point1_23 = np.array([x3 + h*(y2-y1)/d, y3 - h*(x2-x1)/d])
        intersection_point2_23 = np.array([x3 - h*(y2-y1)/d, y3 + h*(x2-x1)/d])
        intersection_points.extend([intersection_point1_23, intersection_point2_23])
        print(intersection_point2_23)


    Asspoint = (intersection_point2_12 + intersection_point2_13 + intersection_point2_23)/3
    print(Asspoint)

Afig, ax = plt.subplots()
circle1 = plt.Circle((p1[0], p1[1]), p1[2], color='r', fill=False)
circle2 = plt.Circle((p2[0], p2[1]), p2[2], color='b', fill=False)
circle3 = plt.Circle((p3[0], p3[1]), p3[2], color='g', fill=False)

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
for point in intersection_points:
    ax.plot(point[0], point[1], 'ko')
    ax.text(point[0], point[1], f'({point[0]:.1f}, {point[1]:.1f})', fontsize=8, ha='left', va='center')



ax.set_xlim([-2000, 3500])
ax.set_ylim([-2000, 3500])
ax.set_title('Circles and Intersection Points')

plt.show()



