import sys

class fileManager():
    def __init__(self, repo_path="repo.db", pkg_path="pkgs.db"):
        self.repo_path = repo_path
        self.pkg_path = pkg_path
        self.pkg_list = self.getPkgs()
        self.repo_graph = self.getRepoGraph()
    def updatepkgs(self, pkg_list):
        # Update pkgs.db with the given list of package names
        # pkg_list is a list of package names
        with open(self.pkg_path, 'w') as f:
            for pkg in sorted(pkg_list):
                f.write(pkg + '\n')
        self.pkg_list = pkg_list
    def getPkgs(self):
        # Return a list of package names in pkgs.db
        with open(self.pkg_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    def getRepoGraph(self):
        # Return a dictionary of dependencies
        # The key is the package name
        # The value is a list of dependencies
        repo_graph = {}
        with open(self.repo_path, 'r') as file:
          for line in file:
            package, deps = line.strip().split(':')
            repo_graph[package] = deps.strip().split()
        return repo_graph
    def getDependents(self,pkg_name):
        # Return a set of dependents
        graph = self.repo_graph
        dependents = set()
        for package in graph:
            if pkg_name in graph[package]:
                if package in self.pkg_list and package not in dependents:
                  dependents.add(package)
                  dependents.update(self.getDependents(package))
        return dependents
    def getDependencies(self,pkg_name):
        # Return a set of dependencies
        graph = self.repo_graph
        dependencies = set()
        if pkg_name in graph:
            dependencies.update(graph[pkg_name])
            for dep in graph[pkg_name]:
                if dep not in self.pkg_list:
                  dependencies.update(self.getDependencies(dep))
        return dependencies
    
    def install(self,pkg_name):
        # Install the given package and dependencies
        dependecies = self.getDependencies(pkg_name)
        dependecies.update([pkg_name])
        dependecies.update(self.pkg_list)
        self.pkg_list= list(dependecies)
        self.updatepkgs(self.pkg_list)

    def uninstall(self,pkg_name):
        # Uninstall the given package and dependents
        dependents = self.getDependents(pkg_name)
        self.pkg_list.remove(pkg_name)
        for dep in dependents:
            self.pkg_list.remove(dep)
        self.updatepkgs(self.pkg_list)

def list_packages(pkgs_path="pkgs.db"):
    # List all installed packages
    with open(pkgs_path, 'r') as f:
        for line in f:
            print(line.strip())
    

if __name__ == "__main__":
    command = sys.argv[1]
    if command not in ["install", "uninstall", "list"]:
        print("Invalid command")
        sys.exit(1)
    if command == "install":
        fm = fileManager()
        pkg_name = sys.argv[2]
        fm.install(pkg_name)
    if command == "uninstall":
        fm = fileManager()
        pkg_name = sys.argv[2]
        if pkg_name not in fm.pkg_list:
            print("Package not installed")
            sys.exit(1)
        fm.uninstall(pkg_name)
    if command == "list":
        list_packages()