import json
import urllib.request
from datetime import datetime

# Replace with your real API key or use environment variable
API_KEY = "at_2Kx07Ot4I87Xs659VpBQ9yBMFWLAW"

def get_client_ip(request):
    """
    Fetch the client IP address from the Django request.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def get_ip_location(ip):
    """
    Fetch country and city info for a given IP using GeoIPify API.
    """
    url = f"https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY}&ipAddress={ip}"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            location = data.get("location", {})
            return {
                "ip": data.get("ip"),
                "country": location.get("country"),
                "region": location.get("region"),
                "city": location.get("city"),
                "lat": location.get("lat"),
                "lng": location.get("lng"),
                "timezone": location.get("timezone"),
                "postalCode": location.get("postalCode"),
            }
    except Exception as e:
        # Return minimal info if API fails
        return {"ip": ip, "error": str(e)}

def get_current_datetime():
    """
    Return the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
