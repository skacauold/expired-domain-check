import whois

def get_domain_expiry_date(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if isinstance(domain_info.expiration_date, list):
            expiry_date = domain_info.expiration_date[0]
        else:
            expiry_date = domain_info.expiration_date
        return expiry_date
    except Exception as e:
        return f"Error: {e}"

domain_name = "google.com"  # Replace with the domain name you want to check
expiry_date = get_domain_expiry_date(domain_name)
print(f"The expiry date of {domain_name} is: {expiry_date}")
