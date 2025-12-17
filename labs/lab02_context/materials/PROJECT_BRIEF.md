# Project Brief (Lab02)

`target_app`은 학습용 초소형 TODO CLI 앱이다.

이 앱은 의도적으로 “문서(요구사항/제약)”와 “코드”가 분리되어 있다.
Copilot이 코드를 바로 고치기 전에,
**반드시 문서를 먼저 읽도록 컨텍스트를 주입**하는 것이 이 실습의 핵심이다.

## 주요 기능

- `list` : TODO 목록 출력
- `add "<title>" --priority <1|2|3>` : TODO 추가
- `done <id>` : TODO 완료 처리

