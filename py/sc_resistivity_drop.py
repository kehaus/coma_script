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
    'size':                 20,
}


#==============================================================================
# plot function
#==============================================================================
x = np.linspace(0,2, 2001)

fig1 = plt.figure(1); fig1.clf()
ax1 = fig1.add_subplot(111)

#ax1.plot(x[:400], 4*x[:400]**2, **line_style1)
ax1.plot([x[401], x[401]], [0, 0.255*x[400]**-1], '--k')
ax1.plot([x[401], x[401]], [0, 0.2*x[401]**2 + 0.2], **line_style1)
ax1.plot(x[400:], 0.2*x[400:]**2 + 0.2, **line_style1)
ax1.set_xlim([-0.2,1.5])
ax1.set_ylim([-0.2,0.7])

# changes axes to arrow head
fig1, ax1 = put_arrowhead_axes(fig1, ax1)



# set opalic
ax1.patch.set_facecolor('none')
ax1.patch.set_alpha(0)


# axis label
xlabel = ax1.annotate('$T$', (0.90, 0.16), xycoords='figure fraction',
                      **font_dict_label)
ylabel = ax1.annotate(r'$ \rho $', (0.14, 0.90), xycoords='figure fraction',
                      **font_dict_label)

# textboxes
txt1 = ax1.annotate(r'$ SC\ state $', (0.24, 0.75), xycoords='figure fraction', color='k',
                    **font_dict_txt)

txt2 = ax1.annotate(r'$ T_C $', (0.38, 0.18), xycoords='figure fraction', color='k',
                    **font_dict_txt)
txt3 = ax1.annotate(r'$ Normal\ state $', (0.50, 0.75), xycoords='figure fraction', color='k',
                    **font_dict_txt)
#txt4 = ax1.annotate(r'$ \chi_{\parallel} $', (0.27, 0.36), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#txt5 = ax1.annotate(r'$ \chi_{\perp} $', (0.25, 0.70), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#txt6 = ax1.annotate(r'$ \vec{B}_\parallel $', (0.83, 0.78), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#txt7 = ax1.annotate(r'$ \vec{B}_\perp $', (0.83, 0.63), xycoords='figure fraction', color='k',
#                    **font_dict_txt)
#

ax1.fill_between([0, x[401]], [ax1.get_ylim()[1]]*2, color='k', alpha=0.1)


#fig1, ax1 = arrow_array(fig1, ax1, arr_size=[3,2], 
#                        x0=1.3, y0=0.5, dx=0.11, dy=0.13, length=0.08,
#                        spin_orientation='anti_parallel')
#
#ax1.arrow(1.72, 0.60    , 0, 0.16, fc='k', ec='k', head_length=0.04, head_width=0.025,
#          length_includes_head=True, clip_on=False)
#
#ax1.plot(1.72 + 0.04*np.sin(np.linspace(0,2*np.pi,51)),
#         0.49 + 0.025*np.cos(np.linspace(0,2*np.pi,51)), '-k')
#ax1.scatter(1.72, 0.49, s=1, c='k')



##plot 2
#fig2 = plt.figure(2); fig2.clf()
#ax2 = fig2.add_subplot(111)
#
#fig2, ax2 = arrow_array(fig2, ax2, arr_size=[3,2])
#
## set opalic
#ax2.patch.set_facecolor('none')
#ax2.patch.set_alpha(0)



fig1.savefig('../img/sc_resistivity_drop.pdf', transparent=True)

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    pass


