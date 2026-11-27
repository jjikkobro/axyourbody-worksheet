# 오늘 운동 흐름 수용 감사

> 이 문서는 당시 검토·실행 이력입니다. 과거 verification 실행 자료와 Stitch 다운로드 시안은 2026-11-27 정리되어 본문의 옛 경로는 현재 재실행·열람 경로가 아닙니다. 삭제한 추적 파일은 Git 이력에서 확인할 수 있습니다.

실행 기준: `verification/calm-coach-goal-b2ddz24c/baseline/manifest.json`.
시작 시 미커밋 변경을 포함한 HTML, 전체 파일 해시, 기존 검사 산출물을 보존했다.
최종 판정과 실행 해시는 [최종 보고](calm-coach-flow-final-report.md)와 실행 폴더의 evidence.json을 따른다. 아래 UI01~UI20은 새 수용 검사와 기존 회귀·화면 검사에 연결했다.

## 재현과 수정 결정

| ID | 관찰 및 사용자 영향 | 수정 결정·대안 | 증거 | 상태 |
|---|---|---|---|---|
| F01 | 시작 후 몸 상태는 편집할 수 있으나 저장 CTA 없음 | 몸 상태 전용 저장/취소 추가. 시작 기준 계획과 수행 객체는 그대로 보존 | baseline/acceptance-corrected → progress-1 AC12 | PASS |
| F02 | 손상 workout 내부 행 및 변경 이력 검증 미비, 변경 이력으로 화면 오류 발생 | 객체별 검증과 정상 자료 유지. 전체 초기화 대신 손상 영역만 분리하고 원문 별도 저장 | 같은 경로 AC15 3개 | PASS |
| F03 | 상담 모달의 입력이 beforeunload 경고 대상에서 빠짐 | 폼 초기값과 현재값 비교를 공통 미저장 판정에 포함 | 같은 경로 AC16 | PASS · 실제 새로고침 거절/입력 유지까지 확인 |
| F04 | 상담 연결 후 해제 행동 없음 | 해제 확인·오류·기존 원문 보존 구현. 삭제 대신 연결만 제거 | 같은 경로 AC18 | PASS |
| F05 | 실제 수행값 오류 시 오류 박스만 초점, 입력과 오류 연결 없음 | 해당 입력에 초점, aria-invalid/describedby 연결 | 같은 경로 AC07 | PASS |
| F06 | 쓰기 장애가 한 번 발생하면 이후에도 영속 저장 재시도 안 함 | 저장 시 재시도하여 복구되면 영속 상태로 표시 | progress-3 AC14 | PASS |
| F07 | 미실행 모달 ‘돌아가기’가 폼 submit 기본 동작까지 실행해 미실행 기록 저장 | 공통 일반 버튼에 type=button. 실제 제출 버튼은 submit 유지 | progress-3 AC10 실패 → progress-4 | PASS · progress-4 이후 취소 시 저장 없음 |
| F08 | 같은 화면의 주요 CTA와 동일 강조 버튼이 경쟁, 수행 초안 상태 안내 부족 | 계획 카드/보조 저장 강조 절제. 미확인·수행 저장 경계 표시 | 화면 검토 예정 | PASS · 110개 화면 조합 및 캡처 검토 |

검사 작성 중 상담/체성분 버튼 이름과 상대 파일 URL을 잘못 지정한 실행은 검사 설정 오류로 구분했다. `baseline/acceptance-corrected`의 최종 결과가 수정 전 재현 근거이며, 이전 잘못된 선택자/URL 실패를 제품 결함으로 세지 않는다.

## 화면·상태별 행동 목록

각 행의 세부 버튼은 다음 절의 action 목록 및 비버튼 목록으로 추적한다. 증거의 경로 기준은 실행 폴더다. `대기`는 PASS가 아니다.

