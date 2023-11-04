import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

def Apply_CSS_Style():
    # HTML에 CSS-STYLE 지정
    with open('style.css', encoding = "utf-8")as f:
        style = f.read()
    st.markdown(f"<style>{style}</style>", unsafe_allow_html = True)

st.title("NEWS_tudy")

# 게이지 바를 만들고 초기값을 0으로 설정
progress = st.progress(0)
progress_value = 20
progress.progress(progress_value)

# Session State 초기화
if 'page_num' not in st.session_state:
    st.session_state.page_num = 1

col1, col2 = st.columns(2)

with col1:
    selected_category = st.radio("카테고리 선택", ["경제", "사회", "IT", "국제"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    

with col2:
    selected_level = st.radio("레벨 선택", ["LEVEL1", "LEVEL2", "LEVEL3"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
# 기사 정보를 스크랩하고 박스에 표시하는 함수
def scrape_news_first(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title_element = soup.find("h2", class_="news_ttl")
        if title_element:
            title = title_element.text

            # 기사 내용 파일 읽기
            with open("economy.txt", "r", encoding="utf-8") as file:
                file_contents = file.read()

            # 기사 이미지 추출 및 표시 (필요에 따라 수정)
            image_element = soup.find("img", class_="")
            if image_element and "src" in image_element.attrs:
                image_url = image_element["src"]
                # 박스 생성
                # Text area를 사용하여 기사 내용을 표시
                with st.container():
                    st.write(f"기사 제목: {title}")
                    st.text_area("기사 내용", file_contents, height=200)
                    #st.image(image_url, caption="기사 이미지", use_column_width=True)
                    st.image("karina.jpeg",caption="카리나",use_column_width =True)
            else:
                st.write("이미지를 찾을 수 없습니다.")
        else:
            st.write("기사 제목을 찾을 수 없습니다.")
    else:
        st.write("기사를 가져오는 데 문제가 발생했습니다.")

# 기사 정보를 스크랩하고 박스에 표시하는 함수
def scrape_news_second(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title_element = soup.find("h2", class_="news_ttl")
        if title_element:
            title = title_element.text

            # 기사 내용 파일 읽기
            with open("economy.txt", "r", encoding="utf-8") as file:
                file_contents = file.read()

            # 기사 이미지 추출 및 표시 (필요에 따라 수정)
            image_element = soup.find("img", class_="")
            if image_element and "src" in image_element.attrs:
                image_url = image_element["src"]
                # 박스 생성
                # Text area를 사용하여 기사 내용을 표시
                with st.container():
                    st.write(f"기사 제목: {title}")
                    st.text_area("기사 내용", file_contents, height=200)
                    
            else:
                st.write("이미지를 찾을 수 없습니다.")
        else:
            st.write("기사 제목을 찾을 수 없습니다.")
    else:
        st.write("기사를 가져오는 데 문제가 발생했습니다.")

def add_quiz_page_problem():
    st.header("퀴즈")

    # 5개의 퀴즈 문제와 정답 리스트
    quiz_questions = [
        "첫 번째 퀴즈: 이 문장은 맞습니까?",
        "두 번째 퀴즈: 이 문장은 틀립니까?",
        "세 번째 퀴즈: 이 문장은 맞습니까?",
        "네 번째 퀴즈: 이 문장은 틀립니까?",
        "다섯 번째 퀴즈: 이 문장은 맞습니까?"
    ]
    correct_answers = [True, False, True, False, True]
    user_choices = []

    for i in range(5):
        user_choice = st.radio(f'문제 {i + 1}: {quiz_questions[i]}', ('O', 'X'))
        user_choices.append(user_choice)

    return user_choices, correct_answers


def add_quiz_page_solved(user_choices, correct_answers):
    st.header("퀴즈 해설")

    col1,col2 = st.columns(2)
    with col1 :
        quiz_questions = [
        "첫 번째 퀴즈: 이 문장은 맞습니까?",
        "두 번째 퀴즈: 이 문장은 틀립니까?",
        "세 번째 퀴즈: 이 문장은 맞습니까?",
        "네 번째 퀴즈: 이 문장은 틀립니까?",
        "다섯 번째 퀴즈: 이 문장은 맞습니까?"
    ]
        for i in range(5):
            st.write(f'{quiz_questions[i]}')
            
    with col2 : 
        for i in range(5):
            if user_choices[i] == correct_answers[i]:
                st.write("정답입니다!")
            else:
                st.write("틀렸습니다.")
                st.write('해설')

# 다음 페이지로 이동하는 함수
def next_page():
    st.session_state.page_num += 1

def back_page():
    st.session_state.page_num -= 1

# 현재 페이지 번호에 따라 해당 페이지의 내용을 표시
if st.session_state.page_num == 1 :
    if selected_category == "경제":
        st.text_area("Today's Keyword", "인플레이션(Inflation)", height=100)
    st.write(f"현재 페이지: {st.session_state.page_num}")
    st.write('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    st.empty()
    # 다음으로 넘어가기 버튼
    if st.button("다음으로 넘어가기"):
        next_page()
    st.session_state.user_choices = None
    st.session_state.correct_answers = None

elif st.session_state.page_num == 2 :
    # 선택된 카테고리에 따른 글 작성 폼 표시
    if selected_category == "경제":
        category_url = "https://www.mk.co.kr/news/economy/10864179"
        scrape_news_first(category_url)

    st.text_area("Keywords","마약은 나빠요",height=200)
    st.write(f"현재 페이지: {st.session_state.page_num}")
    st.write('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    st.empty()
    # 다음으로 넘어가기 버튼
    if st.button("다음으로 넘어가기"):
        next_page()
    # 이전으로 돌아가기 버튼
    if st.button("이전으로 돌아가기"):
        back_page()

elif st.session_state.page_num == 3:
    # 퀴즈 페이지 추가
    user_choices, correct_answers = add_quiz_page_problem()
    # 페이지 하단에 현재 페이지 번호 표시
    st.write(f"현재 페이지: {st.session_state.page_num}")
    st.write('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    st.empty()

    # "다음으로 넘어가기" 버튼을 누를 때 추가 조건 없이 항상 다음 페이지로 이동합니다.
    if st.button("다음으로 넘어가기"):
        next_page()

    # 이전으로 돌아가기 버튼
    if st.button("이전으로 돌아가기"):
        back_page()

    st.session_state.user_choices = user_choices
    st.session_state.correct_answers = correct_answers


elif st.session_state.page_num == 4:
    user_choices = st.session_state.user_choices
    correct_answers = st.session_state.correct_answers
    add_quiz_page_solved(user_choices, correct_answers)
    # 페이지 하단에 현재 페이지 번호 표시
    st.write(f"현재 페이지: {st.session_state.page_num}")
    st.write('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    st.empty()
    if st.button("다음으로 넘어가기"):
        next_page()
    # 이전으로 돌아가기 버튼
    if st.button("이전으로 돌아가기"):
        back_page()
        
elif st.session_state.page_num == 5 :
    
    st.markdown("<h1 style='text-align: center; color: black;'>누적 오답 단어</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1 :
        st.subheader("틀린 단어")
        st.write("단어1")
        st.write("단어2")
        st.write("단어3")

    with col2 :
        st.subheader("틀린 날짜")
    
    with col3 :
        st.subheader("링크")
    st.write(f"현재 페이지: {st.session_state.page_num}")
    st.write('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    st.empty()
    if st.button("다음으로 넘어가기"):
        next_page()
    # 이전으로 돌아가기 버튼
    if st.button("이전으로 돌아가기"):
        back_page()
        

elif st.session_state.page_num == 6:
    with open("economy.txt", "r", encoding="utf-8") as file:
        raw_contents = file.read()
    st.text_area("원본 기사",raw_contents,height=300)

    st.text_area("비평문","국필호 바보",height=200)

    st.write(f"현재 페이지: {st.session_state.page_num}")
    if st.button("다음으로 넘어가기"):
        next_page()
    # 이전으로 돌아가기 버튼
    if st.button("이전으로 돌아가기"):
        back_page()

elif st.session_state.page_num == 7:
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("**내가 쓴 비평문**", "이 기사에 따르면 윤석열 정부가 지방 경제를 돕기 위한 계획을 발표했다고 합니다. 이 계획은 전국에 초광역경제권 7곳을 만들고, 그 지역에서 새로운 일자리와 기술을 개발하려고 합니다. 이것은 지역 경제를 키우고 소멸 위기에 있는 지역을 돕는 좋은 아이디어 같아요. 또한, 지역에 더 많은 사람들이 살게 만들려고 하는데, 그건 지역에 생기와 활력을 불어넣을 수 있을 것 같아요. 여행 할인과 관광 콘텐츠도 늘릴 거라고 하니, 더 많은 사람들이 지방을 방문할 거 같아요. 이 계획은 지방 경제와 지역 사회에 도움이 될 것 같아서 기대돼요.", height = 200) 
    with col2:
        st.text_area("**AI 비평문**", "이 기사는 윤석열 정부가 지방경제를 활성화하고 인구감소로 소멸 위기에 처한 지역을 지원하기 위한 계획을 발표했다는 내용을 다루고 있습니다. 윤석열 정부는 전국에 초광역경제권 7곳을 구축하고 권역별 신산업을 육성하는 방안을 제시했습니다. 이 계획은 지역 경제를 활성화시키는 중앙과 지방 자치 단체 간의 협력을 강화하는 것을 목표로 하고 있으며, 이로써 소멸 위기에 처한 지역을 지원하려는 노력을 보여줍니다.\n\n또한, 이 계획은 \"생활인구\"를 늘리는 정책을 통해 지방의 인구 절벽 위기에 대응하려는 것도 강조하고 있습니다. \"생활인구\"란 지역에 일정 기간 동안 체류하는 주민 및 외국인뿐만 아니라 관광객, 통근자, 통학생 등을 포함한 개념입니다. 이를 통해 지역의 활력을 높이고 지방 경제를 지원하려는 목적으로 다양한 정책을 제시하고 있습니다.\n\n또한, 관광 인구를 늘리기 위해 \"디지털 관광주민증\"을 발급하고 여행 할인 혜택을 제공하며 관광 콘텐츠와 인프라를 향상시키는 방안도 언급되었습니다.\n\n마지막으로, 연구개발특구와 규제자유특구를 통해 과학기술 개발과 규제 혁신을 추진하는 방안을 소개하며 지역 경쟁력을 강화하는 계획도 제시하고 있습니다. 이러한 노력을 통해 지방 경제의 활성화와 지역 사회의 활력 증진을 목표로 하고 있는 것으로 보입니다.", height=200)
    
    st.text_area("**AI 평가**", """내용 일치성 (유사성 점수: 90%)

두 비평문은 주요 내용과 주장에서 크게 일치합니다. 언급된 주요 토픽 및 윤석열 정부의 계획에 대한 설명은 유사합니다.
어휘와 문장 구조 (유사성 점수: 85%)

사용된 어휘와 문장 구조도 유사하며, 비슷한 표현과 단어가 사용되었습니다. 이는 주요 주장과 내용 일치성을 뒷받침합니다.
긍정적인 평가 (유사성 점수: 80%)

두 비평문 모두 윤석열 정부의 계획을 긍정적으로 평가하고, 이를 효과적으로 논리적으로 설명하고 있습니다.
문장 구성과 일관성 (유사성 점수: 85%)

두 비평문은 문장 구성과 일관성을 유지하고 있으며, 첫 번째 문장부터 마지막 문장까지 내용이 일관되게 이어져갑니다.
부가 정보 (유사성 점수: 70%)

'AI 비평문'은 추가 정보 및 상세한 내용을 제공하는 측면에서 더 풍부합니다. 이로 인해 '나의 비평문'과 비교해 일부 부분에서 유사성이 낮게 나올 수 있습니다.
평균적으로, '나의 비평문'과 'AI 비평문'은 84% 정도의 유사성을 가지고 있으며, 이는 주요 내용과 주장이 일치하고 어휘 및 문장 구조가 유사하다는 것을 나타냅니다. 다만, 'AI 비평문'이 부가 정보를 더 제공하여 일부 부분에서 높은 유사성을 보일 수 있습니다""", height=400)

    image_84 = Image.open("score.png")
    st.image(image_84)

    st.markdown("**평가에 쓰인 핵심 키워드**")

    keywords = [
        "윤석열 정부", "지방 경제", "초광역경제권", "소멸 위기",
        "지방자치단체", "규모의 경제", "생활인구", "지역 경제 발전",
        "인구감소", "지역 활력", "디지털 관광주민증", "관광 콘텐츠",
        "인프라", "연구개발특구", "규제자유특구", "과학기술 개발",
        "규제 혁신", "지역 경쟁력", "지방 사회"
    ]

    columns = st.columns(4)
    for i, keyword in enumerate(keywords):
        columns[i % 4].write(keyword)


    st.write(f"현재 페이지: {st.session_state.page_num}")

    # 처음으로 돌아가는 버튼
    if st.button("처음으로 돌아가기"):
        st.session_state.page_num = 1

