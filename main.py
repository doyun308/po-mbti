
import html
import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="💠",
    layout="centered"
)

# 16가지 MBTI별 포켓몬 정보
POKEMON = {
    "INTJ": (
        "뮤츠", "Mewtwo", 150, "에스퍼",
        "분석력 · 독립심 · 집중력",
        "복잡한 문제도 차분하게 분석하는 모습이 닮았어요.\n"
        "자신만의 기준과 계획을 소중하게 생각해요.\n"
        "목표를 향해 끈기 있게 나아갈 단짝이에요."
    ),
    "INTP": (
        "메타몽", "Ditto", 132, "노말",
        "변신 · 유연함 · 가능성",
        "여러 가능성을 자유롭게 탐색하는 모습이 닮았어요.\n"
        "정해진 답보다는 새로운 생각을 즐겨요.\n"
        "기발한 발상을 함께 펼칠 단짝이에요."
    ),
    "ENTJ": (
        "리자몽", "Charizard", 6, "불꽃 / 비행",
        "자신감 · 도전 · 추진력",
        "목표를 향해 자신 있게 도전하는 모습이 닮았어요.\n"
        "어려움 앞에서도 쉽게 물러서지 않아요.\n"
        "더 높은 곳을 향해 함께 나아갈 단짝이에요."
    ),
    "ENTP": (
        "팬텀", "Gengar", 94, "고스트 / 독",
        "장난기 · 재치 · 대담함",
        "기발한 아이디어로 주변을 놀라게 해요.\n"
        "익숙한 방식보다 새로운 시도를 즐겨요.\n"
        "예측 불가능한 모험을 함께할 단짝이에요."
    ),
    "INFJ": (
        "가디안", "Gardevoir", 282, "에스퍼 / 페어리",
        "공감 · 보호 · 신념",
        "상대방의 마음을 깊이 헤아리는 모습이 닮았어요.\n"
        "소중한 존재를 조용하지만 강하게 지켜요.\n"
        "서로의 신념을 존중해 줄 단짝이에요."
    ),
    "INFP": (
        "이브이", "Eevee", 133, "노말",
        "가능성 · 개성 · 성장",
        "자신만의 꿈과 가능성을 소중히 여겨요.\n"
        "다양한 모습으로 성장할 수 있는 잠재력이 있어요.\n"
        "있는 그대로의 모습을 응원해 줄 단짝이에요."
    ),
    "ENFJ": (
        "님피아", "Sylveon", 700, "페어리",
        "교감 · 친절 · 배려",
        "친구에게 따뜻한 에너지를 전하는 모습이 닮았어요.\n"
        "서로의 감정을 알아차리고 다정하게 반응해요.\n"
        "함께 성장하며 응원할 단짝이에요."
    ),
    "ENFP": (
        "피카츄", "Pikachu", 25, "전기",
        "활발함 · 호기심 · 우정",
        "새로운 친구와 모험을 즐기는 모습이 닮았어요.\n"
        "밝은 에너지로 주변 분위기를 바꿔요.\n"
        "매일 즐거운 추억을 쌓을 단짝이에요."
    ),
    "ISTJ": (
        "거북왕", "Blastoise", 9, "물",
        "책임감 · 든든함 · 끈기",
        "주어진 일을 꾸준히 해내는 모습이 닮았어요.\n"
        "신중하게 준비하고 안정적으로 행동해요.\n"
        "언제나 믿고 의지할 수 있는 단짝이에요."
    ),
    "ISFJ": (
        "럭키", "Chansey", 113, "노말",
        "친절 · 치유 · 세심함",
        "어려움에 처한 친구를 세심하게 챙겨요.\n"
        "작은 도움도 기꺼이 건네는 마음이 닮았어요.\n"
        "편안함을 나눌 수 있는 단짝이에요."
    ),
    "ESTJ": (
        "괴력몬", "Machamp", 68, "격투",
        "실행력 · 성실함 · 자신감",
        "해야 할 일에 적극적으로 뛰어드는 모습이 닮았어요.\n"
        "꾸준한 노력으로 목표를 이루려고 해요.\n"
        "든든하게 함께 일할 단짝이에요."
    ),
    "ESFJ": (
        "푸린", "Jigglypuff", 39, "노말 / 페어리",
        "친근함 · 표현력 · 노래",
        "친구들과 즐거움을 나누는 모습이 닮았어요.\n"
        "자신의 감정을 솔직하게 표현해요.\n"
        "주변에 웃음을 선사할 단짝이에요."
    ),
    "ISTP": (
        "루카리오", "Lucario", 448, "격투 / 강철",
        "관찰력 · 침착함 · 민첩함",
        "상황을 빠르게 파악하고 침착하게 행동해요.\n"
        "긴 설명보다 실력으로 보여 주는 편이에요.\n"
        "어려운 순간에 힘이 되어 줄 단짝이에요."
    ),
    "ISFP": (
        "나인테일", "Ninetales", 38, "불꽃",
        "개성 · 우아함 · 신비로움",
        "조용하지만 특별한 개성을 가지고 있어요.\n"
        "자신만의 분위기와 취향을 중요하게 생각해요.\n"
        "편안한 시간을 함께할 단짝이에요."
    ),
    "ESTP": (
        "에이스번", "Cinderace", 815, "불꽃",
        "열정 · 순발력 · 도전",
        "새로운 도전에 빠르게 뛰어드는 모습이 닮았어요.\n"
        "상황에 맞춰 재치 있게 행동해요.\n"
        "신나는 활동을 함께할 단짝이에요."
    ),
    "ESFP": (
        "파치리스", "Pachirisu", 417, "전기",
        "발랄함 · 에너지 · 장난기",
        "밝은 에너지로 주변을 즐겁게 해요.\n"
        "친구들과 어울리는 시간을 좋아해요.\n"
        "매일의 소소한 재미를 찾아 줄 단짝이에요."
    ),
}

