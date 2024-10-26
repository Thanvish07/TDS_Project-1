import requests
import csv
import time

# GitHub authentication - replace 'YOUR_TOKEN_HERE' with your actual GitHub token
headers = {
    "Authorization": "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"
}

# Set up base URLs and parameters
user_url = "https://api.github.com/search/users?q=location:Moscow+followers:>50"
repo_url = "https://api.github.com/users/{}/repos"
params = {"per_page": 500}

def fetch_users():
    response = requests.get(user_url, headers=headers)
    response.raise_for_status()
    return response.json()['items']

def clean_company(company):
    if company:
        return company.replace("@", "").strip().upper()
    return ""

def fetch_user_details(login):
    user_response = requests.get(f"https://api.github.com/users/{login}", headers=headers)
    user_response.raise_for_status()
    user_data = user_response.json()
    
    return {
        "login": user_data["login"],
        "name": user_data.get("name", ""),
        "company": clean_company(user_data.get("company", "")),
        "location": user_data.get("location", ""),
        "email": user_data.get("email", ""),
        "hireable": str(user_data.get("hireable", "")).lower(),
        "bio": user_data.get("bio", ""),
        "public_repos": user_data["public_repos"],
        "followers": user_data["followers"],
        "following": user_data["following"],
        "created_at": user_data["created_at"]
    }

def fetch_repositories(login):
    repos = []
    response = requests.get(repo_url.format(login), headers=headers, params=params)
    response.raise_for_status()
    for repo in response.json():
        repos.append({
            "login": login,
            "full_name": repo["full_name"],
            "created_at": repo["created_at"],
            "stargazers_count": repo["stargazers_count"],
            "watchers_count": repo["watchers_count"],
            "language": repo.get("language", ""),
            "has_projects": str(repo.get("has_projects", False)).lower(),
            "has_wiki": str(repo.get("has_wiki", False)).lower(),
            "license_name": repo["license"]["key"] if repo["license"] else ""
        })
    return repos

def save_to_csv(data, filename, fieldnames):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Main Script
users = fetch_users()
users_data = []
repositories_data = []

for user in users:
    try:
        user_details = fetch_user_details(user['login'])
        users_data.append(user_details)
        repositories_data.extend(fetch_repositories(user['login']))
        time.sleep(1)  # To avoid hitting the rate limit
    except Exception as e:
        print(f"Error fetching data for {user['login']}: {e}")

# Save data to CSV files
user_fields = ["login", "name", "company", "location", "email", "hireable", "bio", 
               "public_repos", "followers", "following", "created_at"]
repo_fields = ["login", "full_name", "created_at", "stargazers_count", "watchers_count", 
               "language", "has_projects", "has_wiki", "license_name"]

save_to_csv(users_data, "users.csv", user_fields)
save_to_csv(repositories_data, "repositories.csv", repo_fields)

print("Data scraping completed. Files saved as users.csv and repositories.csv.")
