# 최종 보고 · 차분한 운동 코치 방향

이 문서는 첫 개선 당시의 범위와 검증 기록이다. 이후 사용자가 운동 여부·다음 행동·변경 영향의 부재를 지적해 범위를 확장했다. 현재 동작과 한계는 [계획에서 운동 일지까지](action-flow.md)를 따른다. 아래 검사 통과는 당시 기능 회귀 결과이며 전체 서비스 행동 흐름의 완성을 의미하지 않는다.

2026-11-27 · STOP REASON: COMPLETE

기존 필수 7개 화면과 상담 입력창의 문구·정보 위계·조작 흐름을 개선했다. 화면별 조작 목록의 미처리 항목은 0건이다. 목록은 현재 노출하는 기능의 범위이며, 준비 중인 서비스 기능까지 새로 구현했다는 의미는 아니다.

## 변경

- 따뜻한 배경과 절제된 녹색으로 정리하고, 중복 표어를 제거했다. 계획 편집과 참고 자료의 시각적 위계를 구분했다.
- ‘제안 수정 적용하기’를 ‘제안을 초안으로 가져오기’로 변경해 저장 전 단계임을 명확히 했다.
- 운동 수치 편집 취소, 몸 상태 선택 해제, 입력 전체 검사, 미저장 이탈 확인을 보완했다.
- 체성분 저장과 상담 연결에 입력 보존·직접 재시도를 제공했다. 상담 입력 저장 실패도 폼 내부에서 안내한다.
- 체성분 목록의 필터·스크롤 복귀, 잘못된 날짜 범위 안내, 저장 불가 시 이번 실행 한정 표시, 대화상자 초점 복귀를 보완했다.
- 한글 표시 누락을 수정했다. 공식 Noto Sans KR의 한글 음절 11,172자를 포함한 WOFF2를 내장했다. 라이선스도 HTML에 포함했다.

## 검증 결과

| 검증 | 결과 | 근거 |
|---|---|---|
| 신규 흐름·오류·취소·재시도 | 19/19 통과 | `verification/calm-coach/flow-results.json` |
| 정의된 버튼 action 실행 | 27/27 UI 클릭으로 실행 | 같은 JSON의 actionInventory/exercisedActions, C19 |
| 화면 폭 | 8종 × 4개 폭 = 32개 조합, 가로 넘침 없음 | 320/390/768/1440px, 같은 JSON의 screens |
| 기존 회귀 | 9/9 통과 | `verification/calm-coach/aztks-followup-results.json` |
| 기존 30개 시나리오 | 수정 전·후 각각 30/30, 가중 합계 각각 132/132 | `verification/calm-coach/tf-results.json` |
| 오프라인 실행 | 검사 중 외부 요청 0, JavaScript 오류 0 | 신규·기존 회귀 결과 JSON |
| 한글 음절 | 11,172/11,172 cmap 포함 | `verification/calm-coach/font-coverage.json` |
| 원자료 보존 | CSV 4개·워크시트 2개가 시작 커밋과 바이트 동일. HTML 원본 데이터·BASE·AI 수치 동일 | `verification/calm-coach/summary.json` |
| JavaScript 문법·공백 | `node --check`, `git diff --check` exits 0 | 최종 확인 시 실행 |

32개 화면 조합의 넘침·제목 초점·필드 라벨을 검사하고 390/1440px 캡처 16개를 남겼다. 대표 캡처에서 실제 글자 표시, 주요 버튼 구분, 모바일 기록 목록·상담 입력창을 직접 확인했다. 모든 입력값 조합이나 모든 브라우저를 검사한 것은 아니다.

## 재실행

Node.js와 Playwright, Chromium을 준비한 뒤 프로젝트 폴더에서 실행한다. 이번 검증 도구와 누락 라이브러리는 `/tmp`에 준비했으므로 임시 파일 정리 후에는 해당 경로를 다시 준비하거나 환경 변수로 바꿔야 한다.

```bash
export PLAYWRIGHT_MODULE=/tmp/axyourbody-review-tools/node_modules/playwright
export CHROMIUM_PATH=/home/jung/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome
export LD_LIBRARY_PATH=/tmp/axyourbody-review-libs/root/usr/lib/x86_64-linux-gnu
node verification/calm-coach-flows.cjs
node verification/aztks-followup.cjs
```

기존 30개 시나리오 비교는 `BASELINE_HTML`에 수정 전 HTML을, `RESULT_FILE`에 결과 경로를 지정해 `verification/tf-30-simulations.cjs`를 실행한다. 이번 수정 전 기준은 시작 커밋 `e3ce86e`의 HTML이다. 기존 회귀 스크립트는 이전 경로에 캡처·JSON을 쓰므로 이번에는 결과를 `verification/calm-coach/`로 옮기고 과거 결과 파일을 원상 보존했다.

## 최종 보고 AZTKS 자체 검토

| 차원 | 등급 | 근거 |
|---|---|---|
| A 알아서 | ○ | 현재 화면 명세·실행 코드·사용자가 고른 시각 방향을 반영했다. 원본 자료와 예시를 보존했다. |
| Z 잘 | ○ | 신규 19개·기존 9개·기존 30개 검증을 각각 명시하고 캡처에서 글리프 문제를 발견해 수정했다. 시각적 선호와 실제 사용성은 미확정이다. |
| T 딱 | ○ | 7개 화면+입력창의 행동 목록을 점검하고 27개 action을 모두 UI로 실행했다. 범위 밖 메뉴는 비활성 상태로 명시했다. |
| K 깔끔 | ○ | 세부 관찰·행동 목록·증거를 문서로 분리하고 대화 보고는 핵심과 링크로 제한했다. |
| S 센스 | ○ | 로컬 수정은 자율 진행하고 원자료·사용자 결정권을 보존했다. 신규 서비스·배포·제출로 확장하지 않았다. |

이 평가는 산출물과 근거의 정합성을 확인한 자체 검토다. 독립 리뷰나 실제 사용자 평가 결과로 해석하지 않는다.

남은 제한: 실제 AI 연결·계정 동기화·운동 일지/목표/수면 신규 입력은 기존 범위 밖이다. 실제 사용자의 과업 이해도와 시각적 만족도는 미측정이다.

## 확인할 파일

- [실행 HTML](../20261126-정정훈-AXYOURBODY프로토타입.html)
- [목표·예산·자율성·지시문 검토](goals/calm-coach-flow.md)
- [관찰과 전체 조작 목록](calm-coach-review.md)
- [모바일 오늘 계획](../verification/calm-coach/390-today.png)
- [데스크톱 AI 제안](../verification/calm-coach/1440-ai.png)
