# Claude Code Configuration

This file contains configuration and preferences for Claude Code.

## Current Session State (2025-09-21)

### 📋 **완료된 주요 작업들**

1. **통합 관리자 페이지 구현** (`unified-admin.html`)
   - 숨결 장례식장 + 동네화물 통합 관리
   - 로그인: admin/admin123
   - 로그인 상태 유지 기능 추가 (LocalStorage 기반)
   - 실시간 데이터 동기화 (3초마다 자동 새로고침)

2. **장례 홈페이지 개선** (`index_FOREST_TEST.html`)
   - 지점선택란 제거 (예약 폼 간소화)
   - 서브메뉴가 위로 나타나도록 수정
   - 관리자 페이지와 실시간 연동 구현

3. **화물 운송 사이트 연동** (`freight-delivery-website/index.html`)
   - 관리자 페이지와 예약 데이터 동기화
   - LocalStorage 기반 데이터 저장

### 🔗 **데이터 연동 시스템**
- **저장 방식**: LocalStorage 기반
- **실시간 동기화**: 3초마다 자동 업데이트
- **데이터 타입**:
  - `funeralBookings` (장례 예약)
  - `funeralInquiries` (장례 문의)
  - `freightOrders` (화물 주문)
  - `freightInquiries` (화물 문의)

### 📁 **주요 파일 위치**
- 통합 관리자: `C:\Users\기광우\pet-funeral-website\unified-admin.html`
- 장례 홈페이지: `C:\Users\기광우\pet-funeral-website\index_FOREST_TEST.html`
- 화물 사이트: `C:\Users\기광우\freight-delivery-website\index.html`

### 🚀 **배포 상태**
- GitHub 연동 필요
- Netlify 자동 배포 설정 확인 필요

## Commands

```bash
# Git 관련 명령어
git add .
git commit -m "메시지"
git push origin main

# 관리자 페이지 열기
start "C:\Users\기광우\pet-funeral-website\unified-admin.html"

# 장례 홈페이지 열기
start "C:\Users\기광우\pet-funeral-website\index_FOREST_TEST.html"

# 화물 사이트 열기
start "C:\Users\기광우\freight-delivery-website\index.html"
```

## Notes

- 다음 세션에서는 현재 상태 그대로 작업 재개 가능
- 모든 데이터 연동 시스템이 완성되어 있음
- 관리자 페이지 로그인 상태 유지됨