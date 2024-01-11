build_carolina = {
    'US': {
        'South Carolina': {
            'Greenville': '411 University Ridge',
        },
        'North Carolina': {
            'Asheville': '123 Sesame Street'
        }
    }
}

for country in build_carolina:
    for state in build_carolina[country]:
        print(country, state, end=': ')
        for city in build_carolina[country][state]:
            print(city)
