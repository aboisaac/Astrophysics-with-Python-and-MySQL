import mysql.connector
import numpy as np 
import matplotlib.pyplot as plt




connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "enjoycode01",
    database  ="Solarsystem"
)

cursor = connect.cursor()
planet_table = "SELECT*FROM planet"
planet_earthmasses = "SELECT EARTHMASSES FROM planet"
cursor.execute(planet_table)
data = cursor.fetchall()


earthmass = 5.971e24 #kg
au = 150e9 #m
G = 6.6743e-11 # m3 kg-1 s-2
solar_mass= 1.9e30

solar_planet_velocity = []
solar_planet_distance =[]
planet_masses = []



for rad in data:
    solar_planet_velocity.append(int(rad[3]))
    solar_planet_distance.append(int(rad[2])*au)
    planet_masses.append(int(rad[1])*earthmass)


angle_degrees= np.linspace(0,2*np.pi,100)

i = solar_planet_distance[-1:]


x_pos = i*np.cos(angle_degrees)
y_pos = i*np.sin(angle_degrees)

fig, axes = plt.subplots(3, figsize=(6,6))

axes[0].plot(x_pos,y_pos, color ="black")
axes[0].set_title("Orbit for Planet 9")
axes[0].set_ylabel("y-pos [AU]")
axes[0].set_xlabel("x-pos [AU]")
axes[0].grid()


axes[1].plot(angle_degrees,x_pos, color= "red")
axes[1].set_title("x-orbit for Planet 9")
axes[1].set_ylabel("x-pos [AU]")
axes[1].set_xlabel("angle")
axes[1].grid()


axes[2].plot(angle_degrees,y_pos,color = "blue")
axes[2].set_title("y-orbit for Planet 9")
axes[2].set_ylabel("y-pos [AU]")
axes[2].set_xlabel("angle")
axes[2].grid()


plt.tight_layout()
plt.show()






