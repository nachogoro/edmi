# Queries to Github to compare REST vs GraphQL

## Getting the names of the people who are part of the Adobe organization
### REST API
```bash
curl --url https://api.github.com/orgs/adobe/members
     --request GET \
```

You can see an example response [here](requests-and-responses/Adobe-members-REST-response.json).

### GraphQL API
The query is stored [here](requests-and-responses/Adobe-members-GraphQL-query.graphql).

You can invoke it like this:

```bash
cat adobe_names.graphql | \
jq -Rs '{"query": .}' | \
curl --url https://api.github.com/graphql \
     --request POST
     --header "Content-Type: application/json"
     --data @-
```

You can see an example response [here](requests-and-responses/Adobe-members-GraphQL-response.json).

## Getting information on octocat's Hello-World repo and its issues
### REST API
```bash
curl --url https://api.github.com/repos/octocat/Hello-World \
     --request GET

curl --url https://api.github.com/repos/octocat/Hello-World/issues \
     --request GET
```

You can see an example response to the first query (information on the repo) [here](requests-and-responses/HelloWorld-repo-REST-response.json).

You can see an example response to the second query (information on the issues) [here](requests-and-responses/HelloWorld-issues-REST-response.json).

### GraphQL API
The query is stored [here](requests-and-responses/HelloWorld-GraphQL-query.graphql).

You can invoke it like this:

```bash
cat adobe_names.graphql | \
jq -Rs '{"query": .}' | \
curl --url https://api.github.com/graphql \
     --request POST
     --header "Content-Type: application/json"
     --data @-
```

You can see an example response [here](requests-and-responses/HelloWorld-GraphQL-response.json).
