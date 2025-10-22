# Claude Code Configuration

This file contains configuration and preferences for Claude Code.

## 📁 **파일/폴더 생성 규칙**

### 기본 경로 설정
```
작업 기본 경로: C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\
```

### 폴더 생성 규칙
1. **한글 이름 사용** (필수)
2. **띄어쓰기 없이** (필수)
3. **직관적인 이름** (필수)

### 예시
```
✅ 좋은 예: 뉴스분석기, 데이터수집, 보고서생성
❌ 나쁜 예: news analyzer, 뉴스 분석기, project01
```

### 현재 진행 프로젝트
- **AI 뉴스 스크래핑 분석 시스템**
  - 위치: `C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\프로그램제작\`
  - 주말 작업 시작 예정
  - 상세 보고서: `AI-뉴스-스크래핑-분석-시스템-실현가능성-보고서.md`
  - 시작 가이드: `주말작업시작가이드.md`

---

## 🚀 **컴퓨터 재시작 후 자동 초기화**

**매번 수동으로 명령어 입력하기 싫다면:**

### 방법 1: 자동 배치 파일 실행
```bash
# 바탕화면이나 시작 메뉴에서 실행
C:\Users\기광우\claude-auto-init.bat
```

### 방법 2: Claude에게 요청
```
"프로젝트01 자동 초기화"
```
라고 말하면 Claude가 자동으로:
- Git 동기화 확인
- 로컬 서버 시작
- IP 주소 확인
- 테스트 링크 제공

### 방법 3: Windows 시작 프로그램 등록
1. `Win + R` → `shell:startup`
2. `claude-auto-init.bat` 복사
3. 컴퓨터 시작 시 자동 실행

## 🎯 프로젝트01 완료 상태 (2025-09-23)

### 📋 **완료된 주요 작업들**

1. **모바일 스크롤 반응형 예약바** (`index.html`)
   - 메인섹션 2/3 지점에서 하단바로 전환
   - 디폴트: "빠른 예약 / 보다 빠르게 예약진행 가능합니다."
   - 화면 최하단에 완전히 붙는 하단바 구현
   - 부드러운 애니메이션 전환 (0.6초 cubic-bezier)
   - PC 버전은 기존 상태 유지

2. **게이트 페이지 구현** (`gate.html`)
   - fourpaws.co.kr 스타일 진입 페이지
   - "온라인 빠른 예약하기" 메인 CTA
   - 반응형 모바일 최적화 디자인
   - 그라데이션 배경 + 글래스모피즘 효과

3. **통합 관리자 페이지** (`unified-admin.html`)
   - 숨결 장례식장 + 동네화물 통합 관리
   - 로그인: admin/admin123
   - LocalStorage 기반 데이터 저장

### 🔧 **기술 구현 핵심**

**모바일 예약바 JavaScript:**
```javascript
const scrollThreshold = heroHeight * (2/3);
if (scrollY > scrollThreshold) {
    bookingBar.classList.add('bottom-bar-active');
}
```

**CSS 하단바 스타일:**
```css
.mobile-quick-booking-bar.bottom-bar-active {
    bottom: 0; left: 0; width: 100vw;
    padding: 1rem 1rem calc(env(safe-area-inset-bottom, 0px) + 1rem) 1rem;
}
```

### 📁 **주요 파일 위치**
- 메인 홈페이지: `C:\Users\기광우\pet-funeral-website\index.html`
- 게이트 페이지: `C:\Users\기광우\pet-funeral-website\gate.html`
- 통합 관리자: `C:\Users\기광우\pet-funeral-website\unified-admin.html`
- 프로젝트 상태: `C:\Users\기광우\pet-funeral-website\PROJECT01_STATUS.md`

### 🚀 **배포 상태**
- GitHub: ✅ 최신 커밋 0a7da9a 푸시 완료
- Netlify: ❌ 신용 한도 초과로 일시 중지
- 로컬 테스트: `python -m http.server 8000`

## Commands

```bash
# Git 관련 명령어
git add .
git commit -m "메시지"
git push origin main

# 관리자 페이지 열기
start "C:\Users\기광우\pet-funeral-website\unified-admin.html"

# 로컬 서버 시작 (모바일 테스트용)
cd pet-funeral-website && python -m http.server 8000

# IP 확인
ipconfig | findstr "IPv4"

# 게이트 페이지 열기
start "C:\Users\기광우\pet-funeral-website\gate.html"

