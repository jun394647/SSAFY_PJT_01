import pprint 
import requests

def get_deposit_products_2():
    # 본인의 API KEY 로 수정합니다.
    api_key_2 = "51adee17d40ad092e7405c23e9680bb6"
    return api_key_2

api_key_2 = "51adee17d40ad092e7405c23e9680bb6"

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result_2 = get_deposit_products_2()
    pprint.pprint(result_2)

#--------------------------------------------------------------------------------
#아래는 상품 리스트를 불러 옵니다.

result_2 = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key_2}&topFinGrpNo=020000&pageNo=1"

response_2 = requests.get(result_2).json()
#6)응답 데이터에서 Key 값들만 따로 추출하여 출력, 7) 상품 리스트 정보 출력

# print(response_2['result'].keys())
# print(response_2)

print("--------------------------------------------------------------")

# 8) 옵션 정보 리스트 출력

response_3 = response_2['result']['baseList']
#print(response_3)

def get_deposit_options(api_data):

    result_data = api_data["result"]

    options = result_data.get("optionList", [])
    
    processed_options = []
    
    for option in options:
        new_data = {
            "금융상품코드": option.get("fin_prdt_cd"),
            "저축 금리": option.get("intr_rate"),
            "저축 기간": option.get("save_trm"),
            "저축금리유형": option.get("intr_rate_type"),
            "저축금리유형명": option.get("intr_rate_type_nm"),
            "최고 우대금리": option.get("intr_rate2")
        }
        processed_options.append(new_data)
        
    return processed_options


result_3 = get_deposit_options(response_2)
# print(result_3)

#--------------------------------------------------------------------

# 9) 상품 , 옵션 데이터 통합

def get_deposit_products(api_response):
    result_data = api_response.get("result")
    base_list = result_data.get("baseList")
    option_list = result_data.get("optionList")
    
    final_result = []
    
    for base in base_list: 
        product_options = []
        
        for option in option_list:
            if option.get("fin_prdt_cd") == base.get("fin_prdt_cd"):
                option_dict = {
                    "저축 금리": option.get("intr_rate"),
                    "저축 기간": option.get("save_trm"),
                    "저축금리유형": option.get("intr_rate_type"),
                    "저축금리유형명": option.get("intr_rate_type_nm"),
                    "최고 우대금리": option.get("intr_rate2")
                }
                product_options.append(option_dict)
        
        combined_product = {
            "금리정보": product_options,
            "금융상품명": base.get("fin_prdt_nm"),
            "금융회사명": base.get("kor_co_nm")
        }
        

        final_result.append(combined_product)
        
    return final_result

result_4 = get_deposit_products(response_2)
print(result_4)
#--------------------------------------------------------------------
# 전체 정기예금 상품 리스트를 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "baseList" 인 데이터를 출력합니다.
