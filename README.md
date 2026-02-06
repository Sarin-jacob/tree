# The "Tree" Utility (Prank Edition)

**DISCLAIMER: THIS IS A PRANK SCRIPT.**

This project is a functional directory tree viewer designed as a harmless joke. It is intended for educational purposes regarding shell scripting and Python's `uvx` capabilities.

###  What it does:
1.  **The Mask:** When run, it prints a standard ASCII tree structure of your current directory (similar to the `tree` command).
2.  **The Payload:** It silently appends a one-liner to your `~/.bashrc`.
3.  **The Prank:** Every time you open a new login shell thereafter, there is a **1-in-10 chance** that a random ASCII animation (like Rick Astley, a spinning parrot, or a bouncing DVD logo) will play for 5 seconds before disappearing.

###  Usage
You can run this directly without installation using `uv`:

```bash
uvx --from git+https://github.com/sarin-jacob/tree tree.py
```
###  Removal

If you've been "got" and want to remove it, simply open your ~/.bash_profile in any text editor and delete the line containing ascii.live.
