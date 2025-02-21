import json


with open("sample-data.json") as file:
    data = json.load(file)

interfaces = data.get("imdata", [])

print("Interface Status")
print("=" * 50)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 90)

for interface in interfaces:
    attributes = interface.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "N/A")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
