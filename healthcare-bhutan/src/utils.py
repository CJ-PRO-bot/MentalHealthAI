from pathlib import Path     #to access files

PROJECT_ROOT = Path(__file__).resolve().parents[1]   #PROJECT_ROOT points to the root folder healthcare-bhutan([1]- 1step up util.py being child[0])

def get_data_path(kind: str = "raw") -> Path:  #in this function, we accept parameter str, if not default raw. Path/data/raw where orginal file is
    if kind == "raw":
        return PROJECT_ROOT / "data" / "raw"
    elif kind == "processed":
        return PROJECT_ROOT / "data" / "processed"
    else:
        raise ValueError("kind must be 'raw' or 'processed'")
