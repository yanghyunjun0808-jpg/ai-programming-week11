import pandas as pd
from analysis import 정제, 반별평균


scores_df = pd.read_csv("scores_2026.csv", dtype={"학번": str})
mini_df = pd.read_csv("mini.csv", dtype={"학번": str})


def test_scores_정제후_100행():
    assert len(정제(scores_df)) == 100


def test_정제후_반은_두종류():
    정제된_df = 정제(scores_df)
    assert set(정제된_df["반"].unique()) == {"1반", "2반"}


def test_반별점수합계가_전체합계와_같다():
    정제된_df = 정제(scores_df)
    반별_합계 = 정제된_df.groupby("반")["점수"].sum()
    assert 반별_합계.sum() == 정제된_df["점수"].sum()


def test_mini_1반_평균은_80점():
    정제된_mini = 정제(mini_df)
    평균 = 반별평균(정제된_mini)
    assert 평균["1반"] == 80.0