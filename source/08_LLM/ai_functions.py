def get_category():
    return {
        '납세의무': {
            '납세의무': 3, '거주자': 3, '비거주자': 3, '납세의무자': 3, 
            '원천징수': 2, '원천징수의무자': 2, '공동사업자': 2, 
            '상속인': 2, '증여자': 2, '신탁재산': 2
        },

        '세율계산': {
            '세율': 3, '소득세': 3, '과세표준': 3, '산출세액': 3, '세액': 3,
            '결정세액': 2, '세액계산': 2, '기본세율': 2, '세율적용': 2,
            '누진세율': 2, '종합소득세': 2
        },

        '근로소득': {
            '근로소득': 3, '총급여': 3, '급여': 3, '연봉': 3, '임금': 3,
            '근로소득금액': 2, '총급여액': 2, '상여': 2, '수당': 2,
            '봉급': 2, '직장인': 2
        },

        '사업소득': {
            '사업소득': 3, '총수입금액': 3, '필요경비': 3,
            '사업자': 2, '사업소득금액': 2, '결손금': 2, '이월결손금': 2,
            '주택임대소득': 2, '공동사업': 2
        },

        '이자배당': {
            '이자소득': 3, '배당소득': 3, '예금이자': 2, '채권': 2,
            '의제배당': 2, '배당세액공제': 2, '분리과세이자소득': 2,
            '분리과세배당소득': 2
        },

        '양도소득': {
            '양도소득': 3, '자산양도': 2, '부동산양도': 2, '주식양도': 2,
            '양도차익': 2, '취득가액': 2, '양도가액': 2, '양도소득금액': 2
        },

        '연금소득': {
            '연금소득': 3, '연금계좌': 3, '연금저축': 3,
            '퇴직연금': 2, '공적연금': 2, '사적연금': 2, '연금보험': 2,
            '연금수령': 2
        },

        '기타소득': {
            '기타소득': 3, '가상자산': 3, '가상자산소득': 2,
            '상금': 2, '보상금': 2, '종교인소득': 2, '원고료': 2,
            '복권': 1, '당첨금': 1, '발명보상금': 1
        },

        '공제감면': {
            '공제': 3, '소득공제': 3, '세액공제': 3,
            '기본공제': 2, '인적공제': 2, '특별공제': 2, '추가공제': 2,
            '근로소득공제': 2, '연금소득공제': 2, '퇴직소득공제': 2,
            '연금계좌세액공제': 2, '감면': 2
        },

        '비과세': {
            '비과세': 3, '비과세소득': 3, '면제': 2, '세액감면': 2,
            '소득세면제': 2, '복무급여': 1, '실업급여': 1, 
            '출산휴가급여': 1, '장학금': 1
        },

        '신고납부': {
            '신고': 3, '확정신고': 3, '과세표준확정신고': 3, 
            '납부': 3, '중간예납': 2, '가산세': 2,
            '신고기한': 2, '납부기한': 2, '납세지': 2
        },

        '과세기간': {
            '과세기간': 3, '과세연도': 3, '사업연도': 2, 
            '과세기간종료일': 2
        },

        '과세방식': {
            '종합과세': 3, '분리과세': 3, '합산과세': 2, 
            '종합소득과세표준': 2, '분리과세소득': 2, 
            '금융투자소득': 2
        },

        '장부기장': {
            '장부': 3, '복식부기': 3, '간편장부': 2, '기장': 2,
            '장부기록': 2, '증명서류': 2, '기장세액공제': 2
        }
    }
def categorize_content(content, top_k=None):
    """내용 카테고리 분류 - 점수 기반으로 모든 카테고리를 점수 순으로 반환
    Parameters :
    - content : 분류할 텍스트 내용
    - top_k : 상위 몇개까지 카테고리를 반환할지(None이면 모든 카테고리 반환)
    Returns:
    - 카테고리 리스트(점수 높은 순)"""
    category_keywords = get_category()
    category_scores = {}
    # 각 카테고리별 점수 계산
    for category, weighted_keywords in category_keywords.items():
        # print(category, weighted_keywords)
        score = 0
        for keyword, weight in weighted_keywords.items():
            if keyword in content:
                score += weight
            #count = content.count(keyword) 나온 횟수로 
            #score += count * weight
        if score > 0:
            category_scores[category] = score
    # print(category_scores)
    # 내림차순 정렬한 카테고리 이름만 추출
    sorted_categories = sorted(category_scores.items(), key=lambda x:x[1], reverse=True) # 내림차순
    # print(sorted_categories)
    all_categories = [category[0] for category in sorted_categories]
    # print(all_categories)
    # 매칭되는 카테고리가 없으면 "기타" 반환
    if not all_categories:
        all_categories = ["기타"]
    # top_k가 지정되면 상위 top_k개만, 아니면 전체 반환
    if top_k is not None:
        return all_categories[:top_k]
    else:
        return all_categories
    
# 참조 조항을 추출하는 함수
def extract_articles_from_docs(documents):
    """
    검색된 문서들에서 article 정보를 추출하여 리스트로 반환
    
    Args:
        documents: retriever에서 반환된 Document 객체 리스트
    
    Returns:
        list: 중복 제거된 조항 리스트 (예: ['제4조', '제16조', '제45조'])
    """
    articles = []
    
    for doc in documents:
        # metadata에서 article 정보 추출 (없으면 기본값)
        article = doc.metadata.get('article', '조항없음')
        
        # article이 문자열이면 그대로 사용, 아니면 처리
        if isinstance(article, str) and article != '조항없음':
            # 「4조, 16조, 45조」 형태를 분리
            article = article.replace('「', '').replace('」', '')
            article_list = [a.strip() for a in article.split(',')]
            articles.extend(article_list)
    
    # 중복 제거 및 정렬
    unique_articles = list(set(articles))
    unique_articles.sort(key=lambda x : int(x[:-1]))
    # '조' 앞에 '제'를 붙여서 표준 형식으로 변환
    # unique_articles = ['조항없음']
    final_articles = ["제"+article for article in unique_articles if article!='조항없음']
    if final_articles:
        return "소득세법 " + ", ".join(final_articles)
    else:
        return unique_articles[0]
    
def format_documents(documents):
    return  "\n\n---\n\n".join([doc.page_content for doc in documents])