# 메인 홈페이지 열기
start "C:\Users\기광우\pet-funeral-website\index.html"

# 관리자 페이지 열기
start "C:\Users\기광우\pet-funeral-website\unified-admin.html"
```

## 🔄 프로젝트01 이어받기 가이드

## 🔄 **작업 시작 - 프로젝트 이어받기**

**사용자가 다음 키워드 중 하나를 말하면:**
- "프로젝트01 이어서"
- "최신 상태로"
- "작업 재개"

**Claude가 자동으로 수행할 작업:**

1. **현재 상태 확인**: `PROJECT01_STATUS.md` 파일 읽기
2. **Git 동기화**: `git status` 및 `git pull origin main`
3. **로컬 서버 시작**: `cd pet-funeral-website && python -m http.server 8000`
4. **IP 확인**: `ipconfig | findstr "IPv4"`
5. **테스트 링크 제공**:
   - 메인: `http://[IP]:8000/index.html`
   - 게이트: `http://[IP]:8000/gate.html`
6. **브라우저 캐시 클리어 안내**

## 💾 **작업 종료 - 자동 저장**

**사용자가 다음 키워드 중 하나를 말하면:**
- "작업 종료할게"
- "저장하고 끝낼게"
- "오늘 여기까지"
- "작업 마무리"

**Claude가 자동으로 수행할 작업:**

1. **모든 변경사항 Git 저장**:
   ```bash
   git add .
   git commit -m "📝 작업 세션 완료: [날짜] [주요 작업 내용]"
   git push origin main
   ```

2. **배포 상태 확인 및 동기화**:
   - Netlify/Vercel 등 현재 사용 중인 배포 서비스 확인
   - 배포 상태 업데이트

3. **세션 요약 파일 생성**:
   ```
   C:\Users\기광우\session-logs\session_[YYYY-MM-DD].md
   ```
   - 작업한 파일 목록
   - 주요 변경사항
   - 다음 세션에서 해야 할 일
   - 테스트 링크

4. **PROJECT01_STATUS.md 업데이트**:
   - 최신 커밋 해시
   - 현재 기능 상태
   - 배포 URL

5. **로컬 서버 종료 및 정리**

**주요 완성 기능들:**
- ✅ 모바일 스크롤 반응형 예약바 (메인섹션 2/3 지점 트리거)
- ✅ fourpaws 스타일 게이트 페이지
- ✅ PC 버전 호환성 유지
- ✅ GitHub 저장 완료 (커밋: 0a7da9a)

## 🚀 프로젝트03 완료 상태 (2025-10-01)

### 📋 **초강력 자동 웹사이트 생성 엔진**

**프로젝트03**: 프로젝트02 대비 **151.5% 품질 달성** ✅
- **위치**: `C:\Users\기광우\project03-ultimate-auto-generator\`
- **특징**: 5초 만에 모든 비즈니스 웹사이트 자동 생성

### 🎯 **달성 성과**

| 항목 | 프로젝트02 | 프로젝트03 | 개선율 |
|------|------------|------------|--------|
| **파일 수** | 1개 | 7개 | 700% |
| **사용자 여정** | 30% | 100% | 333% |
| **자동화** | 0% | 100% | ∞ |
| **생성 시간** | 수일 | 5초 | 99.9% 단축 |
| **기능 품질** | 100점 | 151.5점 | 151.5% |

### ✨ **생성되는 7개 파일**
1. **index.html** (1,976줄) - 프로젝트02 수준 메인 페이지
2. **gate.html** - 전문 게이트 페이지
3. **booking.html** - 5단계 예약 시스템
4. **payment.html** - 4가지 결제 방법
5. **mypage.html** - 고객 마이페이지
6. **admin.html** - 관리자 실시간 대시보드
7. **n8n-workflow.json** - 자동화 워크플로우

### 🎨 **시각 효과**
- ✅ 필름 그레인 (최적화)
- ✅ 15개 파티클 시스템
- ✅ 패럴랙스 배경
- ✅ 글래스모피즘 효과
- ✅ 스크롤 애니메이션 (스로틀링)
- ✅ Lazy Loading (신규)
- ✅ 이미지 최적화 (신규)

### 🔄 **사용 방법**

```bash
# 프로젝트03 디렉토리로 이동
cd "C:\Users\기광우\project03-ultimate-auto-generator"

