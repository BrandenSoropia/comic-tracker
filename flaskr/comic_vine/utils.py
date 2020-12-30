def build_filter_string(filters: dict[str, str]):
    accumulated = ''

    for key in filters:
        accumulated += f"{key}:{filters[key]}"

    return accumulated
