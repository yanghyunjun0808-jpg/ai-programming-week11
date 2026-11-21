import pandas as pd

def 정제(df):
    결과 = df.copy()

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    결과["반"] = 결과["반"].str.strip()
    결과["과목"] = 결과["과목"].str.strip()
    print(f"공백 제거 후: {len(결과)}행")

    # 점수가 비어 있는 행을 제거한다.
    결과 = 결과.dropna(subset=["점수"]).copy()
    print(f"빈 점수 제거 후: {len(결과)}행")

    # 모든 열이 같은 중복 행을 제거한다.
    결과 = 결과.drop_duplicates().copy()
    print(f"중복 제거 후: {len(결과)}행")       

    # 0~100 범위를 벗어난 점수를 제거한다.
    결과 = 결과[결과["점수"].between(0, 100)].copy()
    print(f"점수 범위 정리 후: {len(결과)}행")

    return 결과

df = 정제(pd.read_csv("scores_2026.csv", dtype={"학번": str}))
print("\n정제된 데이터:")
print(df.to_string(index=False))

def 반별평균(df):
    표 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
    print(표)
    return 표["mean"]

미니 = 정제 (pd.read_csv("mini.csv"))
print( 반별평균 ( 미니 ))