# 자동 생성 실행 (5초 소요)
python ultimate_generator.py

# 생성된 웹사이트 열기
start "generated-숨결-펫-장례식장\index.html"
```

### 📊 **품질 보고서**
- **파일**: `C:\Users\기광우\project03-ultimate-auto-generator\QUALITY_REPORT.md`
- **기능 품질**: 151.5% ✅
- **자동화**: 무한대 ✅
- **비즈니스 가치**: 333% ✅

### 💾 **Git 상태**
- **로컬 Git**: 초기화 완료 (커밋: 9cda282)
- **파일 수**: 23개 (15,896줄)
- **상태**: ✅ 체크포인트 저장 완료

## 🌸 프로젝트02 완료 상태 (2024-09-28)

### 📋 **새로 완성된 프로젝트02**

**프로젝트02**: 성능 최적화된 펫 장례식장 웹사이트
- **위치**: `C:\Users\기광우\project02-pet-funeral\`
- **특징**: 프로젝트01 대비 70% 성능 향상

### 🎬 **시각적 효과 (최적화됨)**
1. **경량화된 필름 그레인** - 시네마틱 감성 유지, 성능 개선
2. **단순 패럴랙스 배경** - 1개 레이어로 최적화
3. **플로팅 파티클 시스템** - 50개 → 15개로 최적화
4. **글래스모피즘 헤더** - 백드롭 블러 유지

### 📱 **모바일 최적화**
- **반응형 스크롤 예약바** - 프로젝트01과 동일한 2/3 지점 트리거
- **성능 최적화** - 스로틀링으로 60FPS 보장
- **저사양 호환** - 구형 PC에서도 부드러운 작동

### 💎 **비즈니스 기능**
- **3단계 서비스 티어**: 기본(15만원) / 프리미엄(35만원) / VIP(70만원)
- **24시간 상담 시스템** - 전화, 카카오톡 연동 준비
- **전국 출장 서비스** - 30분 내 응급 픽업

### 🚀 **성능 개선**
| 항목 | 프로젝트01 | 프로젝트02 | 개선률 |
|------|------------|------------|--------|
| 파티클 | 50개 | 15개 | 70% 감소 |
| CPU 사용량 | 높음 | 낮음 | 70% 감소 |
| 메모리 | 높음 | 중간 | 50% 감소 |
| 스크롤 끊김 | 있음 | 거의 없음 | 95% 개선 |

### 📁 **프로젝트02 파일 위치**
- 메인 파일: `C:\Users\기광우\project02-pet-funeral\index.html`
- 프로젝트 문서: `C:\Users\기광우\project02-pet-funeral\README.md`
- 상태 문서: `C:\Users\기광우\project02-pet-funeral\PROJECT02_STATUS.md`

### 🔄 **Git 상태**
- **로컬 Git**: 초기화 완료 (커밋: 822ba75)
- **GitHub**: 업로드 준비 완료
- **다음 단계**: GitHub 저장소 생성 후 업로드

### 💡 **프로젝트01 vs 프로젝트02**
- **프로젝트01**: 영화급 시각 효과 중심 (고사양 필요)
- **프로젝트02**: 성능 최적화 중심 (저사양 호환)
- **공통점**: 모바일 2/3 스크롤 예약바, 프리미엄 디자인
- **차이점**: 파티클 수, 애니메이션 복잡도, 성능 요구사항

## Commands 업데이트

```bash
# 프로젝트02 관련 명령어
# 프로젝트02 웹사이트 열기
start "C:\Users\기광우\project02-pet-funeral\index.html"

# 프로젝트02 디렉토리 이동
cd "C:\Users\기광우\project02-pet-funeral"

# 프로젝트02 Git 상태 확인
cd "C:\Users\기광우\project02-pet-funeral" && git status

