from pathlib import Path
import json


def get_cmds_doc():
    doc_file = Path(__file__).resolve().parent / 'doc.json'
    with open(doc_file, 'r', encoding='utf-8') as file:
        doc = json.load(file)
    return doc


def get_cmds_list():
    names = [cmd['name'] for cmd in get_cmds_doc()]
    return names


def set_cmd_doc(info):
    doc_file = Path(__file__).resolve().parent / 'doc.json'
    cmd_list = get_cmds_doc()
    cmd_list.append(info)

    with open(doc_file, 'w', encoding='utf-8') as file:
        json.dump(cmd_list, file, indent=2, ensure_ascii=False)


def remove_cmd_doc(name):
    doc_file = Path(__file__).resolve().parent / 'doc.json'
    cmd_list = get_cmds_doc()
    cmd_list = [cmd for cmd in cmd_list if cmd['name'] != name]

    with open(doc_file, 'w', encoding='utf-8') as file:
        json.dump(cmd_list, file, indent=2, ensure_ascii=False)
