import requests
import os


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories?",params={"q": name})
        body = r.json()

        return body
    
    def visibility_email(self, email):
        token = os.getenv('GITHUB_TOKEN')
        headers = {'Authorization': f'token {token}'}
        r = requests.get("https://api.github.com/user/emails",headers=headers,params={"email": email})
        body = r.json()

        return body
    
    def compare_commits(self, owner, repo, base, head):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/compare/{base}...{head}")
        body = r.json()

        return body
    
    def privately_report_security_vulnerabilities(self, owner, repo):
        token = os.getenv('GITHUB_TOKEN')
        headers = {'Authorization': f'token {token}'}
        r = requests.post(f"https://api.github.com/repos/{owner}/{repo}/vulnerability-alerts",headers=headers)
        body = r.json()

        return body
