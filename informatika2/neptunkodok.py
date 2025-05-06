neptun_kodok=[
'HMZFKK',
'KJMRMX',
'GTN2JN',
'P15PSN',
'DA88FL',
'DQM8AD',
'CHLAQG',
'X2A2VX',
'GGBL4Q',
'F9JP54',
'QKSIIC',
'MH7L6P',
'ORAE0N',
'F6YZGR',
'MRB6NR',
'BN5IZP',
'U5VOSX',
'DAOWYS',
'CQQTXR',
'ADXHZQ',
'H9FC40',
'EOQX6F',
'DRNNV3',
'WLOKLJ'
]

import os

# Fájlok létrehozása nagybetűs nevekkel
for neptun_kod in neptun_kodok:
    # Fájlnév nagybetűsítése és biztonságos formázása
    safe_name = "".join(c for c in neptun_kod.upper() if c.isalnum() or c in ('_', '-')).rstrip()
    filename = f"{safe_name}.html"
    
    # Fájl létrehozása, ha nem létezik
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            pass  # Üres fájl
        print(f"Fájl létrehozva: {filename}")
    else:
        print(f"A fájl már létezik: {filename}")
