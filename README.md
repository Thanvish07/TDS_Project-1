# GitHub Users in Moscow with Over 50 Followers

- **Data Collection Process**: We used the GitHub API to gather detailed information on users located in Moscow with over 50 followers, including their profiles and repositories.
- **Interesting Finding**: Developers in Moscow are highly engaged in open-source contributions, with Python and JavaScript leading as the most popular languages.
- **Recommendation**: Developers aiming for higher visibility should focus on popular languages and frequently star-rated projects to increase reach.

---

### Project Overview

This project centers on exploring the GitHub community in Moscow by scraping data on users with significant social reach (over 50 followers). Leveraging GitHub’s API, I collected data on user profiles and their associated repositories, then organized it for analysis to uncover trends and actionable insights for developers.

### Files in This Repository

- `users.csv`: Contains comprehensive profile data for Moscow-based users, including username, bio, email, company, follower/following count, and more.
- `repositories.csv`: Contains up to 500 public repositories for each user, including repository name, creation date, language, stars, watchers, license, and more.
- `github_scraper.py`: Python script for collecting user and repository data via GitHub API.
- `README.md`: This file explaining the project, with a summary of data collection, findings, and recommendations.

### How I Collected the Data

Using Python, I built a script that connects to the GitHub API and retrieves Moscow-based users with over 50 followers. Each user’s profile information is pulled first, including their name, bio, location, followers, and associated metadata. For each user, I also collected information on up to 500 of their most recently pushed repositories, fetching data such as repository name, programming language, star count, license, and other details. The resulting datasets were saved in CSV format for structured analysis.

### Analysis Insights

1. **Popular Languages**: Python and JavaScript are dominant among Moscow-based developers, showing strong engagement in both languages across multiple sectors, from open-source to corporate projects.
2. **Follower Influence**: Users who maintain repositories with high star counts tend to have more followers, indicating a potential link between project popularity and social reach.
3. **Licenses Used**: The most popular licenses are MIT, Apache, and GPL. This indicates a preference for permissive open-source licenses, encouraging both individual and enterprise use of their code.
4. **Active Participation**: Many developers had profiles indicating high engagement in the community. Developers with the most followers typically contributed actively and consistently to popular languages, reflecting a correlation between project quality and engagement.

### Recommendations for Developers

Based on the analysis, I recommend that developers focus on the following:

- **Project Visibility**: Contribute to high-interest languages like Python or JavaScript to increase your profile's visibility and attract a larger follower base.
- **Licensing Choices**: Choosing a permissive license such as MIT can encourage more widespread use and contributions to your project, leading to potential increases in stars and forks.
- **Consistent Contribution**: Users with frequent updates to popular repositories gain more followers. Consistency, combined with projects that offer real-world value, is key to increasing your reach.

### How to Use This Repository

1. **Run the Script**: `github_scraper.py` collects the data from GitHub’s API. Be sure to set up your GitHub token in the script to avoid rate limits.
2. **Analyze the Data**: The CSV files `users.csv` and `repositories.csv` are ready for exploration using any data analysis tools, such as pandas in Python or spreadsheet software.
3. **Explore the Results**: Insights are embedded in the data, which can help answer specific questions about follower growth, language preferences, and repository trends among Moscow’s developers.

### Dependencies

To run the `github_scraper.py` script, you need:

- Python 3.x
- `requests` library (install via `pip install requests`)

### Example API Data Fields

The following fields were retrieved for each user:

- **User Profile**: `login`, `name`, `company`, `location`, `email`, `hireable`, `bio`, `public_repos`, `followers`, `following`, `created_at`
- **Repository Data**: `full_name`, `created_at`, `stargazers_count`, `watchers_count`, `language`, `has_projects`, `has_wiki`, `license_name`

### Key Limitations

This project captures only public data for Moscow-based GitHub users with over 50 followers. Due to API rate limits and restrictions on private data, some information may be incomplete.

### Future Directions

To deepen the analysis, future work could include comparing Moscow developers to those in other cities, exploring patterns in contribution frequency, and analyzing the impact of specific repository topics on user followers.

---

Thank you for checking out this project! For questions or collaborations, feel free to reach out.
