import streamlit as st

st.title('🧪 용액의 성질 계산기')

water_feature = ['산성', '중성', '염기성']

base = st.number_input('(1) 염기성 용액 양(ml):', min_value=0.0, value=0.0, step=1.0)
acid = st.number_input('(2) 산성 용액 양(ml):', min_value=0.0, value=0.0, step=1.0)

def water_calculation(base_vol, acid_vol):
    temp_base = base_vol
    temp_acid = acid_vol
    
    while temp_base > 0 and temp_acid > 0:
        if temp_base >= 1 and temp_acid >= 1:
            temp_base -= 1
            temp_acid -= 1
        else:
            min_val = min(temp_base, temp_acid)
            temp_base -= min_val
            temp_acid -= min_val
            break

    if temp_acid > 0:
        result = water_feature[0]
    elif temp_base == 0 and temp_acid == 0:
        result = water_feature[1]
    else:
        result = water_feature[2]

    total_volume = base_vol + acid_vol

    st.divider()
    st.success(f'용액의 성질: **{result}**')
    st.info(f'총 부피: **{total_volume}ml**')

if st.button('계산하기'):
    if base <= 0 or acid <= 0:
        st.warning('⚠️ 두 용액의 양 모두 0보다 큰 양수로 다시 입력해 주세요.')
    else:
        water_calculation(base, acid)
