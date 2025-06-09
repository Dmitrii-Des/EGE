st = '1' * 81
while '11111' in st or '888' in st:
    if '11111' in st:
        st = st.replace('11111', '88', 1)
    else:
        st = st.replace('888', '8', 1)
print(st)