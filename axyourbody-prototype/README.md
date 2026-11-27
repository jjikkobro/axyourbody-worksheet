# AX YOUR BODY 프로토타입

[공개 프로토타입](https://jjikkobro.github.io/axyourbody-worksheet/) · [스킬 기반 작업 과정](../README.md)

## 현재 기준

- [단일 HTML](20261126-정정훈-AXYOURBODY프로토타입.html): 브라우저에서 직접 실행할 수 있는 최종 프로토타입
- [제품 디자인 기준](design/DESIGN-axyourbody.md): 현재 HTML에서 추출한 색상·서체·배치·상태 표현
- [화면 명세](SCREEN_SPEC.md) · [행동 흐름](docs/action-flow.md)
- [최종 목표](docs/goals/calm-coach-flow.md) · [목표 재검토](docs/goals/calm-coach-flow-review.md)
- [최종 실행 보고](docs/calm-coach-flow-final-report.md) · [화면별 감사](docs/calm-coach-flow-audit.md)

## 근거와 이력

[기획 원본](../worksheet.md), `context/`의 서비스 구조와 화면 흐름, `data/`의 가상 CSV를 근거로 작성했습니다. `docs/grip/`에는 화면·지표 결정 7개, `docs/tf-review-30.md`에는 5개 역할 AI 에이전트의 내부 검토, `docs/aztks-improvements.md`에는 후속 개선이 남아 있습니다.

`design/DESIGN-calm-coach.md` 등 초기 참고 원문 3개는 외부 브랜드 패턴의 참고 자료입니다. 제품 수정에는 `DESIGN-axyourbody.md`를 우선합니다.

과거 보고의 `verification/` 실행 파일·JSON·캡처와 초기 Stitch 다운로드 시안은 정리되었습니다. 기록된 수치는 당시 내부 검사 결과이며 현재 배포 작업에서 전부 재실행한 결과가 아닙니다. 삭제한 추적 자료는 Git 이력에서 확인할 수 있습니다. 오래된 ZIP·초기 MANIFEST·중복 워크시트·중복 화면 흐름 사본도 제거했습니다.

## 실행 범위

폰트·아이콘·가상 데이터가 HTML에 포함되어 있습니다. 운동 상태와 계획 변경, 수행 기록·정정, 체성분 비교, 상담 저장·연결을 시연합니다. 실제 AI API, 계정, 서버 동기화 또는 의료 판단은 제공하지 않습니다. 사용자 입력은 브라우저 저장소에 저장되며, 로컬 파일과 Pages 사이트는 서로 다른 저장소를 사용합니다.

## 배포

루트의 `.github/workflows/pages.yml`과 `scripts/build-pages.py`가 GitHub Pages용 HTML·문서만 생성합니다. 상세 작업 과정과 재생성 명령은 [루트 README](../README.md)에 있습니다.
