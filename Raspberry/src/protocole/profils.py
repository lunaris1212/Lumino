import xml.etree.ElementTree as ET


def parse_protocol(xml_path="profils.xml"):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    types = {}
    for type_tag in root.find("types"):
        type_id = int(type_tag.attrib["id"], 16)
        type_name = type_tag.attrib.get("name", "")
        ids = {}
        for id_tag in type_tag.findall("id"):
            id_id = int(id_tag.attrib["id"], 16)
            id_name = id_tag.attrib.get("name", "")
            fields = []
            for field in id_tag.findall(".//field"):
                fields.append({
                    "name": field.attrib.get("name"),
                    "index": int(field.attrib.get("index", 0)),
                    "unit": field.findtext("unit"),
                    "value": field.findtext("value")
                })
            ids[id_id] = {"name": id_name, "fields": fields}
        types[type_id] = {"name": type_name, "ids": ids}
    return types


def compute_checksum(payload):
    return sum(payload) & 0xFF


def verify_frame(hex_string, protocol):
    try:
        frame = bytes.fromhex(hex_string) if type(hex_string) == str else hex_string
        if frame[0] != 0xAA or frame[-1] != 0x55:
            return False, "Start or end byte incorrect"
        length = frame[1]
        expected_len = len(frame) - 4  # exclude AA, checksum, 55, and length itself
        if length != expected_len:
            return False, f"Length mismatch (expected {length}, got {expected_len})"
        type_id = frame[2]
        id_id = frame[3]
        data = frame[4:-2]
        checksum = frame[-2]
        calc_checksum = compute_checksum(frame[1:-2])
        if checksum != calc_checksum:
            return False, f"Checksum mismatch (expected {calc_checksum:#02x}, got {checksum:#02x})"
        if type_id not in protocol:
            return False, f"Unknown type: {type_id:#02x}"
        if id_id not in protocol[type_id]["ids"]:
            return False, f"Unknown ID {id_id:#02x} for type {type_id:#02x}"
        return True, f"Valid frame (type={protocol[type_id]['name']}, id={protocol[type_id]['ids'][id_id]['name']})"
    except Exception as e:
        return False, f"Error parsing frame: {e}"

# =======================
# EXEMPLE D'UTILISATION
# =======================
if __name__ == "__main__":
    pass
