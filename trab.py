from Trajetoria import Trajetoria

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

trajetoria_obj = Trajetoria('batata')

# trajetoria_obj.referencial.origen.x = 0.00
# trajetoria_obj.referencial.origen.y = 0.00
# trajetoria_obj.referencial.origen.z = 0.00

trajetoria_obj.readLog()
print(trajetoria_obj.pontos[0])
print(len(trajetoria_obj.pontos))
#print(trajetoria_obj.pontos[-1])

xline, yline, zline = trajetoria_obj.coord()
#print(zline)

"""-------------------- PLOT ------------------"""

fig = plt.figure()

# Create a 3D axis
#plt.subplots_adjust(0.125, 0.11, 0.65, 0.85, 0.2, 0.2)
ax = fig.add_subplot(111,projection='3d')
ax.plot(xline, yline, zline, color='r')

ax.set_xlim([0, -5])  # Set your desired x-axis limits
ax.set_ylim([-3, 3])  # Set your desired y-axis limits
ax.set_zlim([-3, 3]) 

# ax_updated = fig.add_subplot(122, projection='3d')  # Updated plot
# ax_updated.set_xlim([0, -5])  # Set your desired x-axis limits
# ax_updated.set_ylim([-3, 3])  # Set your desired y-axis limits
# ax_updated.set_zlim([-3, 3]) 

ax_qx = fig.add_axes([0.75, 0.75, 0.20, 0.03])
ax_qy = fig.add_axes([0.75, 0.70, 0.20, 0.03])
ax_qz = fig.add_axes([0.75, 0.65, 0.20, 0.03])
ax_qw = fig.add_axes([0.75, 0.80, 0.20, 0.03])
ax_tx = fig.add_axes([0.75, 0.55, 0.20, 0.03])
ax_ty = fig.add_axes([0.75, 0.50, 0.20, 0.03])
ax_tz = fig.add_axes([0.75, 0.45, 0.20, 0.03])

ax_qw.set_title('Rotação')
ax_tx.set_title('Translação')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')  
ax.set_zlabel('Z Label')
ax.set_title('3D Trajectory Plot')

#####################################
#####################################
#         Código dos sliders      #
#####################################
#####################################
Quaternion_x = Slider(
    ax=ax_qx,
    label='Quaternion X ',
    valmin=-1,
    valmax=1,
    valinit=0,
)
Quaternion_y = Slider(
    ax=ax_qy,
    label='Quaternion Y ',
    valmin=-1,
    valmax=1,
    valinit=0,
)
Quaternion_z = Slider(
    ax=ax_qz,
    label='Quaternion z ',
    valmin=-1,
    valmax=1,
    valinit=0,
)
Quaternion_w = Slider(
    ax=ax_qw,
    label='Quaternion w ',
    valmin=-1,
    valmax=1,
    valinit=0,
)
tran_x = Slider(
    ax=ax_tx,
    label='Translação x ',
    valmin=-3,
    valmax= 3,
    valinit=0,
)
tran_y = Slider(
    ax=ax_ty,
    label='Translação y ',
    valmin=-3,
    valmax=3,
    valinit=0,
)
tran_z = Slider(
    ax=ax_tz,
    label='Translação z ',
    valmin=-3,
    valmax=3,
    valinit=0,
)

#####################################
#####################################

def update_x(val):
    flag = 1
    global xline
    global yline
    global zline
    trajetoria_obj.referencial.transformacao.translacao.x = val
    xline, yline, zline = trajetoria_obj.RotAndTrans(flag)
    flag = 0
    #ax.cla()
    ax.plot(xline, yline, zline, color='r')
    

def update_y(val):
    flag = 2
    global xline
    global yline
    global zline
    trajetoria_obj.referencial.transformacao.translacao.y = val
    xline, yline, zline = trajetoria_obj.RotAndTrans(flag)
    flag = 0
    #ax.cla()
    ax.plot(xline, yline, zline, color='r')

def update_z(val):
    flag = 3
    global xline
    global yline
    global zline
    trajetoria_obj.referencial.transformacao.translacao.z = val
    xline, yline, zline = trajetoria_obj.RotAndTrans(flag)
    flag = 0
    #ax.cla()
    ax.plot(xline, yline, zline, color='r')

tran_x.on_changed(update_x)
tran_y.on_changed(update_y)
tran_z.on_changed(update_z)

# ax.set_xlim3d([-10, 10])
# ax.set_ylim3d([-10, 10])
# ax.set_zlim3d([-10, 10])

plt.show()