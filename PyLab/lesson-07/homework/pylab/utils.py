def load_game_configs_from_json(json_path: str) -> list[dict]:
    # Implement me.
    data = ...
    return data["config"]


def convert_keys(d):
    if not isinstance(d, dict):
        return d
    return {k.replace("-", "_"): convert_keys(v) for k, v in d.items()}
