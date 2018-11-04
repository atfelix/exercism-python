def transform(legacy_data):
    return {element.lower(): k for k in legacy_data for element in legacy_data[k]}