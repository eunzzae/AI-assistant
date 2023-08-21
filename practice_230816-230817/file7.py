from requests import get

websites = (
    "google.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/200",
    "https://httpstat.us/101"
)

# results = {}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = get(website)
#     if response.status_code ==200:
#         results[website] = "OK"
#     else:
#         results[website] = "FAILED"

# print(results)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code <200:
        results[website]="continue"
    elif response.status_code <300:
        results[website] = "success"
    elif response.status_code <400:
        results[website] ="redirection"
    elif response.status_code <500:
        results[website] = "client error"
    elif response.status_code <600:
        results[website]="server error"
    else:
        results[website]="fail"
print(results)