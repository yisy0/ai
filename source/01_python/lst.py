def safe_index(lst, item):
    """첫번째 매개변수 lst에서 item 요소가 있는 index를 반환. 
    item 요소가 없으면 -1 반환"""
    if item in lst:
        return lst.index(item)
    return -1