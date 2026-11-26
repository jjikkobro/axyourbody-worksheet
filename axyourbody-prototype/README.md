# AX YOUR BODY · 시안 제작 자료 묶음

2026-11-26 · 가상 프로필 m-athlete · 핵심 과업 1~3

## 실행할 파일

[prototype-merged.html](prototype-merged.html)을 브라우저에서 직접 엽니다. Clear Guidance 기준의 반응형 단일 파일이며, 폰트·아이콘·가상 원본 데이터가 포함되어 네트워크 없이 동작합니다.

검증 결과와 한계는 [standalone-handoff.md](docs/standalone-handoff.md)를 확인합니다.

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
- MANIFEST.json: 파일별 SHA-256과 출처를 검증하기 위한 목록.

## 작업 시작 지시문

context/service-structure.md, SCREEN_SPEC.md, context/screen-flow.md를 먼저 읽어 주세요.
핵심 과업 1~3에 대해 배치안 2~3개를 제시해 주세요. 파일은 아직 만들지 마세요.
배치안별 필수 7개 화면의 영역·정보·요소 유형·필수 동작을 표로 보여 주세요.
확정 기준과 미정 사항을 구분하고, 계획·상담 샘플을 실제 기록처럼 만들지 마세요.
제가 배치를 정하면 각 테마의 디자인 파일 하나씩 적용해 별도 HTML 시안을 만듭니다.

## 현재 상태

화면·지표 7개 결정은 완료했다. SCREEN_SPEC.md의 세부 작성안·상태 제안·배치는 추가 검토 대상이다.
Stitch에서 받은 과업 1의 세 테마 원본은 stitch-review/에 보존했다. 현재 prototype-merged.html에 Clear Guidance 기준의 필수 화면 7개와 부수 상담 입력을 연결했다. 실제 사용자 대상 사용성 테스트와 Figma 반영은 완료하지 않았다.
references/02-screen-flow-1.html은 문서 구조 검사만 했으며 브라우저 시각 검증은 시스템 라이브러리 부재로 미실시다.

이 ZIP은 로컬 전달용 자료 묶음이며 저장소·게시 사이트·메일·외부 서비스에 자동 업로드하지 않는다.
