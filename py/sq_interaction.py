# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import arrow_array, remove_axes


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
fig1 = plt.figure(num=1,figsize=(8,4));
ax1 = fig1.add_subplot(111)

ax1.set_xlim([0.1,0.9])
ax1.set_ylim([0.1,0.9])
fig1, ax1 = remove_axes(fig1, ax1)


ar1_sta = np.array([0.15, 0.1])
ar1_len = np.array([0.15, 0.35])
ax1.arrow(*ar1_sta, *(1.0*ar1_len), **arrow_style2)                   
ax1.arrow(*ar1_sta, *(0.5*ar1_len),**arrow_style1)                   

ar2_sta = ar1_sta + ar1_len
ar2_len = np.array([-0.15, 0.40])
ax1.arrow(*ar2_sta, *(1.0*ar2_len), **arrow_style2)                   
ax1.arrow(*ar2_sta, *(0.5*ar2_len),**arrow_style1)                   

ar3_sta = np.array([0.8, 0.10])
ar3_len = np.array([-0.15, 0.4])
ax1.arrow(*ar3_sta, *(1.0*ar3_len), **arrow_style2)                   
ax1.arrow(*ar3_sta, *(0.5*ar3_len),**arrow_style1)                   

ar4_sta = ar3_sta + ar3_len
ar4_len = np.array([0.2, 0.45])
ax1.arrow(*ar4_sta, *(1.0*ar4_len), **arrow_style2)                   
ax1.arrow(*ar4_sta, *(0.5*ar4_len),**arrow_style1)                   





xx = np.linspace(ar2_sta[0], ar4_sta[0], 101)
yy = np.linspace(ar2_sta[1], ar4_sta[1], 101)
line_coeff = np.polyfit(xx, yy, 1)


ax1.plot(xx, np.polyval(line_coeff, xx)+ 0.04*np.sin(np.linspace(0,12,101)*np.pi),
         lw=1.4, c='k')



                   
# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)



# textboxes
#txt1 = ax1.annotate(r'$ J > 0 $', (0.22, 0.87), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#txt2 = ax1.annotate(r'$ J < 0 $', (0.69, 0.87), xycoords='figure fraction', color='k',
#                    **font_dict_txt)

fig1.savefig('../img/sq_interaction.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


