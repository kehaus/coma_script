# -*- coding: utf-8 -*-
"""
Contains Base classes for the different axes used to produce the plots and 
graphs in the COMA-script


@author: kh
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib





def put_arrowhead_axes(fig=None, ax=None, 
                       head_width=0.03, head_length=0.05, 
                       line_width=2, overhang=0.3):
    """returns ax-object with x- and y-axis changed to arrow-head
    
    formats the given matplotlib axes-object on a way. That all axis features
    except the axis-labels are removed and replaced by arrowhead axes. fig is 
    is the corresponding matplotlib figure object   
    
    
    code adapted from:
    https://stackoverflow.com/questions/17646247/how-to-make-fuller-axis-arrows-with-matplotlib
    
    
    Example
    -------
    * use default settings
        >>> fig = plt.figure(1)
        >>> ax = fig.add_subplot(111)
        >>> fig, ax = put_arrow_head_axes(fig=fig, ax=ax)
    * change arrow appearance
        >>> fig = plt.figure(1)
        >>> ax = fig.add_subplot(111)
        >>> arrow_style = {'head_width':0.02, 
        ...                'head_length':0.02', 
        ...                'line_width': 2, 
        ...                'overhang': 0.3}
        >>> fig,ax = put_arrow_headaxes(fig=fig, ax=ax, **arrow_style)


    """
    
    if fig ==None:
        fig = plt.figure()
    if ax == None:
        ax = fig_subplot(111)
#    if arrow_style == None:
#        arrow_style = { # default arrow style parameter
#            'head width':   1./30,
#            'head length':  1./20,
#            'line width':   2.0,
#            'overhang':     0.3}
        
        
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    
    for side in ['bottom', 'right', 'top', 'left']:
        ax.spines[side].set_visible(False)

    # remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')  # tick marker
    ax.yaxis.set_ticks_position('none')

    # get width and height of axes object to compute matching arrowhead length
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height
    
    #manual arrowhead width and length
    hw = head_width*(ymax-ymin)
    hl = head_length*(xmax-xmin)
    lw = line_width
    ohg = overhang
    
    #compute matching arrowhead length and width
    yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width
    yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

    # draw x and y arrow-head axes
    ax.arrow(xmin, 0., xmax-xmin, 0., fc='k', ec='k', 
             lw=lw, head_width=hw, head_length=hl, overhang = ohg,
             length_includes_head=True, clip_on=False)
    
    ax.arrow(0., ymin, 0., ymax-ymin, fc='k', ec='k',
             lw = lw, head_width=yhw, head_length=yhl, overhang=ohg,
             length_includes_head=True, clip_on=False)

    return fig, ax





def arrow_array(fig=None, ax=None, 
                x0=0, y0=0, dx=0.07, dy=0.1, length=0.05, arr_size=[3,3], 
                arrow_style=None, spin_orientation='random'):
    """plots array of arrow into given axes
    
    
    
    
    
    Example
    -------
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111)
    >>> fig, ax = arrow_array(fig, ax)
    
    
    
    """
    
    if fig ==None:
        fig = plt.figure()
    if ax == None:
        ax = fig_subplot(111)

    if arrow_style == None:
        arrow_style = { # default arrow style parameter
            'fc':               'k',
            'ec':               'k',
            'head_width':       1./70,
            'head_length':      1./50,
            'lw':               0.5,
            'overhang':         0.3}
        
    for side in ['bottom', 'right', 'top', 'left']:
        ax.spines[side].set_visible(False)

    # remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')  # tick marker
    ax.yaxis.set_ticks_position('none')

    
    x0 = np.ones(arr_size) * x0
    y0 = np.ones(arr_size) * y0    
    
    if spin_orientation == 'all_up':
        vector_arr = length*np.concatenate((np.zeros([*arr_size,1]),np.ones([*arr_size,1])), axis=2)    
        y0 -= length*0.5
    if spin_orientation == 'all_down':
        vector_arr = -length*np.concatenate((np.zeros([*arr_size,1]),np.ones([*arr_size,1])), axis=2)    
        y0 += length*0.5
    if spin_orientation == 'anti_parallel':
        vector_arr = length*np.concatenate((np.zeros([*arr_size,1]),np.ones([*arr_size,1])), axis=2) 
        for i in range(arr_size[0]):
            for j in range(arr_size[1]):
                vector_arr[i,j] *= (-1.)**(i+j)
                y0[i,j] += length*( (i+j)%2) - length*0.5
                
    if spin_orientation == 'random':
        vector_arr= np.zeros([*arr_size,2])
        for i in range(arr_size[0]):
            for j in range(arr_size[1]):
                phi = np.random.random_sample() *2*np.pi
                vector_arr[i,j,:]  = np.array([np.sin(phi), np.cos(phi)]) * length
                x0[i,j] -= np.sin(phi)*length*0.5
                y0[i,j] -= np.cos(phi)*length*0.5
            
    for i in range(arr_size[0]):
        for j in range(arr_size[1]):
            ax.arrow(x0[i,j]+i*dx, y0[i,j]+j*dy, vector_arr[i,j,0], vector_arr[i,j,1],
                     **arrow_style, length_includes_head=True, clip_on=False)
    
    return fig, ax



def remove_axes(fig, ax):
    """removes axes from given axes object"""
    for side in ['bottom', 'right', 'top', 'left']:
        ax.spines[side].set_visible(False)

    # remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')  # tick marker
    ax.yaxis.set_ticks_position('none')
    
    
    return fig, ax


def circle_outline(x, y, radius, pos):
    """returns X,Y coordinates of the outline of circle with radius and center
    
    """
    X = pos[0]+radius*np.cos(x)
    Y = pos[1]+radius*np.sin(x)
    return X,Y

#==============================================================================
# Main function
#==============================================================================

if __name__ == "__main__":
    
    # get arrowhead axis
    fig1 = plt.figure(1); fig1.clf()
    ax1 = fig1.add_subplot(111)   
    
#    fig1, ax = put_arrowhead_axes(fig1, ax)
       
    fig1, ax1 = arrow_array(fig1, ax1)
    
    
    pass

