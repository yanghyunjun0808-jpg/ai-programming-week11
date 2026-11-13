# (프로그램 이름을 적으세요)

<!-- 예) 성적 CSV 검증기 -->

<!--
  README 여섯 항목 양식입니다. (실습 PPT 28쪽 · 학습지 ⑤와 같은 순서)
  1. 이 파일의 이름을 README.md 로 바꾼 뒤 아래 칸을 채웁니다.
  2. <!-- 로 시작하는 설명은 다 채운 뒤 지웁니다.
  3. 명령은 직접 실행해 보고, 실제로 나온 결과만 적습니다.
  4. 공개 저장소이므로 학번·연락처는 적지 않습니다. (학번은 학습지에만)
  5. 각 칸의 내용은 설명이 끝나는 줄 아래 빈 줄에 적습니다. (설명 안에 쓰면 GitHub에 보이지 않습니다)

  판정 기준: 처음 보는 사람이 이 문서만 보고 실행과 테스트를 할 수 있는가.
  (게시 후 새 폴더에 clone해 이 문서대로 직접 실행해 봅니다)
-->

## ① 무엇을 하나요 (What · 현재 상태)
성적이 기록된 CSV 파일을 읽어 유효한 점수와 제외된 데이터를 구분하는 프로그램입니다.

유효한 점수(0~100점)를 목록으로 반환합니다.

잘못된 데이터는 제외하고 해당 행과 제외 사유를 기록합니다.
<!--
  기능 한 문장 + 지금 되는 것 / 안 되는 것.
  예) 성적 CSV를 읽어 유효한 점수 목록과 제외한 행의 기록을 돌려줍니다.
      평균·학점 계산은 아직 하지 않습니다.
-->

## ② 왜 만들었나요 (Why)
CSV 파일에는 이름이나 점수가 비어 있거나, 점수 범위를 벗어나거나, 숫자가 아닌 문자가 입력되는 등 다양한 예외 상황이 발생할 수 있습니다.

이러한 데이터를 구분하고 잘못된 데이터가 프로그램에 영향을 주지 않도록 검증하는 방법을 익히기 위해 만들었습니다.
<!--
  코드만 보고는 알 수 없는, 내가 직접 쓰는 칸입니다. 두세 문장.
  예) 실제 성적 파일에는 빈 칸·범위 밖 점수·글자 점수가 섞여 있어,
      그대로 읽으면 프로그램이 멈추거나 잘못된 값이 들어가기 때문입니다.
-->

## ③ 어떻게 쓰나요 (How)
Python이 설치되어 있어야 합니다. 저장소 폴더의 터미널에서 실행합니다.

python --version
python load_scores.py scores.csv

필요한 경우 테스트 도구를 설치합니다.

python -m pip install pytest pytest-cov

예상 결과: 실제 실행 결과를 확인하여 입력
<!-- 복사해서 그대로 실행할 수 있게. 저장소 폴더의 터미널 기준. -->

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv
```

<!-- set 줄: 강의실 PC처럼 옛 Anaconda가 깔린 PC에서 pytest 플러그인 오류를 막습니다.
     새 터미널을 열 때마다 pytest 전에 한 번 입력합니다. -->

예상 결과: (실행해 보고 적으세요. 예: 읽은 줄 5개 / 건너뛴 줄 5개)
읽은 줄 5개 / 건너뛴 줄 5개

## ④ 어떻게 테스트하나요
다음 명령어로 테스트를 실행합니다.

python -m pytest test_load_scores.py -q

실제 결과: 실행 후 통과한 테스트 개수와 결과 입력

테스트에서는 일반적인 CSV 데이터뿐 아니라 빈 줄, 따옴표가 포함된 이름, 파일 누락, 헤더만 있는 파일, 점수의 경계값 등을 확인합니다.

test_bug_A.py, test_bug_B.py는 별도의 논리 오류 실험용 파일이며, 정상적인 테스트 결과와 구분하여 확인합니다.
```
python -m pytest test_load_scores.py -q
```

실제 결과: (예: 11 passed — 내 화면에 나온 그대로)
11 passed

<!-- 예) 12 passed (기본 11개 + weird.csv 보강 1개)
     예) test_bug_A.py·test_bug_B.py는 find_max 버그를 찾아 2개씩 실패 -->

<!-- AI 실험 파일(test_bug_A.py, test_bug_B.py, 선택: test_ai_draft.py)은 비교용 원본입니다.
     일부 실패할 수 있으며, 그 이유를 한 줄로 적어 두세요. -->

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | (예: CSV를 읽어 (kept, skipped)를 돌려주는 함수) |
| scores.csv · empty.csv · weird.csv | 보편적, 예외적 상황을 다루고 있는 CSV 데이터 |
| test_load_scores.py | 성적 CSV 검증 테스트 |
| test_ai_draft.py (선택 실험을 했다면) |  |
| bug3_logic.py · test_bug_A.py · test_bug_B.py | 논리 오류 실험용 테스트 코드 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : (이름 또는 GitHub 아이디) yanghyunjun0808-jpg
- 사용한 AI 도구·모델 : VS Code Copliot Agent, ChatGPT (GPT-6)
- AI에게 도움받은 부분 : Python 코드 및 테스트 과정에 대한 설명, 오류 원인 분석, Git 사용법과 README 작성 보조
- 내가 직접 판단·확인한 부분 : 코드 실행, 테스트 결과 확인, 오류 수정 및 결과 검증

## 라이선스

MIT License (LICENSE 파일 참고) YHJ
