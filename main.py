import arxiv

client = arxiv.Client()

search = arxiv.Search(
    query="large language models",
    max_results=10,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

# Returns a list of `arxiv.Result` objects
results = client.results(search)

for r in client.results(search):
    print(r.title)
