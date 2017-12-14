# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import arrow_array, remove_axes, circle_outline


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

plt.close('all')
fig1 = plt.figure(num=1, figsize=(12,6));
ax1 = fig1.add_subplot(111)

ax1.set_xlim([-1.2, 1.2])
ax1.set_ylim([-0.1,1.1])
fig1, ax1 = remove_axes(fig1, ax1)
ax1.set_aspect('equal')


#ar1_sta = np.array([0.15, 0.1])
#ar1_len = np.array([0.15, 0.35])
#ax1.arrow(*ar1_sta, *(1.0*ar1_len), **arrow_style2)                   
#ax1.arrow(*ar1_sta, *(0.5*ar1_len),**arrow_style1)                   
#
#ar2_sta = ar1_sta + ar1_len
#ar2_len = np.array([-0.15, 0.40])
#ax1.arrow(*ar2_sta, *(1.0*ar2_len), **arrow_style2)                   
#ax1.arrow(*ar2_sta, *(0.5*ar2_len),**arrow_style1)                   
#
#ar3_sta = np.array([0.8, 0.10])
#ar3_len = np.array([-0.15, 0.4])
#ax1.arrow(*ar3_sta, *(1.0*ar3_len), **arrow_style2)                   
#ax1.arrow(*ar3_sta, *(0.5*ar3_len),**arrow_style1)                   
#
#ar4_sta = ar3_sta + ar3_len
#ar4_len = np.array([0.2, 0.45])
#ax1.arrow(*ar4_sta, *(1.0*ar4_len), **arrow_style2)                   
#ax1.arrow(*ar4_sta, *(0.5*ar4_len),**arrow_style1)                   

xx = np.linspace(0, 2*np.pi, 501)
yy = np.linspace(0, 2*np.pi, 501)

r   = 0.4
pos1 = [-0.6, 0.5]
pos2 = [0.0, 0.5]
pos3 = [0.6, 0.5]

circle1 = circle_outline(xx, yy, r, pos1)
circle2 = circle_outline(xx, yy, r, pos2)
circle3 = circle_outline(xx, yy, r, pos3)

ax1.plot(*circle1, **line_style1)
ax1.plot(*circle2, **line_style1)
ax1.plot(*circle3, **line_style1)


x1_min = pos2[0]-r; x1_max = pos1[0]+r
x2_min = pos3[0]-r; x2_max = pos2[0]+r

x1_fill = np.linspace(x1_min, x1_max, 501)
x2_fill = np.linspace(x2_min, x2_max, 501)


ax1.plot([-1.1, 1.1], [0.5, 0.5], **line_style1)
ax1.plot([0, -0.3], [0.5, 0.5+np.sqrt(r**2-0.3**2)], **line_style1)
ax1.plot([-0.3, -0.3], [0.5,  0.5+np.sqrt(r**2-0.3**2)], **line_style1)


X1, Y1 = circle1
X2, Y2 = circle2

aa1 = X1[X1>=-0.30]
bb1 = Y1[X1>=-0.30]
aa1 = aa1[bb1 >= 0.5]
bb1 = bb1[bb1 >= 0.5]

aa2 = X2[X2<=-0.30]
bb2 = Y2[X2<=-0.30]
aa2 = aa2[bb2 >= 0.5]
bb2 = bb2[bb2 >= 0.5]

aaa = np.concatenate([aa1, aa2], axis=0)
bbb = np.concatenate([bb1, bb2], axis=0)

ax1.fill_between(aaa, 1-bbb, bbb, facecolor='k', alpha=0.1)
ax1.fill_between(0.6+aaa, 1-bbb, bbb, facecolor='k', alpha=0.1)

ax1.arrow( 0.01, 0, 0.59,0,**arrow_style1)
ax1.arrow(-0.01, 0,-0.59,0,**arrow_style1)

                   
# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)



# textboxes
txt1 = ax1.annotate(r'$ \vartheta_k $', (0.46, 0.52), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt3 = ax1.annotate(r'$ q $', (0.40, 0.13), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt4 = ax1.annotate(r'$ q $', (0.60, 0.13), xycoords='figure fraction', color='k',
                    **font_dict_txt)

txt5 = ax1.annotate(r'$ k_F $', (0.45, 0.62), xycoords='figure fraction', color='k',
                    **font_dict_txt)



fig1.savefig('../img/sq_graph_integration.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


