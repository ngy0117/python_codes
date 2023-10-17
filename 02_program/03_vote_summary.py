from collections import Counter

input_str = input("투표 결과를 입력하세요: ")  # 입력창

def str2int(vote_str):
    return [int(vote) for vote in vote_str.split()]

votes = str2int(input_str)
vote_count = Counter(votes)

for candidate, count in vote_count.items():
    print(f"기호 : {candidate} 득표수 : {count}")