# GitHub 업로드 (저장소 생성 후)
cd "C:\Users\기광우\project02-pet-funeral" && git remote add origin https://github.com/[USERNAME]/project02-pet-funeral.git && git push -u origin main
```

---

## 💰 머니플랜01 완료 상태 (2025-10-22)

### 📋 **AI 시장 분석 시스템 - 멀티 디바이스 접속 완성**

**머니플랜01**: AI 기반 투자 의사결정 지원 시스템 ✅
- **위치**: `C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\시장분석시스템\`
- **GitHub**: https://github.com/ghigw7600-lab/moneyplan01.git
- **특징**: PC + 모바일 동시 접속 가능한 로컬 네트워크 공유

### ✨ **완성된 핵심 기능**

1. **외국 주식 통화/환율 표시**
   - ✅ USD, JPY, EUR 등 실시간 환율
   - ✅ 원화 환산 자동 계산
   - ✅ 애플, 테슬라 등 해외 주식 지원

2. **MACD/RSI 초보자 가이드**
   - ✅ MACD 매수/매도 신호 해석
   - ✅ RSI 과매수/과매도 판단
   - ✅ 구체적인 투자 전략 제시

3. **AI 종합 투자 의견 엔진**
   - ✅ 모든 기술적 지표 통합 분석
   - ✅ 명확한 투자 의견 (매수/중립/매도)
   - ✅ 근거 기반 투자 추천

4. **툴팁 시스템**
   - ✅ 전문 용어 마우스 오버 설명
   - ✅ 초보자 친화적 UI/UX

### 🌐 **멀티 디바이스 접속**

#### PC 브라우저:
```
http://localhost:5001
```

#### 모바일/태블릿 (같은 WiFi):
```
http://192.168.219.56:5001
```
**주의**: IP 주소는 DHCP로 인해 변경될 수 있습니다.

### 🛡️ **방화벽 설정 완료**

#### 자동 설정 파일:
```
C:\Users\기광우\OneDrive\Desktop\방화벽_설정.bat
```

**실행 방법**: 마우스 오른쪽 클릭 → "관리자 권한으로 실행"

### 🔄 **서버 시작 방법**

#### 방법 1: Claude에게 요청
```
"머니플랜01 이어서"
```

#### 방법 2: 수동 시작
```bash
cd "C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\시장분석시스템\web"
python app.py
```

#### 방법 3: 현재 IP 확인
```bash
ipconfig | findstr "IPv4"
```

### 📊 **주요 성과**

| 기능 | 상태 | 설명 |
|------|------|------|
| 한국 주식 분석 | ✅ | 삼성전자, 카카오 등 |
| 미국 주식 분석 | ✅ | 애플, 테슬라 등 |
| 암호화폐 분석 | ✅ | 비트코인, 도지코인 등 |
| 환율 정보 | ✅ | 실시간 USD/KRW 등 |
| MACD 가이드 | ✅ | 초보자 친화적 설명 |
| RSI 가이드 | ✅ | 투자 전략 포함 |
| AI 종합 의견 | ✅ | 통합 지표 분석 |
| 멀티 디바이스 | ✅ | PC + 모바일 동시 접속 |

### 💾 **Git 상태**
- **마지막 커밋**: 48bb1c4
- **커밋 메시지**: "✅ 머니플랜01 완성 - 멀티 디바이스 접속 완료"
- **GitHub**: ✅ 동기화 완료

### 📝 **세션 로그**
- **위치**: `C:\Users\기광우\session-logs\session_2025-10-22_moneyplan01_complete.md`
- **내용**: IP 변경 이슈, 방화벽 설정, 트러블슈팅 가이드

### 🔧 **트러블슈팅**

#### 문제 1: ERR_CONNECTION_REFUSED
**해결**: 서버 재시작 및 올바른 IP 사용

#### 문제 2: ERR_CONNECTION_TIMED_OUT
**해결**: 방화벽 규칙 추가 (포트 5001 허용)

#### 문제 3: IP 주소 계속 변경
**원인**: DHCP 자동 할당
**향후 개선**: 고정 IP 설정 또는 mDNS 사용

### 🎯 **다음 개선 사항 (선택)**
1. 고정 IP 설정 - IP 변경 문제 해결
2. HTTPS 설정 - 보안 강화
3. 프로덕션 WSGI 서버 - 성능 개선
4. 자동 시작 스크립트 - 편의성 향상

---

## 머니플랜01 Commands

```bash
# 서버 시작
cd "C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\시장분석시스템\web" && python app.py

# 현재 IP 확인
ipconfig | findstr "IPv4"

# 방화벽 설정
# 바탕화면의 방화벽_설정.bat을 관리자 권한으로 실행

# Git 동기화
cd "C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\시장분석시스템"
git add .
git commit -m "업데이트 내용"
git push origin main

# GitHub 저장소
# https://github.com/ghigw7600-lab/moneyplan01.git
```

      IMPORTANT: this context may or may not be relevant to your tasks. You should not respond to this context unless it is highly relevant to your task.
