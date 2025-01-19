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
            include_org_repos: true

```

## Result

<!--Top-Repositories-->
<!--/Top-Repositories-->