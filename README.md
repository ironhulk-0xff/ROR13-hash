**ror13_hash**:
A tiny Python script that computes ROR13 hashes for Windows API function names. Use this when writing position-independent shellcode that needs to resolve API calls dynamically without leaving suspicious strings in the binary.

**What it does:**
Feed it a list of Windows API function names, and it gives you their ROR13 hashes; then embed those hashes in your shellcode instead of the raw strings. At runtime, your shellcode walks the PEB to find loaded modules, parses their export tables, hashes each function name, and compares it against the pre-computed values.

**Why bother?**

- No strings attached: Your shellcode never contains strings like "LoadLibraryA" or "CreateProcessA". Static analysis and signature-based detection have nothing obvious to latch onto.
- Smaller payload: A 4-byte hash takes up way less space than a full function name, which matters when you're squeezing shellcode into tight buffers.
- It just works: ROR13 is fast, trivial to implement in assembly, and collision rates are low enough within a single DLL's export table that you won't run into trouble.

Edit the functions list in the script to include whatever API calls your shellcode needs, then copy the output hashes into your assembly or C payload. **You need to add the resolve code**

**Heads up:**
ROR13 is not cryptographically secure — it's trivially reversible and full of collisions. Don't use it for anything that needs real secrecy. Its job is obfuscation, not encryption.
