unicode_text = (
    "079099032758|025778737|Nguy\u00E1\u00BB\u2026n Ng\u00E1\u00BB\u008Dc Ngh\u00C4\u0083\u00A9a|"
    "09041999|Nam|29 L\u0103\u0323 36 Ph\u00E1\u00BA\u00A1m Th\u00E1\u00BA\u00BF Hi\u00E1\u00BB\u0083n, Ph\u00C6\u00B0\u00E1\u00BB\u009Dng 4, Qu\u00E1\u00BA\u00ADn 8, TP.H\u00E1\u00BB\u0093 Ch\u00C4\u009B Minh|10052021"
)

decoded_text = bytes(unicode_text, "utf-8").decode("unicode_escape")
print(decoded_text)
print(1)
