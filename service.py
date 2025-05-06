import hashlib
import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def create_short_url(self, long_url):
        # Create a hash of the long URL (using MD5 for simplicity)
        short_url = hashlib.md5(long_url.encode()).hexdigest()[:6]  # Take first 6 characters of the hash
        self.url_mapping[short_url] = long_url
        return short_url

    def get_long_url(self, short_url):
        return self.url_mapping.get(short_url)