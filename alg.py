inbox_data = ['С', 'С', 'З', 'С', 'К', 'З', 'З', 'З',
          'К', 'К', 'С', 'З', 'С', 'С', 'К', 'З']


def sort_colors(data):
    green = []
    blue = []
    red = []
    for a in data:
        if a == 'З':
            green.extend('З')
        if a == 'С':
            blue.extend('С')
        if a == 'К':
            red.extend('К')
    return green + blue + red


print(sort_colors(inbox_data))
