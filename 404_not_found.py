# Jesus Carlos Martinez Gonzalez
# 30/03/2024
# 404 Not found (https://www.codechef.com/problems/ERROR404)

"""
Chef's website has a specific response mechanism based on the HTTP status code received:
• Ifthe response code is 404, the website will return NOT FOUND.
• For any other response code different from 404, the website will return FOUND.
Given the response code as X, determine the website response.
"""

print("NOT FOUND" if input() == "404" else "FOUND")
