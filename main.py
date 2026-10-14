
import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="🌟",
    layout="wide"
)

# 포켓몬 데이터
# 한국어 이름, 영어 이름, 도감 번호, 타입, 특징, 어울리는 이유
POKEMON = {
    "INTJ": (
        "뮤츠", "Mewtwo", 150, "에스퍼",
        "뛰어난 지능 · 독립심 · 강한 의지",
        "혼자 깊이 생각하고 치밀하게 계획하는 모습이 닮았어요.\n"
        "어려운 문제에도 냉정하게 집중해요.\n"
        "자신만의 목표를 끝까지 추구하는 단짝이에요."
    ),
    "INTP": (
        "메타몽", "Ditto", 132, "노말",
        "변신 능력 · 유연함 · 무한한 가능성",
        "끊임없이 새로운 가능성을 탐색하는 성향이 닮았어요.\n"
        "고정관념 없이 다양한 관점에서 생각해요.\n"
        "호기심 가득한 실험 정신을 가진 단짝이에요."
    ),
    "ENTJ": (
        "리자몽", "Charizard", 6, "불꽃 / 비행",
        "자신감 · 강한 힘 · 승부욕",
        "목표를 정하면 과감하게 앞으로 나아가요.\n"
        "도전적인 상황에서 리더십을 보여 줘요.\n"
        "큰 꿈을 향해 함께 비상할 든든한 단짝이에요."
    ),
    "ENTP": (
        "팬텀", "Gengar", 94, "고스트 / 독",
        "장난기 · 재치 · 대담함",
        "예측할 수 없는 아이디어로 모두를 놀라게 해요.\n"
        "새로운 상황을 재미있는 도전으로 받아들여요.\n"
        "재치 있는 모험을 즐기기에 딱 맞는 단짝이에요."
    ),
    "INFJ": (
        "가디안", "Gardevoir", 282, "에스퍼 / 페어리",
        "공감 · 보호 본능 · 집중력",
        "다른 이의 마음을 세심하게 헤아리는 모습이 닮았어요.\n"
        "소중한 존재를 지키기 위해 조용히 힘을 발휘해요.\n"
        "따뜻한 신념을 함께 나눌 수 있는 단짝이에요."
    ),
    "INFP": (
        "이브이", "Eevee", 133, "노말",
        "다양한 진화 가능성 · 친근함 · 잠재력",
        "자신만의 꿈과 가능성을 소중히 생각해요.\n"
        "다양한 모습으로 성장할 수 있는 잠재력이 있어요.\n"
        "있는 그대로의 개성을 응원해 주는 단짝이에요."
    ),
    "ENFJ": (
        "님피아", "Sylveon", 700, "페어리",
        "친밀함 · 다정함 · 교감",
        "주변 친구들에게 따뜻한 에너지를 전해요.\n"
        "함께하는 이들의 감정에 세심하게 반응해요.\n"
        "서로 응원하며 성장하기 좋은 단짝이에요."
    ),
    "ENFP": (
        "피카츄", "Pikachu", 25, "전기",
        "활발함 · 친근함 · 강한 유대",
        "밝고 호기심 많은 성격으로 모험을 즐겨요.\n"
        "새로운 친구를 만나면 금세 활기를 불어넣어요.\n"
        "즐거운 추억을 함께 만들 최고의 단짝이에요."
    ),
    "ISTJ": (
        "거북왕", "Blastoise", 9, "물",
        "든든함 · 끈기 · 안정감",
        "묵묵히 맡은 역할을 해내는 모습이 닮았어요.\n"
        "신중하게 준비한 뒤 확실하게 움직여요.\n"
        "언제나 믿고 의지할 수 있는 단짝이에요."
    ),
    "ISFJ": (
        "럭키", "Chansey", 113, "노말",
        "배려 · 치유 · 친절함",
        "어려운 친구를 보면 먼저 도와주고 싶어 해요.\n"
        "주변의 작은 변화에도 세심하게 관심을 기울여요.\n"
        "편안함과 따뜻함을 나눌 수 있는 단짝이에요."
    ),
    "ESTJ": (
        "괴력몬", "Machamp", 68, "격투",
        "실행력 · 힘 · 성실함",
        "해야 할 일이 생기면 망설이지 않고 행동해요.\n"
        "꾸준한 노력으로 큰 성과를 쌓아 가요.\n"
        "함께 목표를 완수하기 좋은 듬직한 단짝이에요."
    ),
    "ESFJ": (
        "푸린", "Jigglypuff", 39, "노말 / 페어리",
        "표현력 · 친근함 · 노래",
        "자신의 매력을 드러내며 분위기를 밝게 만들어요.\n"
        "친구들과 즐거운 시간을 보내는 것을 좋아해요.\n"
        "함께할수록 웃음이 많아지는 단짝이에요."
    ),
    "ISTP": (
        "루카리오", "Lucario", 448, "격투 / 강철",
        "민첩함 · 관찰력 · 침착함",
        "주변 상황을 빠르게 파악하고 적절히 행동해요.\n"
        "화려한 말보다 실력으로 보여 주는 편이에요.\n"
        "위기의 순간에도 침착한 해결사 단짝이에요."
    ),
    "ISFP": (
        "나인테일", "Ninetales", 38, "불꽃",
        "우아함 · 개성 · 신비로움",
        "조용하지만 독특한 분위기와 매력이 있어요.\n"
        "자신만의 감성과 취향을 소중하게 여겨요.\n"
        "편안한 속도로 함께할 수 있는 단짝이에요."
    ),
    "ESTP": (
        "에이스번", "Cinderace", 815, "불꽃",
        "운동 감각 · 열정 · 순간 판단",
        "몸을 움직이며 새로운 도전에 뛰어드는 걸 좋아해요.\n"
        "빠른 판단과 과감한 행동이 돋보여요.\n"
        "짜릿한 순간을 함께 즐길 활동적인 단짝이에요."
    ),
    "ESFP": (
        "파치리스", "Pachirisu", 417, "전기",
        "활발함 · 장난기 · 에너지",
        "생기 넘치는 모습으로 주변을 즐겁게 만들어요.\n"
        "친구들과 어울리며 신나는 시간을 보내요.\n"
        "매일을 특별하게 만들어 줄 단짝이에요."
    )
}

