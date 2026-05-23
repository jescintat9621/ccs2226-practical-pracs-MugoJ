# Part A: Australia Map Coloring
regions_aus = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors_aus = ['Blue', 'Red', 'Green']

neighbors_aus = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['NSW', 'SA'],
    'T': []
}

assignment_aus = {}

def is_valid_aus(region, color):
    for neighbor in neighbors_aus[region]:
        if neighbor in assignment_aus and assignment_aus[neighbor] == color:
            return False
    return True

def color_aus(index):
    if index == len(regions_aus):
        return True
    region = regions_aus[index]
    for color in colors_aus:
        if is_valid_aus(region, color):
            assignment_aus[region] = color
            if color_aus(index + 1):
                return True
            del assignment_aus[region]
    return False

print("Australia Map Coloring ")
if color_aus(0):
    print(assignment_aus)


# Part B: Nairobi Sub-Counties Least Colors
sub_counties = [
    'Westlands', 'DagorettiNorth', 'DagorettiSouth', 'Langata', 'Kibra',
    'Roysambu', 'Kasarani', 'Ruaraka', 'EmbakasiNorth', 'EmbakasiSouth',
    'EmbakasiCentral', 'EmbakasiEast', 'EmbakasiWest', 'Makadara',
    'Kamukunji', 'Starehe', 'Mathare'
]

neighbors_nairobi = {
    'Westlands': ['DagorettiNorth', 'Langata', 'Kibra', 'Starehe', 'Roysambu'],
    'DagorettiNorth': ['Westlands', 'DagorettiSouth', 'Kibra'],
    'DagorettiSouth': ['DagorettiNorth', 'Langata', 'Kibra'],
    'Langata': ['Westlands', 'DagorettiSouth', 'Kibra', 'EmbakasiSouth'],
    'Kibra': ['Westlands', 'DagorettiNorth', 'DagorettiSouth', 'Langata', 'Starehe'],
    'Roysambu': ['Westlands', 'Kasarani', 'Ruaraka', 'Starehe'],
    'Kasarani': ['Roysambu', 'Ruaraka', 'EmbakasiEast'],
    'Ruaraka': ['Roysambu', 'Kasarani', 'Mathare', 'Starehe'],
    'Mathare': ['Ruaraka', 'Starehe', 'Kamukunji', 'EmbakasiNorth'],
    'Starehe': ['Westlands', 'Roysambu', 'Ruaraka', 'Mathare', 'Kamukunji', 'Kibra', 'Makadara'],
    'Kamukunji': ['Starehe', 'Mathare', 'EmbakasiNorth', 'EmbakasiWest', 'Makadara'],
    'Makadara': ['Starehe', 'Kamukunji', 'EmbakasiWest', 'EmbakasiSouth', 'EmbakasiCentral'],
    'EmbakasiNorth': ['Mathare', 'Kamukunji', 'EmbakasiWest', 'EmbakasiCentral'],
    'EmbakasiWest': ['Kamukunji', 'EmbakasiNorth', 'EmbakasiCentral', 'Makadara'],
    'EmbakasiCentral': ['EmbakasiNorth', 'EmbakasiWest', 'Makadara', 'EmbakasiEast', 'EmbakasiSouth'],
    'EmbakasiSouth': ['Langata', 'Makadara', 'EmbakasiCentral', 'EmbakasiEast'],
    'EmbakasiEast': ['Kasarani', 'EmbakasiCentral', 'EmbakasiSouth']
}

assignment_nairobi = {}

def is_valid_nairobi(sub_county, color):
    for neighbor in neighbors_nairobi[sub_county]:
        if neighbor in assignment_nairobi and assignment_nairobi[neighbor] == color:
            return False
    return True

def color_nairobi(index, color_list):
    if index == len(sub_counties):
        return True
    sub_county = sub_counties[index]
    for color in color_list:
        if is_valid_nairobi(sub_county, color):
            assignment_nairobi[sub_county] = color
            if color_nairobi(index + 1, color_list):
                return True
            del assignment_nairobi[sub_county]
    return False

print("\nNairobi Sub-Counties Map Coloring ")
available_colors = ['Color1', 'Color2', 'Color3', 'Color4']
for num_colors in range(1, 5):
    test_colors = available_colors[:num_colors]
    assignment_nairobi.clear()
    if color_nairobi(0, test_colors):
        print(f"Successfully colored using {num_colors} colors!")
        print(assignment_nairobi)
        break