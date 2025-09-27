# Claude Code Configuration

This file contains configuration and preferences for Claude Code.

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