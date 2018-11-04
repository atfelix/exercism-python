import re

HEADER_REGEX = r'^(#+ )(.*)$'
HEADER_TEMPLATE = '<h%d>%s</h%d>'
STRONG_REGEX = r'__(.*)__'
STRONG_TEMPLATE = r'<strong>\1</strong>'
EM_REGEX = r'_(.*)_'
EM_TEMPLATE = r'<em>\1</em>'
LIST_REGEX = re.compile(r'(<li>.*</li>[\n]?)+', re.MULTILINE)
LIST_TEMPLATE = '<ul>%s</ul>'
LIST_ITEM_TEMPLATE = f'<li>%s</li>'
PARAGRAPH_TEMPLATE = '<p>%s</p>'
LIST_ITEM_PREFIX = '* '

def parse_markdown(markdown):
    lines = [parse(line) for line in markdown.splitlines()]
    return parse_list(''.join(lines))

def parse(line):
    parsed_line = bold_italicized_line(line)
    if re.match(HEADER_REGEX, line):
        return parse_header(parsed_line)
    elif line.startswith(LIST_ITEM_PREFIX):
        return parse_list_item(parsed_line)
    else:
        return parse_paragraph(parsed_line)

def bold_italicized_line(line):
    return parse_em(parse_strong(line))

def parse_strong(line):
    return re.sub(STRONG_REGEX, STRONG_TEMPLATE, line)

def parse_em(line):
    return re.sub(EM_REGEX, EM_TEMPLATE, line)

def parse_header(line):
    return re.sub(HEADER_REGEX, header_replace, line)

def header_replace(match):
    length_of_header = len(match.group(1)) - 1
    return HEADER_TEMPLATE % (length_of_header, match.group(2), length_of_header)

def parse_list_item(line):
    return LIST_ITEM_TEMPLATE % line[2:] if line.startswith(LIST_ITEM_PREFIX) else line

def parse_paragraph(line):
    return PARAGRAPH_TEMPLATE % line

def parse_list(markdown):
    return re.sub(LIST_REGEX, list_item_replace, markdown)

def list_item_replace(match):
    return LIST_TEMPLATE % ''.join(match.groups())