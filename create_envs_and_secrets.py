from github import Github
import os

def create_environment(repo, env_name):
    """Create a new environment if it doesn't exist."""
    try:
        # Check if the environment already exists
        existing_envs = [env.name for env in repo.get_environments()]
        if env_name in existing_envs:
            print(f"Environment {env_name} already exists.")
            return True
        
        # If it doesn't exist, create it
        repo.create_environment(env_name)
        print(f"Created new environment: {env_name}")
        return True
    except Exception as e:
        print(f"Error creating environment {env_name}: {str(e)}")
        return False

def create_environment_secret(repo, env_name, secret_name, secret_value):
    """Create a new secret for an environment."""
    try:
        env = repo.get_environment(env_name)
        env.create_secret(secret_name, secret_value)
        return True
    except Exception as e:
        print(f"Error creating secret {secret_name} for environment {env_name}: {str(e)}")
        return False

def create_envs_and_secrets(repo):
    # Create 10 environments
    for i in range(12, 20):
        env_name = f"FOO_ENV_{i}"
        if create_environment(repo, env_name):
            print(f"Created environment: {env_name}")
            # Create 10 secrets for each environment
            for j in range(1, 11):
                secret_name = f"FOO_SECRET_{j}"
                secret_value = f"Value for {secret_name} in {env_name}"
                if create_environment_secret(repo, env_name, secret_name, secret_value):
                    print(f"Created secret: {secret_name} in environment: {env_name}")
        print()  # Add a newline for better readability


def main():
    # Get GitHub token from environment variable
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")
    
    # Create a Github instance
    g = Github(github_token)
    
    # Get repository details
    repo_owner = "CONCETO"
    repo_name = "environment-secret-sandbox"
    
    # Get the repository
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    # create_envs_and_secrets(repo)
    env_name = f"FOO_ENV_20"
    if create_environment(repo, env_name):
        print(f"Created environment: {env_name}")
        for i in range(111, 1001):
            secret_name = f"FOO_SECRET_{i}"
            secret_value = f"Value for {secret_name} in {env_name}"
            if create_environment_secret(repo, env_name, secret_name, secret_value):
                print(f"Created secret: {secret_name} in environment: {env_name}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")