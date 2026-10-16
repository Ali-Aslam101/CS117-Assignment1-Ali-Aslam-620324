def star_to_delta(ra, rb, rc):
    numerator = ra * rb + rb * rc + rc * ra   # calculated once, reused three times
    r_ab = numerator / rc
    r_bc = numerator / ra
    r_ca = numerator / rb
    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)
print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))
