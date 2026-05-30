#!/usr/bin/env python3
# ror13_hash.py — Compute ROR13 hash for Windows API function names

def ror32(val, count):
    count &= 31
    return ((val >> count) | (val << (32 - count))) & 0xFFFFFFFF

def ror13(name):
    h = 0
    for c in name:
        h = ror32(h, 13)
        h = (h + ord(c)) & 0xFFFFFFFF
    return h

# Known function hashes (verify these match the table in the course):
functions = [
    "LoadLibraryA",
    "GetProcAddress",
    "WinExec",
    "ExitProcess",
    "CreateProcessA",
    "VirtualAlloc",
    "VirtualProtect",
    "CreateThread",
    "WriteProcessMemory",
    "OpenProcess",
]

print(f"{'Function':<25} {'Hash':>12}")
print("-" * 40)
for fn in functions:
    print(f"{fn:<25} 0x{ror13(fn):08X}")

# Usage: python3 ror13_hash.py
# Expected output:
# Function                       Hash
# ----------------------------------------
# LoadLibraryA              0xEC0E4E8E
# GetProcAddress            0x7C0DFCAA
# WinExec                   0x0E8AFE98
# ExitProcess               0x73E2D87E
# ...
