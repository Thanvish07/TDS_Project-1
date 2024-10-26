import requests
import csv
import time

# GitHub API credentials
TOKEN = "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"
HEADERS = {"Authorization": f"token {TOKEN}"}

# Parameters
LOCATION = "Moscow"
MIN_FOLLOWERS = 50
USER_FIELDS = [
    "login", "name", "company", "location", "email", "hireable", "bio",
    "public_repos", "followers", "following", "created_at"
]
REPO_FIELDS = [
    "login", "full_name", "created_at", "stargazers_count", "watchers_count",
    "language", "has_projects", "has_wiki", "license_name"
]

# Base URLs
USER_SEARCH_URL = "https://api.github.com/search/users"
REPO_URL = "https://api.github.com/users/{}/repos"

# Clean company name format
def clean_company(company):
    if company:
        return company.replace("@", "").strip().upper()
    return ""

# Fetch users in Moscow with over 50 followers
def fetch_users(location, min_followers):
    users = []
    params = {"q": f"location:{location} followers:>{min_followers}", "per_page": 100}
    
    while True:
        response = requests.get(USER_SEARCH_URL, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch users: {response.status_code}")
            break
        
        data = response.json()
        print(f"Fetched {len(data.get('items', []))} users in this page.")
        
        for item in data.get("items", []):
            user_details = fetch_user_details(item["login"])
            if user_details:
                users.append(user_details)
        
        if "next" in response.links:
            time.sleep(1)  # To avoid hitting rate limit
            params = response.links["next"]["url"].split('?')[1]  # Update params for the next request
        else:
            break
        
    print(f"Total users fetched: {len(users)}")
    return users

# Fetch detailed user data
def fetch_user_details(login):
    user_url = f"https://api.github.com/users/{login}"
    response = requests.get(user_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to fetch user details for {login}: {response.status_code}")
        return None
    
    user_data = response.json()
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

# Fetch repository data for a user
def fetch_repositories(login):
    repos = []
    params = {"sort": "pushed", "per_page": 100}
    
    while True:
        response = requests.get(REPO_URL.format(login), headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch repos for {login}: {response.status_code}")
            break
        
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
            if len(repos) >= 500:
                break
        
        if "next" in response.links:
            time.sleep(1)  # Rate limiting between requests
            params = response.links["next"]["url"].split('?')[1]  # Update params for the next request
        else:
            break
            
    return repos

# Save data to CSV files
def save_to_csv(data, filename, fieldnames):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Main function to run the scraper
def main():
    users = fetch_users(LOCATION, MIN_FOLLOWERS)
    if users:
        save_to_csv(users, "users.csv", USER_FIELDS)
        print("Saved users.csv")

    all_repos = []
    for user in users:
        repos = fetch_repositories(user["login"])
        all_repos.extend(repos)
        time.sleep(1)  # Rate limiting between users
    
    if all_repos:
        save_to_csv(all_repos, "repositories.csv", REPO_FIELDS)
        print("Saved repositories.csv")

if __name__ == "__main__":
    main()
