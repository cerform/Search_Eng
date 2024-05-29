import nbformat

def process_ipynb(file):
    notebook = nbformat.read(file, as_version=4)
    cells = notebook.cells
    return cells
