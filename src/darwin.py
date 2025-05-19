import subprocess

def apply_pf_rule(port, action="block"):
    # Mac or darwin platform
    cmd = ["pfctl", "-t", "block_ports", "-T", "add", str(port)] if action == "block" else ["pfctl", "-t", "allow_ports", "-T", "add", str(port)]
    subprocess.run(cmd, check=True)
    print(f"{action.capitalize()}ed port {port}")

# Example: Block port 80
apply_pf_rule(80, "block")