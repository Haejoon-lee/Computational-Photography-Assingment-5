# %%
import numpy as np
from matplotlib import pyplot as plt
import skimage.color
import cv2
from mpl_toolkits.mplot3d import Axes3D
from src.cp_hw5 import *

# %%
from matplotlib.colors import LightSource

def display_depth_3d_w_light(Z, flip_z=False, num_fig=1):
    """
    Plot the depth map as a surface with lighting effects.

    Parameters
    ----------
    Z : numpy.ndarray
        The HxW array of surface depths.

    flip_z : bool, optional
        If True, flips the Z-axis.

    Returns
    -------
    None
    """

    H, W = Z.shape
    x, y = np.meshgrid(np.arange(W), np.arange(H))

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Add lighting effect
    ls = LightSource()
    if flip_z:
        Z = -Z
    color_shade = ls.shade(Z, plt.cm.gray)

    # Display the surface with lighting
    ax.plot_surface(x, y, Z, facecolors=color_shade, rstride=4, cstride=4)

    plt.show()
    # plt.show(block=False)


# %%
# Normal Integration
# surface_poisson = np.load('surface_poisson_uncal_diffG.npy')
# surface_poisson = np.load('surface_poisson_cal.npy')
surface_poisson = np.load('surface_poisson_mine1.npy')
# plt.imshow(surface_poisson, cmap='gray')
# plt.title('Depth map from Poisson integration')
# plt.show()
display_depth_3d_w_light(surface_poisson, num_fig=1)
# plt.show(block=False)
# plt.show()

# surface_frankot = np.load('surface_frankot_uncal.npy')
# surface_frankot = np.load('surface_frankot_cal.npy')
# surface_frankot = np.load('surface_frankot_mine1.npy')
# surface_frankot = np.load('surface_frankot_entropy.npy')
surface_frankot = np.load('surface_frankot_mine2.npy')


# plt.imshow(surface_frankot, cmap='gray')
# plt.title('Depth map using Frankot and Chellappa method')
# plt.show()
display_depth_3d_w_light(surface_frankot, num_fig=2)
# Show both plots
# plt.show()
