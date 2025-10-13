def safe_index(lst, item, start=0):
    """
    첫번째 매개변수 lst : 리스트, 튜플
    두번째 매개변수 item : 리스트나 튜플에서 찾을 데이터
    세번째 매개변수 start : 몇번째 index부터 찾을지 index 수(기본값:0)
    """
    return lst.index(item, start) if item in lst[start:] else -1
#     if item in lst[start:]:
#         return lst.index(item, start) # start번째부터 item이 있는 index를 반환
#     else:
#         return -1