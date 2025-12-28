import sys
import re
import zlib
import base64
import binascii
import argparse

def try_zlib(data):
    try:
        raw = data if isinstance(data, bytes) else data.encode('utf-8')
        return zlib.decompress(raw)
    except:
        return None

def try_base64(data):
    try:
        if isinstance(data, str) and len(data) > 16:
            if re.match(r'^[A-Za-z0-9+/= \n\r]+$', data):
                return base64.b64decode(data, validate=True)
    except:
        return None

def try_hex(data):
    try:
        if isinstance(data, str):
            clean_hex = data.replace('\\x', '')
            if re.match(r'^[0-9a-fA-F]+$', clean_hex):
                return binascii.unhexlify(clean_hex)
    except:
        return None

def get_payload(data):
    # Try Zlib
    result = try_zlib(data)
    if result: return get_payload(result)

    # Try Base64
    result = try_base64(data)
    if result:
        try:
            return get_payload(result.decode('utf-8'))
        except:
            return get_payload(result)

    # Try Hex
    result = try_hex(data)
    if result: return get_payload(result)

    return data

def save_file(text, path, method):
    if not isinstance(text, str):
        text = text.decode('utf-8', errors='ignore')

    with open(path, 'w', encoding='utf-8') as f:
        if method == "clean":
            f.write(text)
        else:
            b64 = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            code = f'code="""import base64, subprocess; payload="{b64}"; decoded=base64.b64decode(payload).decode("utf-8"); exec(decoded)"""; exec(code)'
            f.write(code)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-m", "--method", choices=["clean", "evasion"], default="clean")
    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = re.findall(r"['\"]([^'\"]{20,})['\"]", content)
        if matches:
            blob = max(matches, key=len)
            clean_code = get_payload(blob)
            save_file(clean_code, args.output, args.method)
    except:
        pass

run()