| ID | 진입 조건 | 보이는 상태 | 주요 CTA | 편집 대상 | 저장 범위 | 다음 상태 | 취소·오류 복구 | AC / 증거 | 판정 |
|---|---|---|---|---|---|---|---|---|---|
| UI01 | 저장 없음 / plans | 운동 여부 미확인 | 오늘 계획 정하기 | 없음 | 없음 | today | 사후 기록·미실행 경로 | AC01 / progress-3 | PASS |
| UI02 | today 미저장·수정 중 | 저장 전 변경 | 계획 저장하고 다음 단계로 | 수치·몸 상태·메모·이유 | 오늘 계획 | 저장된 계획 | 편집 취소·이탈 선택·재시도 | AC02~04 | PASS |
| UI03 | today 저장됨 | 시작 전 | 운동 시작하기 | 계획 | workout 기준 스냅샷 | active | 오류 후 시작 재시도 | AC05·13 | PASS |
| UI04 | AI 기본/로딩/오류 | 고정 시연 제안 | 제안 적용 | 계획 초안 | 저장 전에는 없음 | today 편집 | 저장 계획 유지·직접 편집·뒤로 | AC03 / 기존 회귀 | PASS |
| UI05 | workout active | 운동 중 | 운동 마치기 | 실제 수행·시간·메모 | 임시 수행 또는 종료 상태 | ended | 임시 저장·미실행·오류 재시도 | AC06~08·13 | PASS |
| UI06 | workout logging | 수행 내용 작성 중 | 운동 일지 저장하기 | 사후 수행 | 수행 기록 | done | 임시 저장·미실행·이탈 | AC09 | PASS |
| UI07 | workout ended | 종료·최종 저장 전 | 운동 일지 저장하기 | 수행 확인/수정 | 최종 일지 | done | 저장 오류·임시 저장 | AC08·13 | PASS |
| UI08 | workout done | 운동했어요 | 수행 기록 수정하기 | 수행 초안 | 수행 기록만 | done | 수정 취소·이탈·오류 | AC11 | PASS |
| UI09 | skip 모달 | 운동 안 했어요 확인 | 미실행 일지 저장 | 선택 이유 | 운동 여부 | skipped | 돌아가기·닫기·Escape·오류 재시도 | AC10·13·16 | PASS |
| UI10 | workout skipped | 운동 안 했어요 | 기록 바로잡기 | 정정 초안 | 확정 전 기존 미실행 유지 | logging→done | 정정 취소 | AC10 | PASS |
| UI11 | 시작 후 today/AI | 기준 계획 보존 | 실제 수행값 확인 | 몸 상태만 | 몸 상태만 | 저장 또는 취소 | 계획 잠금·일지 이동 | AC12 | PASS |
| UI12 | log | 이번 일지/원본 구분 | 현재 상태에 맞는 행동 | 없음 | 없음 | workout/원본 상세 | 목록 복귀 | AC20 | PASS |
| UI13 | 원본 운동 상세 | 읽기 전용 | 오늘 계획/일지 보기 | 없음 | 없음 | today/workout | 뒤로 | AC20 | PASS |
| UI14 | 체성분 목록/빈 결과 | 조건별 측정 자료 | 기록 상세/필터 초기화 | 조회 조건 | 저장 안 함 | 상세/목록 | 필터 해제 | AC17 | PASS |
| UI15 | 체성분 상세/오류 | 원값·포함 상태 | 체성분 기록 저장 | 추세 포함 설정 | inclusion만 | 목록 | 이탈 거절/수락·재시도 | AC17·16 | PASS |
| UI16 | 상담 목록/빈 결과 | 가상 예시/사용자 원문 | 상담 내용 남기기 | 검색·상대 필터 | 저장 안 함 | 작성/상세 | 검색 해제·목록 복귀 | AC18 | PASS |
| UI17 | 상담 작성 모달/오류 | 저장 전 원문 | 상담 내용 저장 | 주제·날짜·상대·질문·답변·결론 | 상담만 | 상세 | 취소·Escape·재시도·이탈 | AC16·18 | PASS |
| UI18 | 상담 상세/연결됨/오류 | 원문 및 연결 상태 | 연결/해제 | planId | 상담 연결만 | 상세 | 선택 이탈·해제 확인·재시도 | AC18 | PASS |
| UI19 | 저장 거부/손상 | 이번 실행만/복구 안내 | 원래 과업 저장 재시도 | 해당 과업 | 정상 자료 보존 | 저장/세션 한정 | 손상 원문 보존 실패 시 덮어쓰기 차단 | AC14·15 | PASS |
| UI20 | 데이터 안내/수면 누락/목표 메뉴 | 시연 범위 | 안내 닫기/현재 과업 계속 | 없음 | 없음 | 원래 화면 | 닫기 초점 복귀 | AC19·20 | PASS |

