import colorgram


def get_rgb(image_path):
    rgb_colors = []
    colors = colorgram.extract(image_path, 30)
    for color in colors:
        rgb_colors.append(tuple([color.rgb.r, color.rgb.g, color.rgb.b]))

    return rgb_colors









