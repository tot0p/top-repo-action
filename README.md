# top-repo-action

This is a simple GitHub Action that will list the top repositories of a user or organization.

## Exemple of usage

```yaml
name: List top repositories

on:
  push:
    branches:
      - master

jobs:
    list-top-repos:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout
        uses: actions/checkout@v2
        - name: List top repositories
        uses: tot0p/top-repo-action@v1
        with:
            username: tot0p
            include_org_repos: true # Optional (default: false)
            commit_message : "Update README.md" # Optional (default: "Update README.md with top repositories")
            name_of_balise : "Top-Repositories" # Optional (default: "Top-Repositories")
            top : 3 # Optional (default: 3)


```

## Result

<!--Top-Repositories-->
| Top | Repo                                                                                                                                                                                    |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | <a href="https://github.com/Eclalang/Ecla"><img src="https://denvercoder1-github-readme-stats.vercel.app/api/pin/?username=Eclalang&repo=Ecla&theme=dark" width="480px"/></a>           |
| 2   | <a href="https://github.com/tot0p/Hello-World"><img src="https://denvercoder1-github-readme-stats.vercel.app/api/pin/?username=tot0p&repo=Hello-World&theme=dark" width="480px"/></a>   |
| 3   | <a href="https://github.com/Eclalang/LearnEcla"><img src="https://denvercoder1-github-readme-stats.vercel.app/api/pin/?username=Eclalang&repo=LearnEcla&theme=dark" width="480px"/></a> |

<!--/Top-Repositories-->