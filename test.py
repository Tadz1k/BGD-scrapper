# main.py

for filename in ["file1.txt", "file2.txt"]:
    with open(filename) as f:
        contents = f.read()

    lines = contents.splitlines()

    for line in lines:
        if not line or line.startswith("# ") or line.startswith("// "):
            continue

        for word in line.split():
            print(f"[{word}]", end="")

        print("")