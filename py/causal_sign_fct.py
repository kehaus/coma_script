# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



from base_axes import put_arrowhead_axes, light_beam


#==============================================================================
# color definition
#==============================================================================

khBlue  = '#5B7BE6'
khRed   = '#FF6666'

#==============================================================================
# Plot settings
#==============================================================================

# arrow style


# plot line style
line_style1 = {
    'linewidth':    1.8,
    'linestyle':    '-',
    'color':        'k'
}

line_style_blue = {
    'linewidth':    1.8,
    'linestyle':    '-',
    'color':        khBlue,
}

line_style_red = {
    'linewidth':    1.8,
    'linestyle':    '-',
    'color':        khRed,
}

# fontproperties - label
font_dict_label = {
    'family':               'serif',
    'size':                 25,
}

# fontproperties - textbox
font_dict_txt = {
    'family':               'serif',
    'size':                 20,
}



#==============================================================================
# mathematical functions
#==============================================================================

x = np.arange(-0.4, 1-0, 0.1)
y = np.concatenate((np.array([0, 0, 0, 0, 0,]), 
                    [0.1, 0.3, 0.2, -0.1, 0.1, 0.6, 0.7, 0.8, 0.6]))


X = np.linspace(0, x.max(), 501)
Y = 0.1*np.sin(20*np.pi*X)

X_ = np.zeros(len(X))
Y_ = np.zeros(len(Y))
phi = np.pi/4

rot = np.matrix([[np.cos(phi), -np.sin(phi)],
                 [np.sin(phi),  np.cos(phi)]])

#for idx in range(len(X)):
#    X_[idx], Y_[idx] = rot * np.matrix([X[idx], Y[idx]]).T

X_i, Y_i = light_beam(X, 0.02, 7, -np.pi/4)
X_r, Y_r = light_beam(X, 0.02, 7,  np.pi/4)
X_t, Y_t = light_beam(X, 0.02, 7, 7*np.pi/8)
#==============================================================================
# plot function
#==============================================================================
fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

ax1.plot([0, 1], [1, 1], **line_style_blue)
ax1.plot([-1, 0], [-1, -1], **line_style_blue)
ax1.set_xlim([-0.8,0.8])
ax1.set_ylim([-1.4,1.4])

# changes axes to arrow head
fig1, ax1 = put_arrowhead_axes(fig1, ax1)



# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)


# axis label
xlabel = ax1.annotate('t', (0.78, -0.2), xycoords='data',
                      **font_dict_label)
ylabel = ax1.annotate(r'$ sign(t)$', (-0.25, 1.3), xycoords='data',
                      **font_dict_label)

# textboxes
txt1 = ax1.annotate(r'$ 1 $', (-0.06, 0.95), xycoords='data', color='k',
                    **font_dict_txt)
txt2 = ax1.annotate(r'$ -1 $', (0.02, -1.05), xycoords='data', color='k',
                    **font_dict_txt)
#txt3 = ax1.annotate(r'$ T < T_C $', (0.87, 0.47), xycoords='figure fraction', color=khBlue,
#                    **font_dict_txt)



fig1.tight_layout()
fig1.savefig('../img/causal_sign_fct.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


