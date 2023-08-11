# packageManager
---- 8< ------------

# Package Manager Simulator

Write a simulator for a package manager.

The package dependences are supplied in a file `repo.db` file such as:

    a: b c d
    d: e f
    f: g

That is `a` requires `b` ,`c`, and `d`.
You can assume that there are no dependencies cycles in the `repo.db`

Your installed packages will be represented as a `pkgs.db`.

    d
    e
    f

Write a `pkg` script such as.

    pkg {install PKG|uninstall PKG|list}

Where:

- `pkg install PKG` will add `PKG` and all it dependencies (transitive included) into the `pkgs.db`
- `pkg uninstall` will remove `PKG` and all it packages that is dependent on it (transitive included) from `pkgs.db`
- `pkg list` will list the current packages in `pgs.db`

# Assignment guidelines

- Solve this question using Python and its standard-libraries.
- Submit your solution as a link to a Git repository (e.g., GitHub, GitLab, BitBucket, SourceHut, etc), or a tar-ball of a local Git repository (include the `.git/` directory).
- Try to commit often.

------ >8 ---