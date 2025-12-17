# 01. Setup  
Copilot Coding Agent 시작하기

이 강의의 목표는 단 하나다.

> **“Copilot Coding Agent가 실제로 동작하는 상태”를 만드는 것**

여기까지 오면,
- Copilot이 설치되어 있고
- 채팅이 가능하며
- 간단한 작업을 실제로 수행하는 상태가 된다.

---

## 이 강의에서 할 일

이 강의에서는 다음을 수행한다.

- GitHub Copilot 기본 환경 확인
- VS Code에서 Copilot Agent 사용 준비
- Copilot에게 첫 작업 맡기기
- “아, 된다” 경험 만들기

---

## 사전 준비 사항

### 필수 조건

- GitHub 계정
- GitHub Copilot 사용 가능 상태
- Visual Studio Code 설치

> Copilot 플랜이나 UI는 시점에 따라 다를 수 있다.  
> 메뉴 위치가 조금 달라도 정상이다.

---

## Step 1. Copilot 확장 확인

VS Code에서 확장(Extensions)을 열고  
다음 항목이 설치되어 있는지 확인한다.

- GitHub Copilot
- GitHub Copilot Chat

설치되어 있다면 VS Code를 재시작한다.

---

## Step 2. Copilot Chat 열기

VS Code에서 Copilot Chat을 연다.

- 사이드바 Copilot 아이콘
- 또는 Command Palette에서 `Copilot` 검색

중요한 것은 **“대화가 가능한 상태”**다.

---

## Step 3. Copilot Agent에게 첫 작업 맡기기

이제 Copilot에게 아주 간단한 작업을 맡겨본다.

Copilot Chat에 다음을 입력해보자.

~~~text
이 프로젝트에 대해 간단히 설명해줘.
~~~

### 확인 포인트

- 현재 폴더 구조를 인식하는가?
- README.md를 참고하는가?

결과가 완벽하지 않아도 괜찮다.  
**응답이 나온다는 사실이 중요하다.**

---

## Step 4. 파일 생성 작업 시켜보기

이제 실제 파일 작업을 맡겨본다.

~~~text
README.md에
이 프로젝트가 무엇을 위한 저장소인지
간단한 설명을 추가해줘.
~~~

### 확인 포인트

- 파일 변경 제안을 하는가?
- 수정 내용을 요약해 주는가?

이 단계에서 Copilot은 이미  
**“자동완성”이 아니라 “작업 수행자”다.**

---

## Step 5. 잘못된 지시도 한 번 해보자

일부러 애매하게 요청해본다.

~~~text
이 프로젝트를 더 좋게 만들어줘.
~~~

관찰해보자.

- 수정 범위가 과도한가?
- 의도를 추측하는가?

👉 이 경험이 중요하다.  
앞으로 왜 **구체적인 지시가 필요한지** 체감하게 된다.

---

## 정리

이 강의가 끝났다면,

- Copilot이 정상 동작하고
- 파일 작업을 수행할 수 있으며
- 결과를 제안하는 상태가 되었다.

아직 대단한 건 하지 않았다.  
하지만 **가장 중요한 준비는 끝났다.**

---

## 다음 단계

👉 **02. Agent Mindset – Copilot을 대하는 관점 바꾸기**

이제 Copilot을  
“도와주는 도구”가 아니라  
“일을 맡길 대상”으로 바라보는 연습을 시작한다.
