# top-repo-action

This is a simple GitHub Action that will list the top repositories of a user or organization.

## Inputs

### `username`

**Required** The username of your GitHub account.

### `include_org_repos`

**Optional** If you want to include the repositories of the organizations you are part of. Default `false`.

### `commit_message`

**Optional** The commit message. Default `"Update README.md with top repositories"`.

### `name_of_balise`

**Optional** The name of the balise. Default `"Top-Repositories"`.

### `top`

**Optional** The number of top repositories to list. Default `3`.

## Outputs

No outputs. The action will update the README.md file of the repository.

## Configuration

You need to have a `README.md` file in the root of your repository.

And you need to have the following balise in your `README.md` file:

```markdown
<!--Top-Repositories-->
<!--/Top-Repositories-->
```

> The name of the balise can be changed with the `name_of_balise` input. Default is `"Top-Repositories"`.

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

<!--/Top-Repositories-->