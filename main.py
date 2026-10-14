
# 포켓몬 설명 카드
reason_html = reason.replace("\n", "<br>")

st.markdown(
    f"""
<div class="card">
<div class="poke-name">{name_ko}</div>
<div class="english">{name_en}</div>
<div class="type-pill">✨ 타입 · {poke_type}</div>
<div class="attribute">
<b>🌟 포켓몬 특징</b><br>
{traits}
</div>
<div class="explain">
<b>💬 나와 어울리는 이유</b><br><br>
{reason_html}
</div>
</div>
""",
    unsafe_allow_html=True
)
