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

fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

#ax1.plot(x, np.polyval([0.2,0,0,0,0],x), **line_style1)
#ax1.plot(x, np.polyval([1,0,0],x), **line_style_red)
#ax1.plot(x, np.polyval([0.4,0,-0.7,0,0],x), **line_style_blue)
#ax1.plot(x, np.polyval([0.8, -1.0], x), **line_style_blue)
#ax1.plot(x, np.polyval([0.8, 0], x), **line_style_red)
ax1.set_xlim([-0.1,1.0])
ax1.set_ylim([-0.1,1.0])

# changes axes to arrow head
#fig1, ax1 = put_arrowhead_axes(fig1, ax1)
fig1, ax1 = arrow_array(fig1, ax1, x0=-0.1, y0=0, arr_size=[4,3], 
                        spin_orientation='all_up')

fig1, ax1 = arrow_array(fig1, ax1, x0=0.3, y0=0, arr_size=[4,3], 
                        spin_orientation='anti_parallel')

# set opalic
#ax1.patch.set_facecolor('none')
#ax1.patch.set_alpha(0)


# axis label
#xlabel = ax1.annotate('m', (0.90, 0.25), xycoords='figure fraction',
#                      **font_dict_label)
#ylabel = ax1.annotate('F', (0.46, 0.88), xycoords='figure fraction',
#                      **font_dict_label)

# textboxes
txt1 = ax1.annotate(r'$ J > 0 $', (0.13, 0.47), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt2 = ax1.annotate(r'$ J < 0 $', (0.43, 0.47), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt3 = ax1.annotate(r'$ J < 0 $', (0.72, 0.47), xycoords='figure fraction', color='k',
                    **font_dict_txt)




fig1.savefig('../img/exch_spin_config.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


