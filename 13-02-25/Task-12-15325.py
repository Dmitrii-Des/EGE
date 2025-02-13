st = '8' * 45
while '1111' in st or '8888' in st:
    st = st.replace('1111', '88')
    st = st.replace('8888', '11')
print(st)