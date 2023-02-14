# babbling의 각 문자열에서 단어들은 각각 최대 한 번씩만 등장

# 조합은 순서를 고려하지 않음
# 순열은 순서를 고려 → 순열 사용!

from itertools import permutations

def solution(babbling) :
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    bab = []

    # range(len(word))로 실행하면 안 됨
    # python은 index가 0부터 시작하기 때문에, permutations(word, 0)이 되어버리면 0개의 원소를 골라 순열을 생성하는 것이기 때문
    # len(word)로 마지막 index를 설정하면, 모든 조합이 나오지 않음
    # index를 1부터 시작하지 않으면 런타임 에러 뜸
    for i in range(1, len(word)+1) :
        for j in permutations(word, i) :
            # 리스트 안의 문자열들을 구분자를 기준으로 합쳐줌
            bab.append("".join(j))

    for i in babbling :
        if i in bab :
            answer += 1

    return answer