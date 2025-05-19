import argparse
import json

def load_rules():
    try:
        with open("rules.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_rules(rules):
    with open("rules.json", "w") as f:
        json.dump(rules, f, indent=2)

parser = argparse.ArgumentParser(description="Firewall Manager")
parser.add_argument("--add-rule", help="Add rule (e.g., 'block tcp 80')")
parser.add_argument("--list-rules", action="store_true", help="List all rules")
args = parser.parse_args()

rules = load_rules()

if args.add_rule:
    action, protocol, port = args.add_rule.split()
    rules.append({"action": action, "protocol": protocol, "dst_port": int(port)})
    save_rules(rules)
    print(f"Added rule: {action} {protocol} {port}")

if args.list_rules:
    for rule in rules:
        print(f"{rule['action']} {rule['protocol']} {rule['dst_port']}")