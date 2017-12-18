# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import arrow_array, remove_axes, circle_outline, plot_box

#==============================================================================
# functions
#==============================================================================

def clmb(x1, y1, x2, y2):
    """ """
    coupling_constant = 0.05
    distance = np.abs((x1-x2)**2 + (y1-y2)**2)
    x2_new = x2 + np.sign(x1-x2)*coupling_constant /(distance + 1)
    y2_new = y2 + np.sign(y1-y2)*coupling_constant /(distance + 1)
    return  [x2_new, y2_new]


#==============================================================================
# color definition
#==============================================================================

khBlue  = '#5B7BE6'
khRed   = '#FF6666'

#==============================================================================
# Plot settings
#==============================================================================

# arrow style
arrow_style1 = { # default arrow style parameter
    'fc':               'k',
    'ec':               'k',
    'head_width':       1./30,
    'head_length':      1./20,
    'lw':               1.2,
    'overhang':         1.0
}
arrow_style2= arrow_style1.copy()
arrow_style2['head_width'] = 0
arrow_style2['head_length'] = 0


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
# plot function
#==============================================================================
#x = np.linspace(-2,2, 1001)

#plt.close('all')
fig1.clf()
fig1 = plt.figure(num=1, figsize=(16,4));
ax1 = fig1.add_subplot(111)

ax1.set_xlim([-1.5, 1.5])
ax1.set_ylim([-0.0,0.7])
fig1, ax1 = remove_axes(fig1, ax1)
ax1.set_aspect('equal')




width = 0.8
height = 0.7

x1 = -1.4; y1 = 0.0
x2 = -0.4; y2 = 0.0
x3 =  0.6; y3 = 0.0

ax1 = plot_box(x1, y1, width, height, ax1, **line_style1)
ax1 = plot_box(x2, y2, width, height, ax1, **line_style1)
ax1 = plot_box(x3, y3, width, height, ax1, **line_style1)


#points = np.random.rand(2, 15)

points = np.array([
    [0.10, 0.10],
    [0.30, 0.510],
    [0.80, 0.44],
    [0.22, 0.69],
    [0.58, 0.59],
    [0.73, 0.78],
    [0.62, 0.18],
    [0.82, 0.26],
    [0.47, 0.88],
    [0.51, 0.11],
    [0.34, 0.27],
    [0.11, 0.38],
    [0.26, 0.04]
]).T

point_p = np.array([0.38, 0.28])

points[0,:] *= width
points[1,:] *= height

for idx in range(points.shape[1]):

    
    x_new, y_new= clmb(point_p[0], point_p[1], points[0, idx], points[1, idx])    
    
    ax1.annotate('-', (x1 + points[0, idx], y1 + points[1, idx]), xycoords='data', fontsize=30)
    ax1.annotate('-', (x2 + points[0, idx], y2 + points[1, idx]), xycoords='data', fontsize=30)
    ax1.annotate('-', (x3 + x_new, y3 + y_new), xycoords='data', fontsize=30)
    

ax1.annotate('+', (x2 + point_p[0], y2 + point_p[1]), xycoords='data', color='r', fontsize=20)
ax1.annotate('+', (x3 + point_p[0], y3 + point_p[1]), xycoords='data', color='r', fontsize=20)


#xx = np.linspace(0, 2*np.pi, 501)
#yy = np.linspace(0, 2*np.pi, 501)
#
#r   = 0.4
#pos1 = [-0.6, 0.5]
#pos2 = [0.0, 0.5]
#pos3 = [0.6, 0.5]
#
#circle1 = circle_outline(xx, yy, r, pos1)
#circle2 = circle_outline(xx, yy, r, pos2)
#circle3 = circle_outline(xx, yy, r, pos3)
#
#ax1.plot(*circle1, **line_style1)
#ax1.plot(*circle2, **line_style1)
#ax1.plot(*circle3, **line_style1)
#
#
#x1_min = pos2[0]-r; x1_max = pos1[0]+r
#x2_min = pos3[0]-r; x2_max = pos2[0]+r
#
#x1_fill = np.linspace(x1_min, x1_max, 501)
#x2_fill = np.linspace(x2_min, x2_max, 501)
#
#
#ax1.plot([-1.1, 1.1], [0.5, 0.5], **line_style1)
#ax1.plot([0, -0.3], [0.5, 0.5+np.sqrt(r**2-0.3**2)], **line_style1)
#ax1.plot([-0.3, -0.3], [0.5,  0.5+np.sqrt(r**2-0.3**2)], **line_style1)
#
#
#X1, Y1 = circle1
#X2, Y2 = circle2
#
#aa1 = X1[X1>=-0.30]
#bb1 = Y1[X1>=-0.30]
#aa1 = aa1[bb1 >= 0.5]
#bb1 = bb1[bb1 >= 0.5]
#
#aa2 = X2[X2<=-0.30]
#bb2 = Y2[X2<=-0.30]
#aa2 = aa2[bb2 >= 0.5]
#bb2 = bb2[bb2 >= 0.5]
#
#aaa = np.concatenate([aa1, aa2], axis=0)
#bbb = np.concatenate([bb1, bb2], axis=0)
#
#ax1.fill_between(aaa, 1-bbb, bbb, facecolor='k', alpha=0.1)
#ax1.fill_between(0.6+aaa, 1-bbb, bbb, facecolor='k', alpha=0.1)
#
#ax1.arrow( 0.01, 0, 0.59,0,**arrow_style1)
#ax1.arrow(-0.01, 0,-0.59,0,**arrow_style1)

                   
# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)



# textboxes
txt1 = ax1.annotate('a', (x1-0.04, y1+0.01), xycoords='data', color='k',
                    **font_dict_txt)
txt3 = ax1.annotate('b', (x2-0.04, y2+0.01), xycoords='data', color='k',
                    **font_dict_txt)
txt4 = ax1.annotate('c', (x3-0.04, y3+0.01), xycoords='data', color='k',
                    **font_dict_txt)

fig1.tight_layout()
fig1.savefig('../img/screening_charge_box.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