# MBTI 그룹
GROUPS = {
    "🧠 분석가형": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "🌷 외교관형": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "🛡️ 관리자형": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "🎨 탐험가형": ["ISTP", "ISFP", "ESTP", "ESFP"]
}

# CSS 디자인
st.markdown("""
<style>
.stApp {
    background:
      radial-gradient(circle at 15% 5%,
        #fff0bc 0%, transparent 32%),
      linear-gradient(155deg,
        #fffaf0, #fff6dc 65%, #fffaf1);
    color: #493920;
}

.block-container {
    max-width: 1040px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p {
    font-family: 'Malgun Gothic',
                 'Apple SD Gothic Neo', sans-serif;
}

h1 {
    color: #4d3918 !important;
    font-size: clamp(2rem, 5vw, 3.2rem) !important;
    text-align: center;
}

.hero-sub {
    text-align: center;
    color: #807256;
    font-size: 1.12rem;
    margin-bottom: 24px;
    line-height: 1.8;
}

.eyebrow {
    text-align: center;
    color: #a47a11;
    font-size: .85rem;
    font-weight: 900;
    letter-spacing: .17em;
    margin: 15px 0;
}

.group-title {
    font-size: 1.14rem;
    font-weight: 850;
    color: #77602e;
    margin: 22px 0 8px;
}

.stButton > button {
    background: #fffdf7 !important;
    border: 2px solid #f0dda7 !important;
    border-radius: 17px !important;
    color: #5c431c !important;
    font-weight: 850 !important;
    font-size: 1.12rem !important;
    min-height: 66px;
    width: 100%;
    box-shadow: 0 5px 14px #9a6b1710;
    transition: all .15s;
}

.stButton > button:hover {
    background: #ffe394 !important;
    border-color: #edba39 !important;
    transform: translateY(-2px);
}

.intro {
    text-align: center;
    color: #7a6d55;
    font-size: 1.05rem;
}

.card {
    border: 1px solid #f2dfb6;
    background: linear-gradient(145deg,
        #fff2c4, #fffef8);
    border-radius: 26px;
    padding: 25px 24px;
    text-align: center;
    box-shadow: 0 16px 35px #7b56171c;
}

.pill {
    display: inline-block;
    border-radius: 99px;
    background: #fff;
    padding: 8px 18px;
    color: #966b0a;
    font-weight: 800;
}

.poke-name {
    font-size: 2.5rem;
    font-weight: 900;
    color: #573d13;
    margin: 12px 0 2px;
}

.english {
    font-size: 1.08rem;
    color: #a48650;
}

.type-pill {
    display: inline-block;
    background: #ffdb7b;
    color: #674709;
    border-radius: 12px;
    padding: 7px 16px;
    margin: 15px 0;
    font-weight: 750;
}

.attribute {
    font-size: 1rem;
    color: #655435;
    line-height: 1.8;
}

.explain {
    background: #fffdf8;
    border-radius: 17px;
    padding: 20px;
    text-align: left;
    color: #584831;
    line-height: 2;
    font-size: 1.05rem;
    margin-top: 12px;
    white-space: pre-line;
}

.note {
    text-align: center;
    color: #9b8b6e;
    font-size: .83rem;
    margin-top: 30px;
    line-height: 1.8;
}

[data-testid="stImage"] img {
    object-fit: contain;
    max-height: 320px;
    filter: drop-shadow(
        0 12px 12px #77592326);
}

@media(max-width:600px) {
    .block-container {
        padding-left: 1.05rem;
        padding-right: 1.05rem;
    }
    .stButton > button {
        font-size: 1rem !important;
        min-height: 60px;
    }
    .card {
        padding: 18px 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# 화면 제목
st.markdown(
    '<div class="eyebrow">✦ POKÉMON × MBTI ✦</div>',
    unsafe_allow_html=True
)

st.title("🌟 나의 단짝 포켓몬 찾기")

st.markdown("""
<p class="hero-sub">
16가지 MBTI 중 내 유형을 선택하면<br>
나와 닮은 단짝 포켓몬이 나타나요!
</p>
""", unsafe_allow_html=True)

# 선택 정보 저장
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

# MBTI 선택 화면
if st.session_state.selected_mbti is None:

    st.markdown(
        '<div class="intro">👇 내 MBTI 버튼을 눌러 보세요</div>',
        unsafe_allow_html=True
    )

    for label, types in GROUPS.items():
        st.markdown(
            f'<div class="group-title">{label}</div>',
            unsafe_allow_html=True
        )

        columns = st.columns(4, gap="small")

        for col, mbti in zip(columns, types):
            with col:
                if st.button(
                    mbti,
                    key=f"select_{mbti}",
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

    # 인터넷 포켓몬 이미지
    image_url = (
        "https://raw.githubusercontent.com/"
        "PokeAPI/sprites/master/sprites/"
        "pokemon/other/official-artwork/"
        f"{dex_id}.png"
    )

    # 축하 애니메이션
    if st.session_state.celebrate:
        st.balloons()
        st.session_state.celebrate = False

    st.markdown(
        '<div class="eyebrow">🎉 단짝 찾기 성공!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<h2 style="text-align:center;color:#795512">'
        f'{mbti}의 단짝은 누구?</h2>',
        unsafe_allow_html=True
    )

    left, mid, right = st.columns([1, 3, 1])

    with mid:
        st.markdown("""
        <div class="card">
            <span class="pill">
                💛 MY POKÉMON PARTNER
            </span>
        </div>
        """, unsafe_allow_html=True)

        # 포켓몬 이미지 표시
        try:
            st.image(
                image_url,
                caption=f"{name_ko} · Pokémon Artwork",
                use_container_width=True
            )
        except Exception:
            st.markdown(
                '<div style="text-align:center;font-size:6rem">'
                '🌟</div>',
                unsafe_allow_html=True
            )

        # 포켓몬 설명 카드
        st.markdown(f"""
        <div class="card">

            <div class="poke-name">
                {name_ko}
            </div>

            <div class="english">
                {name_en}
            </div>

            <div class="type-pill">
                ✨ 타입 · {poke_type}
            </div>

            <div class="attribute">
                <b>특징</b><br>
                {traits}
            </div>

            <div class="explain">
                <b>💬 나와 어울리는 이유</b><br>
                {reason}
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # 다시 선택하기
    if st.button(
        "↩️ 다른 MBTI 다시 고르기",
        use_container_width=True,
        type="primary"
    ):
        st.session_state.selected_mbti = None
        st.session_state.celebrate = False
        st.rerun()

# 하단 안내
st.markdown("""
<div class="note">
이 매칭은 재미를 위한 창작 콘텐츠이며,
과학적인 성격 진단은 아닙니다.<br>
포켓몬 이미지: PokéAPI Sprites (온라인 이미지)
</div>
""", unsafe_allow_html=True)
