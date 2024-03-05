import requests
from tabulate import tabulate

def get_shards_info(qdrant_url):
    try:
        response = requests.get(f"{qdrant_url}")
        response.raise_for_status()
        shards = response.json()
        return shards
    except requests.RequestException as e:
        print(f"Error fetching shards info: {e}")
        return None

def display_shards_info(shards_info):
    if shards_info:
        table = [["Shard ID", "Nodes"]]
        for shard_id, nodes in shards_info.items():
            if isinstance(nodes, (list, tuple)):  # Check if nodes is iterable
                table.append([shard_id, ", ".join(nodes)])
            else:
                table.append([shard_id, str(nodes)])  # Handle non-iterable nodes
        print(tabulate(table, tablefmt="grid"))

def main():
    qdrant_url = input("Enter the URL of the Qdrant instance: ")
    shards_info = get_shards_info(qdrant_url)
    display_shards_info(shards_info)

if __name__ == "__main__":
    main()
