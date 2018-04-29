import argparse
import tmxlib

# atlas_scale     (1 hex = 25   mi  | 24      mi) composed of blocks that measure 5 hexes square
# regional_scale  (1 hex =  5   mi  |  4.8    mi) composed of large atlas hexes, with 5 regional hexes between parallel edges
# local_scale     (1 hex =  1   mi  |  0.96   mi) composed of large regional hexes, with 5 local hexes between parallel edges
# subhex_scale    (1 hex =  0.2 mi  |  0.192  mi) composed of large local hexes, with 5 subhex hexes between parallel edges
# subhex_scale    (1 hex =  0.04 mi |  0.0384 mi) composed of large local hexes, with 5 subhex hexes between parallel edges

# province 1 hex = 1 mi
# kingdom 1 hex = 6 mi
# continent 1 hex = 60 mi

# 1 square = 5 ft
# 1 square = 10 ft

# D&D 5e Scale (3 mi/hr walking speed, 30ft/6sec combat speed, 300ft/min, 18000ft/hour ~3.4 mi/hr, mi = 5280 ft -> 15840ft/mi)
hex_scale = { #    mi/hex  travel time     5e name             approx to OSR
    'world'    :  21600.00, #   2.5 years   - 
    'continent':   3600.00, # 150   days    -
    'kingdom'  :    360.00, #  15   days    -
    'province' :     60.00, #   2.5 days    continent
    'equinox'  :     36.00, #  12   hours   -
    'atlas'    :     24.00, #   8   hours   day travel on road  atlas (25mi/hex)
    'township' :      6.00, #   2   hours   kingdom             region (5mi/hex)
    'local'    :      1.00, #  20   minutes province            local  (1mi/hex)
    'ground'   :       1/6, #   3'33"
    # convert to square grid (5' 10') and movement
    # 'micro'    :      1/36, #   
}

#             single  tile    
# size        world   continent   kingdom     province    equinox     atlas   township    local    ground
# world       1       1/6         
# continent   6       1           
# kingdom     60      10          1           
# province    360     60          6           1           
# equinox     600     100         10          5/3 (1.166) 1
# atlas       900     150         15          5/2 (2.500) 3/2 (1.500) 1       
# township    3600    600         60          10          6           4       1
# local       21600   3600        360         60          36          24      6           1
# ground      129600  21600       2160        360         216         144     36          6       1

# Scale conversion for DF maps (square to hex)
# pixel to hex (https://www.redblobgames.com/grids/hexagons/)
# http://steamtunnel.blogspot.co.nz/2009/12/in-praise-of-6-mile-hex.html

if __name__ == '__main__':
    ap = argparse.ArgumentParser('Conversion Script for Tiled Formats')
    ap.add_argument('--tileset', '-t', action='store', help='Tiled Tileset file output')
    ap.add_argument('--map', '-m', action='store', help='Tiled Map file output')
    ap.add_argument('--hxm', '-x', action='store', help='Hexographer Map Data File')
    ap.add_argument('--text', '-e', action='store', help='TextMmapper Data File')
    a = ap.parse_args()

    if a.hxm:
        with open(a.hxm, 'r') as hexo_map:
            print(hexo_map.read())
    if a.text:
        with open(a.text, 'r') as text_map:
            print(text_map.read())
            