def get_city_country_name(city, country, population=''):
    if population:
        full_info = f"{city}, {country} - population {population}"
    else:
        full_info = f"{city}, {country}"
    return full_info.title()
