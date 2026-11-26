# AX YOUR BODY · 시안 제작 자료 묶음

2026-11-26 · 가상 프로필 m-athlete · 핵심 과업 1~3

## 실행할 파일

[20261126-정정훈-AXYOURBODY프로토타입.html](20261126-정정훈-AXYOURBODY프로토타입.html)을 브라우저에서 직접 엽니다. Clear Guidance 기준의 반응형 단일 파일이며, 폰트·아이콘·가상 원본 데이터가 포함되어 네트워크 없이 동작합니다.

검증 결과와 한계는 [standalone-handoff.md](docs/standalone-handoff.md), 5인 TF의 30개 시나리오 비교는 [tf-review-30.md](docs/tf-review-30.md)를 확인합니다.

최신 개선·검증 내역: [AZTKS 검토 후 개선](docs/aztks-improvements.md).

## 먼저 읽을 파일

1. [서비스 구조 설명서](context/service-structure.md)
2. [공통 화면 명세 SCREEN_SPEC.md](SCREEN_SPEC.md)
3. [과업 1 화면 흐름·상태](context/screen-flow.md)
4. [테마 적용·비교 기준](docs/theme-application.md)
5. 사용할 테마의 design/DESIGN-*.md 한 개

## 구성

- SCREEN_SPEC.md: 필수 화면 7개·부수 제안 1개, 흐름·필수 동작·데이터·지표·상태와 미정 사항.
- context/service-structure.md: 워크시트의 1~8번 서비스 구조 설명서 코드 블록을 그대로 분리.
- context/screen-flow.md: 과업 1의 3개 화면과 상태 4종. 과업 2·3은 SCREEN_SPEC.md 참조.
- worksheet.md: 현재 워크시트 전체 스냅샷. 과업 4~7은 이번 필수 구현 범위가 아님.
- docs/grip/GRIP_REGISTER.md: 화면·지표 결정 7개와 근거.
- docs/persona-source.md: 교재의 m-athlete 가상 프로필 원문과 출처.
- design/: getdesign.md Oura·NerdWallet·Linear 디자인 원문 3개와 SOURCES.md.
- docs/theme-application.md: 테마 파일 대응·적용 제안·비교 양식.
- data/: m-athlete 가상 CSV 4개와 출처. 실제 운동 계획·상담 원문은 없음.
- references/: 화면 흐름 워크시트 HTML과 사용자 제공 원본 SVG. 앱 자체의 프로토타입이 아님.
- MANIFEST.json: 초기 자료 묶음 20개 파일의 SHA-256과 출처를 검증하기 위한 당시 목록. 현재 전체 파일의 목록은 아님.

## 현재 상태

화면·지표 7개 결정과 Clear Guidance 기준의 필수 화면 7개, 부수 상담 입력을 단일 HTML에 구현했다. 5개 역할의 AI 에이전트가 제안한 30개 시나리오를 오프라인 Chromium에서 기존안·개선안에 실행했고, 개선안이 내부 가중 평가에서 최고 점수였다. 실제 사용자 대상 사용성 테스트나 Figma 반영 결과는 아니다.
Stitch에서 받은 과업 1의 세 테마 원본은 stitch-review/에 보존했다.

이 ZIP은 로컬 전달용 자료 묶음이며 저장소·게시 사이트·메일·외부 서비스에 자동 업로드하지 않는다.
