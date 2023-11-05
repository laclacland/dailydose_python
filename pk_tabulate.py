from tabulate import tabulate
from colorama import Style

data = [
    ["NumPy", "Numerical computing and array operations"],
    ["Pandas", "Data manipulation and analysis"],
    ["Matplotlib", "Data visualization"],
    ["TensorFlow", "Machine learning and deep learning"],
    ["PyTorch", "Deep learning framework"],
    ["Scikit-Learn", "Machine learning algorithms and tools"],
    ["Django", "Web application development framework"],
    ["Flask", "Lightweight web framework for microservices"],
    ["SQLAlchemy", "SQL toolkit and Object-Relational Mapping (ORM)"],
    ["Requests", "HTTP library for making web requests"]
]

table = tabulate(
    data,
    headers=["Package", "Primary Purpose"],
    tablefmt="fancy_grid")

title = f"{Style.BRIGHT} ~ Popular Python Packages ~ {Style.RESET_ALL}"

print(title)
print(table)
