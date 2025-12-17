# Sample Prompts

아래 프롬프트는 “컨텍스트 주입”을 연습하기 위한 예시다. 그대로 복사해도 되고, 더 개선해도 된다.

## 1) 요약 + 위험요소 찾기

~~~text
먼저 아래 문서를 읽고, 작업 전에 위험요소(실수하기 쉬운 점)를 5개만 뽑아줘.

- labs/lab02_context/materials/PROJECT_BRIEF.md
- labs/lab02_context/materials/CONSTRAINTS.md
- labs/lab02_context/materials/GLOSSARY.md

그 다음 target_app/ 코드를 훑고,
정렬 규칙을 넣기 위한 변경 지점을 파일/함수 단위로 제안해줘.
~~~

## 2) 작업 단위 쪼개기

~~~text
정렬 규칙 구현을 3~5개의 작은 작업으로 쪼개고,
각 작업마다 “완료 조건”을 1줄로 적어줘.
그리고 가장 위험한 작업부터 먼저 하자.
~~~

## 3) 제약을 체크리스트로 고정

~~~text
아래 제약을 체크리스트로 만들고,
코드 변경 후에 각 항목을 통과했는지 스스로 검증해줘.

- 저장 포맷(JSON 스키마) 변경 금지
- CLI 명령/인자 의미 변경 금지
- 외부 라이브러리 추가 금지
~~~

