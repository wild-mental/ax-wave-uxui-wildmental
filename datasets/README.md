# 프로필 데이터셋

교재 「핵심 타깃 프로필」의 네 명에게 딸린 4주치 가상 기록입니다(2026-10-05 ~ 2026-11-01, 28일). 고른 프로필의 폴더에서 CSV 4개를 내려받아, Day 3에는 작업 폴더 `axyourbody-prototype/data/`에 넣습니다.

| 프로필 | 폴더 | 파일 |
|---|---|---|
| 김도현 (남성 · 일반인) | `m-general` | [body](m-general/body.csv) · [workout](m-general/workout.csv) · [meal](m-general/meal.csv) · [sleep](m-general/sleep.csv) |
| 이서연 (여성 · 일반인) | `f-general` | [body](f-general/body.csv) · [workout](f-general/workout.csv) · [meal](f-general/meal.csv) · [sleep](f-general/sleep.csv) |
| 박준혁 (남성 · 운동인) | `m-athlete` | [body](m-athlete/body.csv) · [workout](m-athlete/workout.csv) · [meal](m-athlete/meal.csv) · [sleep](m-athlete/sleep.csv) |
| 정하은 (여성 · 운동인) | `f-athlete` | [body](f-athlete/body.csv) · [workout](f-athlete/workout.csv) · [meal](f-athlete/meal.csv) · [sleep](f-athlete/sleep.csv) |

링크를 누르면 내용이 화면에 보입니다. 파일로 저장하려면 링크에서 오른쪽 버튼 → 「다른 이름으로 링크 저장」을 고릅니다.

## 열 이름 읽는 법

| 파일 | 열 | 뜻 |
|---|---|---|
| `body.csv` | `date` · `weight_kg` · `skeletal_muscle_kg` · `body_fat_pct` · `measure_condition` | 날짜 · 체중(kg) · 골격근량(kg) · 체지방률(%) · 측정 조건 |
| `workout.csv` (일반인) | `date` · `type` · `minutes` · `activity` · `steps` | 날짜 · 운동 종류 · 시간(분) · 활동 · 걸음 수 |
| `workout.csv` (운동인) | `date` · `type` · `minutes` · `exercise` · `weight_kg` · `reps` · `sets` · `rpe` | 날짜 · 운동 종류 · 시간(분) · 종목 · 무게(kg) · 반복 · 세트 · RPE(운동 자각도) |
| `meal.csv` | `date` · `meal` · `carbs_g` · `protein_g` · `fat_g` | 날짜 · 끼니 · 탄수화물(g) · 단백질(g) · 지방(g) 대략값 |
| `sleep.csv` | `date` · `sleep_hours` · `condition_1to5` | 날짜 · 수면 시간 · 컨디션(1~5) |

스프레드시트 프로그램(Excel, Google 스프레드시트, Numbers)으로 열 때 글자가 깨지면 「가져오기」에서 인코딩을 UTF-8로 고릅니다. 여는 법은 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」에 있습니다.

모든 이름과 수치는 수업을 위해 만든 가상 데이터입니다.
