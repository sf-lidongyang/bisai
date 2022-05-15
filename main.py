from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1)
scene.set_floor(-22, (255/255,228/255,225/255))
scene.set_directional_light((-1,0.5, -1), 0.2, (255/255,228/255,225/255))
scene.set_background_color((127/255,255/255,212/255))

@ti.func
def love(pos, r, color):
    j = -20
    for i,k in ti.ndrange((-64,64),(-64,64)):
        if (i-pos[0])**2 - abs(i)*k + k**2 < r*r:
            scene.set_voxel(vec3(i,j,k), 1, color)

@ti.func
def sphere(pos, r, color):
    for i,k,j in ti.ndrange((-58,58),(-58,58),(-58,58)):
        if (i-pos[0])**2 + (k-pos[1])**2 + (j-pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,k,j), 2, color)

@ti.func
def selfsphere(pos, r, color):
    for i,k,j in ti.ndrange((-58,58),(-58,0),(-10,10)):
        if (i-pos[0])**2 + (k-pos[1])**2 + (j-pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,k,j), 2, color)

@ti.func
def ellipse(pos, a, b, color):
    j = 19
    for i, k in ti.ndrange((-64, 64), (-64, 64)):
        if (i - pos[0])**2*b**2+(k - pos[1])**2*a**2 < a**2*b**2:
            scene.set_voxel(vec3(i, k, j), 2, color)

@ti.func
def ellipsoid(pos, a, b, c, color):
    for i, k, j in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        if (i-pos[0])**2*b**2*c**2+(k-pos[1])**2*a**2*c**2+(j-pos[2])**2*a**2*b**2<a**2*b**2*c**2:
            scene.set_voxel(vec3(i, k, j), 2, color)

@ti.kernel
def initialize_voxels():
    color_red = vec3(220 / 255, 20 / 255, 60 / 255);color_red2 = vec3(178/255,34/255,34/255)
    color_pink = vec3(255 / 255, 105 / 255, 180 / 255);color_eyered = vec3(220 / 255, 20 / 255, 60 / 255)
    color_black = vec3(0, 0, 0);color_white = vec3(255,255,255)
    color_blue = vec3(0/255,191/255,255/255)

    pos1 = vec3(0, 10, 0)
    sphere(pos1, 20, color_pink)
    # blush
    pos2 = vec3(-10, 9, 19)
    pos3 = vec3(10, 9, 19)
    ellipse(pos2, 4, 3, color_eyered)
    ellipse(pos3, 4, 3, color_eyered)
    # eye
    pos5 = vec3(4, 15, 10)
    pos6 = vec3(-4, 15, 10)
    ellipse(pos5, 3, 6, color_black)
    ellipse(pos6, 3, 6, color_black)
    # pupil
    pos5 = vec3(4, 17, 10)
    pos6 = vec3(-4, 17, 10)
    ellipse(pos5, 2, 3, color_white)
    ellipse(pos6, 2, 3, color_white)
    pos5 = vec3(4, 12, 10)
    pos6 = vec3(-4, 12, 10)
    ellipse(pos5, 2, 1, color_blue)
    ellipse(pos6, 2, 1, color_blue)
    # hands
    pos12 = vec3(20,3,10); pos13 = vec3(-21,20,10)
    sphere(pos12, 6, color_pink)
    sphere(pos13, 6, color_pink)
    # foot
    pos14 = vec3(12, -12, 0)
    ellipsoid(pos14, 7, 7,10, color_red2)
    pos15 = vec3(-12, -12, 0)
    ellipsoid(pos15, 7, 7,10, color_red2)
    # ground
    pos16 = vec3(0, -20, 0)
    love(pos16, 30, color_red)
    # mouth
    pos17 = vec3(0, 6, 20)
    ellipse(pos17, 1, 1, color_black)
    pos17 = vec3(1, 6, 20)
    ellipse(pos17, 1, 1, color_black)
    pos17 = vec3(-1, 6, 20)
    ellipse(pos17, 1, 1, color_black)
    pos17 = vec3(2, 7, 20)
    ellipse(pos17, 1, 1, color_black)
    pos17 = vec3(-2, 7, 20)
    ellipse(pos17, 1, 1, color_black)

initialize_voxels()
scene.finish()
