# -*- coding: utf-8 -*-
"""
Condensed matter - script

Contains plot function to plot the graphical solution to the Magnetisation in 
a Ferromagnet

@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt



from base_axes import put_arrowhead_axes, arrow_array


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
    'size':                 22,
}


#==============================================================================
# plot function
#==============================================================================
x = np.linspace(0,1.32, 2001)

x = x[1:]

fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

ax1.plot(x, -0.4/x, **line_style1)
ax1.plot(x, -0.3*np.exp(-x*3.0)/x, **line_style1)
ax1.set_xlim([0.0,1.4])
ax1.set_ylim([-1.0,0.3])




# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)


# axis label
xlabel = ax1.annotate(r'$r$', (0.90, 0.75), xycoords='figure fraction',
                      **font_dict_label)
ylabel = ax1.annotate(r'$ \phi(r) $', (0.03, 0.90), xycoords='figure fraction',
                      **font_dict_label)

# textboxes
txt1 = ax1.annotate(r'$ \exp(-k_0 r)/r $', (0.38, 0.54), xycoords='figure fraction', color='k',
                    **font_dict_txt)

txt2 = ax1.annotate(r'$ 0 $', (0.09, 0.72), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt3 = ax1.annotate(r'$ 1/r $', (0.70, 0.42), xycoords='figure fraction', color='k',
                    **font_dict_txt)



ax1.fill_between(x, -0.3*np.exp(-x*3.0)/x, color='k', alpha=0.1)

# changes axes to arrow head
fig1, ax1 = put_arrowhead_axes(fig1, ax1)


fig1.savefig('../img/screening_yukawa.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


