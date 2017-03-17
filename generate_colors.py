import getcolor as gc


def get_color_set():
    primary_color = '#331177'
    secondary_color = '#224477'
    accent_color = '#bb192a'
    text_color = '#eee'
    inv_text_color = 'rgba(0,0,0,0.4)'

    colors = gc.get_colors()
    print colors
    print 'Colors len:', len(colors)
    print colors[0][2][2]

    if len(colors) == 2:
        primary_color = colors[0][0]
        secondary_color = colors[1][0]
        if colors[0][2][2] > 50:
            text_color = '#222'
            inv_text_color = 'rgba(255,255,255,0.4)'

    elif len(colors) == 3:
        primary_color = colors[0][0]
        secondary_color = colors[1][0]
        accent_color = colors[2][0]
        if colors[0][2][2] > 50:
            text_color = '#222'
            inv_text_color = 'rgba(255,255,255,0.4)'

    elif len(colors) == 4:
        primary_color = colors[1][0]
        secondary_color = colors[2][0]
        accent_color = colors[3][0]
        if colors[1][2][2] > 50:
            text_color = '#222'
            inv_text_color = 'rgba(255,255,255,0.4)'

    # primary_color = '#999999'
    # secondary_color='#777777'
    # accent_color='#eee'
    # text_color='#333'
    # inv_text_color='rgba(0,0,0,0.4)'

    return primary_color, secondary_color, accent_color, text_color, inv_text_color