## 비버튼 조작과 추가 검증 큐

- 계획: 날짜/상태/검색 필터, 세 수치 입력, 변경 이유, 몸 상태 1~5·해제·메모.
- 수행: 수행 체크, 행별 계획값 복사, 실제 수치·시간·메모.
- 체성분: 측정 조건/포함 여부/날짜 구간, 기록 선택, 추세 포함 체크.
- 상담: 검색/상대 필터, 기록 선택, 폼 입력/제출, 계획 선택.
- 공통: 내비게이션·뒤로·details 상태 시연·닫기·Escape·Tab/Shift+Tab/Enter/Space·초점 복귀·새로고침·IME.
- 위 추가 검증 큐는 최종 수용 28개·기존 회귀 17/19/9/30개·화면 조합 110개로 확인했다. 새로운 사용자 실험은 수행하지 않았다.

## 최종 수용 기준과 증거 연결

모든 경로는 `verification/calm-coach-goal-b2ddz24c/` 기준이다. A=final/acceptance/acceptance.json, L=final/lifecycle/lifecycle-results.json, C=final/calm/flow-results.json, F=final/followup/aztks-followup-results.json, T=final/tf.json, S=final/screens/screens.json. 각 결과의 개별 passed와 최종 HTML 해시를 확인한다.

| 기준 | 자동 증거 및 보완 관찰 | 판정 |
|---|---|---|
| AC01 | A 처음 진입, L01, S plans/today 첫 화면 | PASS |
| AC02 | A 계획 전후·취소·저장, L02, S plan-edit | PASS |
| AC03 | A 몸 상태·AI 초안, C03/C09/C10, T Q01 | PASS |
| AC04 | A 이탈 거절/수락·직접 기록 저장/폐기, C08, L16 | PASS |
| AC05 | A 시작/재진입, L03 기준 스냅샷·미수행 | PASS |
| AC06 | A 부분 임시 저장/재방문, L03 | PASS |
| AC07 | A 오류 입력 초점, L04/L17, C07 | PASS |
| AC08 | A 종료/최종 저장 분리·요약, L04 | PASS |
| AC09 | A 사후 수행·시간 미상, L07 | PASS |
| AC10 | A 미실행 취소/정정/정정 취소, L06/L09 | PASS |
| AC11 | A 수행 수정·취소·재방문·저장 성공 문구 제거, L05 | PASS |
| AC12 | A 시작 후 몸 상태 저장/취소·기준 보존, L08 | PASS |
| AC13 | A 종료 오류 재시도, L10/L11 시작·임시·최종·미실행 오류 | PASS |
| AC14 | A 쓰기 복구·읽기 실패 기존값 보존, L13, C15/C18, F | PASS |
| AC15 | A 구버전·손상 JSON·내부 행·이력·상태·수치·시각·보존 실패 | PASS |
| AC16 | A 상담 실제 새로고침 거절/입력 유지, C03/C04/C08/C11/C13, L12 | PASS |
| AC17 | A 원측정 보존, C04/C05, F 필터와 요약 일치·빈 결과 | PASS |
| AC18 | A 연결/해제/취소/오류, C11~C16, T IME·복귀·출처 | PASS |
| AC19 | A 키보드 활성화/체크/순환/복귀, C17, T A01~A06, S 110조합·캡처 검토 | PASS |
| AC20 | A 원본/범위 구분, C01/C02/C10/C12, T D01~D06, 문구·시각 검토 | PASS |

## 모든 명명된 행동

정의된 action 47개를 UI 클릭으로 실행한 증거는 [action-inventory.json](../verification/calm-coach-goal-b2ddz24c/action-inventory.json)에 저장했다. 클릭 집계는 범위 누락 검사용이며 의미 검증은 위 AC 매핑으로 판정한다. 폼 제출·필터·날짜·체크박스·키보드는 action 수에 넣지 않고 UI01~UI20과 비버튼 목록에서 검증한다.

