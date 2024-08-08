# import matplotlib.pyplot as plt
#
# fig,ax = plt.subplots()
#
# rect = plt.Rectangle((1,1), 3, 1, fill=True, edgecolor='r')
# rect2 = plt.Rectangle((3,3), 1, 1, fill=True, edgecolor='b')
# rect3 = plt.Rectangle((1,3), 1, 1, fill=True, edgecolor='g')
# ax.add_patch(rect)
# ax.add_patch(rect2)
# ax.add_patch(rect3)
#
# ax.set_xlim([0,5])
# ax.set_ylim([0,5])
#
# plt.title("rysunek techniczny")
# plt.xlabel("X")
# plt.ylabel("Y")
#
# plt.grid()
# plt.show()

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
rect = plt.Rectangle((0.2,0.2),0.6,0.2, linewidth=2, edgecolor='blue', facecolor='none')
rect1 = plt.Rectangle((0.6, 0.6),0.2,0.2, linewidth=2, edgecolor='red', facecolor='yellow')
rect2 = plt.Rectangle((0.2, 0.6),0.2,0.2, linewidth=2, edgecolor='red', facecolor='yellow')
circle = plt.Circle((0.5, 0.5),0.1,edgecolor='blue', facecolor='pink')
ax.add_patch(circle)
ax.add_patch(rect)
ax.add_patch(rect1)
ax.add_patch(rect2)
plt.plot([0.2, 0.8], [0.2, 0.4], color='red', linestyle='solid', linewidth=2)
plt.plot([0.2, 0.8], [0.4, 0.2], color='green', linestyle='solid', linewidth=2)
plt.plot([0.2, 0.2], [0,1],color='red', linestyle='solid', linewidth=2)
plt.plot([0.8, 0.8], [0,1],color='red', linestyle='solid', linewidth=2)

plt.xlim([0,1])
plt.ylim([0,1])

plt.grid(True)
plt.show()
