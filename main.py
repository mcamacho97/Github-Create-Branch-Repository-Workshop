from github import Github

def create_branch(branch_name):
    """
    Function that creates a new branch for a repository in Github.

    Parameters:
    branch_name (str): Name of the branch to be created.

    Returns:
    A string value indicating the creation of the new branch.

    """
    repository_name = input("Digite el nombre de su repositorio: ")
    access_token = Github(input("Digite el access token de su cuenta github: "))
    try:
        for repo in access_token.get_user().get_repos():
            if repo.name == repository_name:
                new_branch = repo.create_git_ref(ref=f'refs/heads/{branch_name}', 
                                             sha=repo.get_branch("main").commit.sha)
                print(f'Branch: {branch_name} creada en el repositorio {repository_name}')
    except Exception as error_str:
        print(
                f"Error al crear la rama en el repositorio, porfavor verifica que el nombre del "
                f"repositorio exista en tu cuenta github o el access token esté digitado correctamente: \n{error_str}")

input_branch_name = input("Digite el nombre de la rama que desea crear: ")

def main():
    """
    Main function that calls `create_branch` function.

    Parameters:
    input_branch_name (str): Name of the branch to be created.

    Returns:
    None
    """
    create_branch(input_branch_name)

if __name__ == "__main__":
    main()
