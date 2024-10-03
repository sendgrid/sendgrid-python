def build_url(url: str, region: str) -> str:
    base_url = "https://api.sendgrid.com"

    if region and isinstance(region, str):
        new_url = f"https://api.{region}.sendgrid.com"
    else:
        new_url = base_url

    # Ensure that there's a '/' before appending the url
    if not new_url.endswith('/'):
        new_url += '/'

    new_url += url.lstrip('/')

    return new_url

