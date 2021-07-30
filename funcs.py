def style_func(x):
    pop = x['properties']['POP2005']

    if pop <= 1000000:
        return {'fillColor': 'green'}
    elif pop <= 10000000:
        return {'fillColor': 'yellow'}
    elif pop <= 20000000:
        return {'fillColor': 'orange'}
    else:
        return {'fillColor': 'red'}