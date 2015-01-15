# http://stackoverflow.com/a/214657/1722562

def colorRgbToHex(rgb):
    hex = '#%02x%02x%02x' % rgb
    return hex.upper()

def colorHexToRgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
