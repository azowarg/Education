"""Return result of check"""
from website_alive.check_response import check

print("Site available" if check() else "Site unavailable")
