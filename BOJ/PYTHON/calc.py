import sys




def divide_by_sum_of_nutrient(data):
    """
    Desc :
        영양소의 가중치를 구할 때, (음식 별 영양소 함유량)/(모든 음식의 영양소 총합)로 구한 결괏값을 반환하는 함수.

    Args :
        data : 정규화 할 데이터, 모든 column은 영양소이며 0행은 각 영양소의 명칭이다.

    Returns :
        Datafreme 형태로 모든 음식의 각 영양소를 0-1 정규화하여 반환
    """

    # 수정 필요
    for col in range(data.columns):
        col = "현재 컬럼 이름"
        sum_of_nutrient = data[col].sum()
        for row in range(data.rows):
            data[row, col] /= sum_of_nutrient


def calc_weight():
    """
    Desc :
        설문조사 결과로 (영양소 별 부족한 정도 가중치 ) x (음식 별 해당 영양소의 가중치 )를 계산한다.

    Args :
        data : 정규화 할 데이터, 모든 column은 영양소이며 0행은 각 영양소의 명칭이다.

    Returns :
        Datafreme 형태로 모든 음식의 각 영양소를 0-1 정규화하여 반환
    """
