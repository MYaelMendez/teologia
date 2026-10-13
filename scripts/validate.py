#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required={"locale","title","subtitle","source","handbook","start","notice"}
files={"en":"en.json","es":"es.json","pt-BR":"pt-BR.json"}
for locale,name in files.items():
    data=json.loads((root/"i18n"/name).read_text(encoding="utf-8"))
    assert data["locale"]==locale,(name,"wrong locale")
    assert set(data)==required,(name,"missing or extra keys",set(data)^required)
    assert all(isinstance(v,str) and v.strip() for v in data.values()),name
print("OK: locale contracts validated")
