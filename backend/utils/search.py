def search_files(query, file_contents):
    # Placeholder implementation of search logic
    # You should replace this with actual search functionality
    results = []
    for file_name, content in file_contents.items():
        if query.lower() in content.lower():
            results.append(file_name)
    return {"results": results}
