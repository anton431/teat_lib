from git import Repo
# Путь к репозиторию Git

repo_path = 'https://github.com/anton431/teat_lib.git'


# Инициализация объекта репозитория

repo = Repo(repo_path)
assert not repo.bare
# Получение текущего коммита

current_commit = repo.head.commit
# Получение текста коммита

commit_message = current_commit.message
# Вывод текста коммита

print(commit_message)
