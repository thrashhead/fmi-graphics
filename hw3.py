def get_bezier_domains(domain, degree):
    bezier_domains = []
    num_domains = len(domain) // degree
    for i in range(num_domains):
        new_domain = domain[degree*i:degree*i + degree + 1]
        bezier_domains.append(new_domain)
        
    return bezier_domains

def pick_color(repeat):
    while True:
        for _ in range(repeat):
            yield 'red'
        for _ in range(repeat):
            yield 'green'
        for _ in range(repeat):
            yield 'blue'
        for _ in range(repeat):
            yield 'yellow'
        for _ in range(repeat):
            yield 'black'