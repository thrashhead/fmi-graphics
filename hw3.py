def get_bezier_domains(domain, degree):
    bezier_domains = []
    num_domains = len(domain) // degree
    for i in range(num_domains):
        new_domain = domain[degree*i:degree*i + degree + 1]
        bezier_domains.append(new_domain)
        
    return bezier_domains