st = '8' * 9  + '5' * 12
while '555' in st or '888' in st:
    st = st.replace('555', '8')
    st = st.replace('888', '5')

print(st)
