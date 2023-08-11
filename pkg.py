import sys

class fileManager():
    def __init__(self, repo_path="repo.db", pkg_path="pkgs.db"):
        self.repo_path = repo_path
        self.pkg_path = pkg_path
    def updateRepo(self, pkg_list):
        # Update the repo with the given list of packages
        # pkg_list is a list of package names
        with open(self.pkg_path, 'w') as f:
            for pkg in pkg_list:
                f.write(pkg.name + '\n')
    def getRepo(self):
        # Return a list of package names
        with open(self.pkg_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    def getRepoGraph(self):
        # Return a dictionary of dependencies
        # The key is the package name
        # The value is a list of dependencies
        dependencies = {}
        with open(self.repo_path, 'r') as file:
            for line in file:
                package, deps = line.strip().split(':')
                dependencies[package] = deps.strip().split()
        return dependencies

def getDependencies(pkg, fm):
    RepoGraph = fm.getRepoGraph()

def install(pkg_name):
    # Install the given package and dependencies
    pass
def uninstall(pkg_name):
    # Uninstall the given package and dependents
    pass
def list_packages():
    # List all installed packages
    pass

if __name__ == "__main__":
    command = sys.argv[1]
    if command not in ["install", "uninstall", "list"]:
        print("Invalid command")
        sys.exit(1)
    if command == "install":
        pkg_name = sys.argv[2]
        install(pkg_name)
    if command == "uninstall":
        pkg_name = sys.argv[2]
        uninstall(pkg_name)
    if command == "list":
        list_packages()