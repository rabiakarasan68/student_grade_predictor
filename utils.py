def harf_notu(score):
    if score >= 90:
        return "AA"
    elif score >= 80:
        return "BA"
    elif score >= 70:
        return "BB"
    elif score >= 60:
        return "CB"
    elif score >= 50:
        return "CC"
    else:
        return "FF"
