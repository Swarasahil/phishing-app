
def extract_features(url):
    return {
        'url_length': len(url),
        'has_at_symbol': '@' in url,
        'has_dash': '-' in url,
        'https': url.startswith("https"),
        'num_dots': url.count('.'),
    }
