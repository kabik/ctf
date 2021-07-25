src = 'EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT'

for c in src:
    if c.islower():
        new_c = chr( ord('a') + (ord(c)-ord('a')+13)%26 )
    elif c.isupper():
        new_c = chr( ord('A') + (ord(c)-ord('A')+13)%26 )
    else:
        new_c = c
    print(new_c, end='')
print()
