#test.py
import random
import pickle

#2중 dictionary 형태
def generate_random():
    outer_dict = {}

    # 바깥 dict에 key는 5개로 설정
    for i in range(5):
        inner_dict = {}
        # 안 dict의 key는 3개로 설정
        for j in range(3):
            #value 값은 1~50으로 랜덤설정
            inner_dict[f'list_{i}_weight_{j}']= random.randint(1,50)
        outer_dict[f'list_{i}'] = inner_dict

    return outer_dict

#dictionary 생성
random_dict = generate_random()

#pickle이용해서 data 저장
with open('random_dict.pkl', 'wb') as f:
    pickle.dump(random_dict, f)

#저장된 pickle file 다시 load
with open('random_dict.pkl', 'rb') as f :
    loaded_dict = pickle.load(f)

print(loaded_dict)