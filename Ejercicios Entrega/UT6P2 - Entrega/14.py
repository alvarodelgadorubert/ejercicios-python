from pathlib import Path

txt_files = list(Path("logs").glob("*.txt"))
print(f"Total de ficheros .txt en logs/: {len(txt_files)}")