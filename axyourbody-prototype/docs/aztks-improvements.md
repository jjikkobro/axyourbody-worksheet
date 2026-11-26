# AZTKS 검토 후 개선

2026-11-26 · 대상: `20261126-정정훈-AXYOURBODY프로토타입.html` · 범위: 검토에서 확인한 5개 항목

| 검토 항목 | 반영 내용 | 확인한 행동 |
|---|---|---|
| 체성분 제외 결과 확인 | 측정 조건 배지와 추세 포함/제외 배지를 각각 표시 | 10/22 제외 → 목록 확인 → 새로고침 → 포함 재설정. 원본 37.0kg 보존 |
| 상담 복귀 경로 | 상담 상세의 진입 화면을 기억해 뒤로 가기 적용 | 상담 목록·검색에서 진입하면 목록·검색으로, 오늘 계획에서 진입하면 오늘 계획으로 복귀 |
| 반복 방문 시 저장 상태 | 오늘 계획에 저장 전 변경·저장됨·마지막 저장 시각을 지속 표시 | 직접 입력·AI 초안·저장·새로고침. 저장 불가 시 이번 실행 중 반영이라고 표시 |
| 모바일 저장 안내 | 상단 프로필에 이름이 있는 안내 버튼 제공 | 390px에서 데이터·저장 안내 대화상자 열기·닫기 |
| 체성분 요약의 조회 기준 | 날짜·조건·포함 여부 필터에 맞는 마지막 측정으로 요약 갱신 | 10/19까지 조회, 훈련 직후만 조회, 조건에 맞는 기록 없음. 빈 결과에는 요약 숨김 |

## 검증

- 추가 회귀 검증 9개 통과: `verification/aztks-followup.cjs`, 결과 `verification/aztks-followup-results.json`.
- 기존 TF 30개 시나리오도 현재 HTML에서 재실행해 30개 통과. 결과는 `verification/tf-30-followup-results.json`에 별도 보존했다. U02는 새 지속 상태 영역과 기존 저장 완료 배너를 구분하도록 선택자를 보완했다.
- 320·390·768·1440px의 운동 계획 상세·체성분·상담 목록에서 가로 넘침 없음. 오프라인 실행 중 외부 요청·JavaScript 오류 없음.
- 미리보기: `verification/aztks-{390,1440}-{today,body}.png`.
- 실제 사용자 이해도·의료적 효과를 측정한 결과는 아니다. 기존 TF 점수는 당시의 내부 검증 항목에 대한 점수다.

## 재실행

Node.js, Playwright와 Chromium이 있는 환경에서 실행한다. 설치 경로가 다르면 `PLAYWRIGHT_MODULE`, `CHROMIUM_PATH`를 지정한다.

```bash
node verification/aztks-followup.cjs
RESULT_FILE=verification/tf-30-followup-results.json node verification/tf-30-simulations.cjs
```

TF 비교용 기존 HTML은 `tf-review-30.md`에 적힌 커밋에서 추출하거나 `BASELINE_HTML`로 지정한다.
