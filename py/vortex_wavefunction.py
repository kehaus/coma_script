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
arrow_style_blue = {
            'fc':               khBlue,
            'ec':               khBlue,
            'head_width':       1./30,
            'head_length':      1./20,
            'lw':               1.5,
            'overhang':         0.0}

arrow_style_red = arrow_style_blue.copy()
arrow_style_red['fc'] = khRed; arrow_style_red['ec'] = khRed            

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
# functions
#==============================================================================

def psi(x, xi=1, psi_0=1):
    """ """
    return psi_0 * np.tanh(x/xi)

#==============================================================================
# plot function
#==============================================================================
x = np.linspace(0, 2.2, 1001)

fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

ax1.plot(x, psi(x,xi=0.5), **line_style_blue)
ax1.plot(x, psi(x,xi=2.0), **line_style_red)
ax1.set_xlim([0,2.4])
ax1.set_ylim([0,1.2])

# changes axes to arrow head
fig1, ax1 = put_arrowhead_axes(fig1, ax1)



# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)


# axis label
xlabel = ax1.annotate('$x$', (0.90, 0.05), xycoords='figure fraction',
                      **font_dict_label)
ylabel = ax1.annotate('$\psi(x)$', (0.03, 0.91), xycoords='figure fraction',
                      **font_dict_label)

# textboxes
txt2 = ax1.annotate(r'$ \xi_1 $', (0.18, 0.60), xycoords='figure fraction', color=khBlue,
                    **font_dict_txt)
txt3 = ax1.annotate(r'$ \xi_2 $', (0.27, 0.43), xycoords='figure fraction', color=khRed,
                    **font_dict_txt)

ax1.arrow(0.05, 0.70, 0.35, 0,**arrow_style_blue,
          length_includes_head=True, clip_on=False)
ax1.arrow(0.05, 0.45, 0.82, 0,**arrow_style_red,
          length_includes_head=True, clip_on=False)


fig1.savefig('../img/vortex_wavefunction.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


