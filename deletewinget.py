import nbformat

path = "NLP final.ipynb"  # đổi tên file tại đây

with open(path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb.metadata:
    print("Found metadata.widgets — removing...")
    del nb.metadata["widgets"]

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("✔ Notebook đã được sửa.")