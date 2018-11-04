class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def add(self, child):
        self.children.append(child)


def BuildTree(records):
    records.sort(key=lambda record: record.record_id)
    if not areRecordsValid(records):
        raise ValueError('''Invalid records:  records must satisfy:
        -> parent_id < record_id or parent_id == record_id == 0
        -> lowest record_id == 0
        -> highest record_id == number of record minus 1''')
    trees = list(map(lambda i: Node(i), range(len(records))))
    for record in records[1:]:
        trees[record.parent_id].add(trees[record.record_id])
    return trees[0] if trees else None

def areRecordsValid(records):
    if not records:
        return True
    min_record_id = min(records, key=lambda x: x.record_id).record_id
    max_record_id = max(records, key=lambda x: x.record_id).record_id
    return min_record_id == 0 and max_record_id == len(records) - 1 and all(valid(record) for record in records)


def valid(record):
    return record.parent_id < record.record_id or record.parent_id == record.record_id == 0

