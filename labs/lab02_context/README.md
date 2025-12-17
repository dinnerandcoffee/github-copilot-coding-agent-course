# Lab 02. Context Injection 심화

이 실습은 “컨텍스트를 얼마나 잘 주입하느냐”에 따라 Copilot 결과가 크게 달라지는 상황을 의도적으로 만든다.

---

## 목표

- Copilot이 **먼저 읽어야 할 문서/폴더**를 명확히 지정한다
- “하면 안 되는 것(제약)”을 컨텍스트로 고정한다
- 애매한 요구사항을 **질문으로 수렴**시키고, 작업 단위를 쪼갠다

---

## 실습 구성

- `materials/` : 프로젝트 목적/제약/용어집 (컨텍스트 주입 재료)
- `target_app/` : 수정 대상 미니 코드베이스

---

## Step 1. 컨텍스트 주입(필수)

Copilot에게 아래 파일을 먼저 읽고 요약하게 한다.

~~~text
다음 파일을 먼저 읽고 프로젝트를 요약해줘.

- labs/lab02_context/materials/PROJECT_BRIEF.md
- labs/lab02_context/materials/CONSTRAINTS.md
- labs/lab02_context/materials/GLOSSARY.md

그리고 target_app/ 폴더 구조를 보고,
각 파일의 역할을 1줄씩 설명해줘.
~~~

---

## Step 2. “하지 말아야 할 것”을 못 박기(필수)

~~~text
작업 전에 제약을 다시 확인하자.

- storage 포맷(JSON 스키마)은 바꾸지 마
- CLI 명령 이름은 바꾸지 마
- 외부 라이브러리 추가하지 마

이 제약을 지키면서 아래 작업을 진행해줘.
~~~

---

## Step 3. 과제: 정렬 규칙 추가

`target_app`은 TODO 목록을 출력할 때 입력 순서대로 보여준다.
아래 정렬 규칙을 추가하자.

1) 완료되지 않은 항목 먼저  
2) `priority`가 높은 것 먼저 (3 > 2 > 1)  
3) `created_at`이 빠른 것 먼저

### 완료 조건

- `python3 labs/lab02_context/target_app/main.py list` 실행 시 정렬 규칙이 적용된다
- `materials/CONSTRAINTS.md`의 제약을 모두 준수한다

---

## Step 4. 과제: “최소 컨텍스트” 버전 만들기(선택)

Copilot이 실수하기 쉬운 포인트를 최소 컨텍스트로도 해결하게 만들려면,
어떤 정보를 더/덜 제공해야 하는지 프롬프트를 개선해본다.

힌트: `materials/SAMPLE_PROMPTS.md`를 참고한다.

