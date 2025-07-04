def prepare_graph(parsed_obj: dict):
    valid_node_ids = {node["id"] for node in parsed_obj["nodes"]}
    nodes_with_edges_set = set()
    edges_adjusted = []
    seen_edge_pairs = set()

    for edge in parsed_obj["edges"]:
        source = edge["source"]
        target = edge["target"]
        if (
            source not in valid_node_ids
            or target not in valid_node_ids
            or edge["number_of_interactions"] == 0
        ):
            continue

        edge_key = tuple(sorted([source, target]))

        if edge_key in seen_edge_pairs:
            continue

        seen_edge_pairs.add(edge_key)
        nodes_with_edges_set.update([edge["source"], edge["target"]])
        edges_adjusted.append(
            {
                "source": edge["source"],
                "target": edge["target"],
                "label": str(edge["number_of_interactions"]),
            }
        )

    nodes_with_edges_dict = {}
    nodes_without_edges_dict = {}

    for node in parsed_obj["nodes"]:
        if node["id"] in nodes_with_edges_set:
            nodes_with_edges_dict[node["id"]] = node
        else:
            nodes_without_edges_dict[node["id"]] = node

    return {
        "nodes_with_edges": list(nodes_with_edges_dict.values()),
        "nodes_without_edges": list(nodes_without_edges_dict.values()),
        "edges": edges_adjusted,
    }