GROUPS = {
    "🧠 분석가형": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "🌷 외교관형": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "🛡️ 관리자형": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "🎨 탐험가형": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

# 하늘색 디자인
st.markdown("""
<style>
.stApp {
    background:
      radial-gradient(circle at 8% 5%,
        #d6f5ff 0, transparent 38%),
      linear-gradient(145deg,
        #eefaff 0%, #dceffc 60%, #f7fcff 100%);
    color: #193852;
}

.block-container {
    max-width: 880px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3, p {
    font-family: 'Malgun Gothic',
                 'Apple SD Gothic Neo', sans-serif;
}

h1 {
    color: #13537d !important;
    text-align: center;
    font-size: clamp(2rem, 5vw, 3.1rem) !important;
}

.kicker {
    text-align: center;
    color: #3281ab;
    font-weight: 800;
    letter-spacing: .15em;
    margin: 7px 0 12px;
    font-size: .84rem;
}

.subtitle {
    text-align: center;
    color: #54778e;
    font-size: 1.05rem;
    line-height: 1.85;
    margin-bottom: 30px;
}

.group {
    font-weight: 800;
    color: #2e698d;
    font-size: 1.12rem;
    margin: 22px 0 11px;
}

.stButton button {
    background: #ffffff !important;
    border: 2px solid #b9e5fa !important;
    border-radius: 17px !important;
    color: #17567a !important;
    font-weight: 800 !important;
    font-size: 1.15rem !important;
    min-height: 65px;
    box-shadow: 0 6px 18px rgba(40,117,165,.08);
    transition: transform .15s, background .15s;
}

.stButton button:hover {
    background: #daf3ff !important;
    border-color: #5db8e7 !important;
    transform: translateY(-2px);
}

.stButton button:focus-visible {
    outline: 3px solid #2088bc;
    outline-offset: 2px;
}

.card {
    background: linear-gradient(150deg,#fff,#e9f8ff);
    border: 1px solid #c5e8f7;
    border-radius: 25px;
    padding: 26px 23px;
    box-shadow: 0 12px 30px rgba(30,103,152,.10);
    text-align: center;
    margin-top: 12px;
}

.pill {
    display: inline-block;
    background: #dff4ff;
    color: #16739f;
    font-weight: 800;
    padding: 8px 17px;
    border-radius: 30px;
}

.name {
    font-size: 2.4rem;
    font-weight: 900;
    color: #155a82;
    margin: 14px 0 2px;
}

.english {
    font-size: 1.1rem;
    color: #588aa7;
}

.type {
    display: inline-block;
    background: #c6edff;
    border-radius: 14px;
    padding: 8px 17px;
    color: #155b85;
    font-weight: 800;
    margin: 15px 0;
}

.traits {
    color: #376781;
    line-height: 1.8;
    font-size: 1.05rem;
}

.reason {
    background: #fff;
    border: 1px solid #d3effd;
    border-radius: 16px;
    padding: 19px;
    text-align: left;
    line-height: 2;
    color: #28536c;
    margin-top: 20px;
    font-size: 1.02rem;
}

.note {
    text-align: center;
    color: #66869b;
    font-size: .84rem;
    margin-top: 33px;
    line-height: 1.9;
}

[data-testid='stImage'] img {
    object-fit: contain;
    max-height: 330px;
    filter: drop-shadow(
        0 11px 12px rgba(35,113,160,.13));
}

@media(max-width:600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .stButton button {
        font-size: .98rem !important;
        min-height: 59px;
    }

    .card {
        padding: 19px 14px;
    }

    .name {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown(
    '<div class="kicker">✦ POKÉMON × MBTI ✦</div>',
    unsafe_allow_html=True
)

st.title("☁️ 나의 단짝 포켓몬 찾기")

st.markdown(
    '<p class="subtitle">'
    '나의 성격과 잘 어울리는 포켓몬은 누구일까요?<br>'
    'MBTI를 선택하고 단짝을 만나 보세요!'
    '</p>',
    unsafe_allow_html=True
)

# 선택한 MBTI 기억하기
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

# MBTI 선택 화면
if st.session_state.selected_mbti is None:

    st.markdown(
        '<p style="color:#54778e;text-align:center;'
        'font-weight:700">👇 내 MBTI를 골라 주세요</p>',
        unsafe_allow_html=True
    )

    for group, types in GROUPS.items():

        st.markdown(
            f'<div class="group">{group}</div>',
            unsafe_allow_html=True
        )

        cols = st.columns(4, gap="small")

        for col, mbti in zip(cols, types):
            with col:
                if st.button(
                    mbti,
                    key=mbti,
                    use_container_width=True
                ):
                    st.session_state.selected_mbti = mbti
                    st.session_state.celebrate = True
                    st.rerun()

# 포켓몬 결과 화면
else:
    mbti = st.session_state.selected_mbti

    name_ko, name_en, dex_id, poke_type, traits, reason = (
        POKEMON[mbti]
    )

    # 포켓몬 아트워크 이미지
    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{dex_id}.png"
    )

    # 축하 애니메이션
    if st.session_state.celebrate:
        st.balloons()
        st.snow()
        st.session_state.celebrate = False

    st.markdown(
        '<div class="kicker">🎉 단짝 찾기 성공!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<h2 style="text-align:center;color:#195f86">'
        f'{mbti}의 단짝 포켓몬</h2>',
        unsafe_allow_html=True
    )

    # 포켓몬 사진
    st.image(
        image_url,
        caption=f"{name_ko} ({name_en}) · Pokémon Artwork",
        use_container_width=True
    )

    # 줄바꿈 및 HTML 표시 오류 수정
    reason_html = "<br>".join(
        html.escape(line) for line in reason.splitlines()
    )

    # 결과 카드
    # HTML을 한 줄씩 연결해 코드로 보이는 오류 방지
    card_html = (
        '<div class="card">'
        '<span class="pill">💎 MY POKÉMON PARTNER</span>'
        f'<div class="name">{html.escape(name_ko)}</div>'
        f'<div class="english">{html.escape(name_en)}</div>'
        f'<div class="type">✨ 타입 · '
        f'{html.escape(poke_type)}</div>'
        f'<div class="traits"><b>🌟 특징</b><br>'
        f'{html.escape(traits)}</div>'
        f'<div class="reason">'
        f'<b>💬 나와 어울리는 이유</b><br><br>'
        f'{reason_html}</div>'
        '</div>'
    )

    st.markdown(
        card_html,
        unsafe_allow_html=True
    )

    st.write("")

    # 다시 선택하기
    if st.button(
        "🔄 다시 고르기",
        use_container_width=True,
        type="primary"
    ):
        st.session_state.selected_mbti = None
        st.session_state.celebrate = False
        st.rerun()

# 하단 안내
st.markdown(
    '<div class="note">'
    'MBTI와 포켓몬의 연결은 재미를 위한 창작 설정입니다.<br>'
    '포켓몬 이미지는 온라인 PokéAPI Sprites에서 불러옵니다.'
    '</div>',
    unsafe_allow_html=True
)