| action | 보이는 이름 | 클릭 증거 묶음 |
|---|---|---|
| retry-workout-start | 조건부 조작 · 해당 결과의 테스트 참조 | lifecycle |
| retry-workout-save | 다시 저장하기 | lifecycle, acceptance |
| retry-skip | 조건부 조작 · 해당 결과의 테스트 참조 | lifecycle |
| review-today | 오늘 계획 보고 운동 시작하기 / 오늘 계획 정하기 | lifecycle, acceptance |
| save-and-review | 계획 변경 저장하기 / 계획 저장하고 다음 단계로 | calm, lifecycle, acceptance |
| discard-plan-changes | 계획 변경 버리기 | acceptance |
| save-condition | 몸 상태 저장하기 | acceptance |
| cancel-condition | 몸 상태 수정 취소 | acceptance |
| start-workout | 운동 시작하기 | lifecycle, acceptance |
| record-performed | 이미 한 운동 남기기 | lifecycle, acceptance |
| view-workout | 오늘 운동 일지 확인하기 / 이어서 수행값 입력하기 | lifecycle, acceptance |
| fill-workout-row | 계획대로 했어요 · 수행값 채우기 | lifecycle, acceptance |
| save-workout-draft | 수행 내용 임시 저장하기 | lifecycle, acceptance |
| finish-workout | 운동 마치기 | lifecycle, acceptance |
| save-workout-final | 운동 일지 저장하기 | lifecycle, acceptance |
| edit-workout-log | 수행 기록 수정하기 | lifecycle, acceptance |
| cancel-workout-edit | 기록 수정 취소 | lifecycle, acceptance |
| correct-skipped | 운동했어요 · 기록 바로잡기 | lifecycle, acceptance |
| skip-workout | 오늘 운동 안 했어요 | lifecycle, acceptance |
| view-source-workout | 2026. 10. 29웨이트프론트스쿼트 · 힙스러스트 · 노르딕 컬3개 종목 | lifecycle, acceptance |
| finish-loading | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| open-today | 오늘 계획 확인하기 | calm, lifecycle, acceptance |
| back-today | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| back-consults | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| open-ai | AI가 제안한 운동 계획 보기 | calm, lifecycle, acceptance |
| open-body | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| reset-plan | 필터 초기화 | calm |
| reset-body | 초기화 | calm |
| reset-consult | 초기화 | calm |
| toggle-edit | 운동 계획 바꾸기 | calm, lifecycle, acceptance |
| cancel-edit | 이번 수치 편집 취소 | calm, lifecycle, acceptance |
| clear-condition | 몸 상태 선택 해제 | calm |
| save-plan | 선택한 계획 저장하기 | calm, acceptance |
| retry-plan | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| ai-apply | 제안을 초안으로 가져오기 | calm, acceptance |
| ai-keep | 저장된 계획 유지하기 | calm |
| ai-direct | 직접 변경하기 | calm |
| retry-body | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| save-body | 체성분 기록 저장하기 | calm, acceptance |
| load-samples | 가상 상담 예시 불러오기 | calm, acceptance |
| unlink-consult | 계획 연결 해제하기 | acceptance |
| retry-link | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| link-consult | 선택한 계획에 연결하기 | calm, acceptance |
| new-consult | 상담 내용 남기기 / 상담 내용 직접 남기기 | calm, acceptance |
| sleep-input | 조건부 조작 · 해당 결과의 테스트 참조 | calm |
| close-dialog | 닫기 / 돌아가기 / 취소 | calm, acceptance |
| info | 데이터·저장 안내 / 데이터·저장 안내 열기 | calm |

## 문구와 시각 자체 검토

- 최초 진입의 같은 단계 나열을 반복하던 설명을 ‘운동 전/이미 한 운동’의 실제 선택 설명으로 바꿨다. 단계 표시는 한 번 유지했다.
- 계획 목록의 두 주요 강조를 다음 행동 하나로 정리하고 상세 열기는 보조 강조로 뒀다.
- 완료 일지 수정 시 이전 성공 안내가 계속 남지 않게 했다. 입력 후에는 저장 전 변경 상태를 표시한다.
- 몸 상태 저장이 막힌 상태를 ‘기능 준비 중’으로 처리하지 않고 전용 저장/취소와 영향 설명을 제공했다.
- 미실행 취소가 제출되던 오류는 일반 버튼의 type=button으로 수정했다.
- 본문·입력값 대비, 입력 경계, 도움말/시연 조작 크기, 첫 화면 CTA, 200% 확대를 확인했다. 작은 글자로 안내를 감추거나 출처를 삭제하지 않았다.
- 실제 사용자 이해도는 미측정이다. 본 검토는 에이전트의 캡처·동작 검토이며 독립 평가가 아니다.
