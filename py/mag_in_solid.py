# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import arrow_array


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
# plot function
#==============================================================================
x = np.linspace(-2,2, 1001)

plt.close('all')
fig1 = plt.figure(num=1,figsize=(8,3));
ax1 = fig1.add_subplot(111)

ax1.set_xlim([-0.15,0.93])
ax1.set_ylim([-0.14,0.25])

# changes axes to arrow head
fig1, ax1 = arrow_array(fig1, ax1, x0=-0.15, y0=0, arr_size=[7,3], 
                        spin_orientation='random')

fig1, ax1 = arrow_array(fig1, ax1, x0=0.50, y0=0, arr_size=[7,3], 
                        spin_orientation='all_up')
                        
#fig1, ax1 = arrow_array(fig1, ax1, x0=0.78, y0=0.08, arr_size=[1,1], 
#                        spin_orientation='anti_parallel')
#                        
#fig1, ax1 = arrow_array(fig1, ax1, x0=0.88, y0=0.2, arr_size=[1,1], 
#                        spin_orientation='anti_parallel')
#
#plt.plot([0.82, 0.93],[0.075, 0.075], '-k', lw=1.2)
#plt.plot([0.80, 0.86],[0.12, 0.170], '-k', lw=1.2)
#plt.plot([0.95, 0.88],[0.12, 0.170], '-k', lw=1.2)


# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)



# textboxes
txt1 = ax1.annotate(r'$ M = 0 $', (0.22, 0.10), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt2 = ax1.annotate(r'$ M \neq 0 $', (0.70, 0.10), xycoords='figure fraction', color='k',
                    **font_dict_txt)
#txt3 = ax1.annotate(r'$ J < 0 $', (0.78, 0.87), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#txt4 = ax1.annotate(' ? ', (0.86, 0.41), xycoords='figure fraction', color='k',
#                    **font_dict_label)
#
#


fig1.savefig('../img/mag_in_solid.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


