# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import put_arrowhead_axes


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
x = np.linspace(0,np.pi/2, 1001)

fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

ax1.plot(1.6*np.sin(x), 0.7*np.cos(x), **line_style1)
#ax1.plot(x, np.polyval([0.8, -1.0], x), **line_style_blue)
#ax1.plot(x, np.polyval([0.8, 0], x), **line_style_red)
ax1.set_xlim([-0.2,2.4])
ax1.set_ylim([-0.2,1.0])

# changes axes to arrow head
fig1, ax1 = put_arrowhead_axes(fig1, ax1)



# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)


# axis label
xlabel = ax1.annotate('t', (0.90, 0.16), xycoords='figure fraction',
                      **font_dict_label)
ylabel = ax1.annotate('m', (0.12, 0.89), xycoords='figure fraction',
                      **font_dict_label)

# textboxes
txt2 = ax1.annotate(r'$ T = T_C $', (0.62, 0.17), xycoords='figure fraction', color='k',
                    **font_dict_txt)




fig1.savefig('../img/ferromag_M_T.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


