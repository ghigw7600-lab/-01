#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 키워드 기반 홈페이지 자동 생성기 v2.0
몇 가지 키워드만 입력하면 완전한 웹사이트를 자동으로 생성합니다!

성공 사례:
- 숨결 장례식장 (반려동물 전문 장례 서비스)
- 동네화물 운송 (지역 화물 배송 서비스)

사용법:
python 홈페이지자동생성기.py
"""

import os
import json
import uuid
import webbrowser
from datetime import datetime
from pathlib import Path

def get_user_input():
    """사용자로부터 비즈니스 정보를 입력받습니다."""
    print("=" * 50)
    print("    🚀 키워드 기반 홈페이지 자동 생성기")
    print("=" * 50)
    print()
    print("몇 가지 키워드만 입력하면 완전한 웹사이트를 자동으로 생성합니다!")
    print("성공 사례: 숨결 장례식장, 동네화물 운송")
    print()

    config = {}

    config['business_name'] = input("🏢 사업체 이름을 입력하세요 (예: 행복한 카페): ")

    print("\n📋 사업 분야를 선택하세요:")
    print("1: 서비스업")
    print("2: 음식점")
    print("3: 의료/헬스케어")
    print("4: 쇼핑몰")
    print("5: 기타")
    business_type = input("선택 (1-5): ")

    keywords_input = input("\n🎯 주요 키워드를 입력하세요 (쉼표로 구분, 예: 커피,디저트,브런치): ")
    config['keywords'] = [k.strip() for k in keywords_input.split(',')]

    config['phone'] = input("\n📞 연락처를 입력하세요 (예: 010-1234-5678): ")
    config['email'] = input("📧 이메일을 입력하세요 (예: info@company.com): ")
    config['address'] = input("📍 주소를 입력하세요 (예: 서울시 강남구): ")

    # 비즈니스 타입별 설정
    type_configs = {
        '1': {
            'type': 'service',
            'color': 'professional',
            'icon': '🏢',
            'services': ['전문 상담', '맞춤 서비스', '사후 관리']
        },
        '2': {
            'type': 'restaurant',
            'color': 'warm',
            'icon': '🍽️',
            'services': ['메인 메뉴', '음료', '디저트']
        },
        '3': {
            'type': 'medical',
            'color': 'medical',
            'icon': '🏥',
            'services': ['진료', '검사', '치료']
        },
        '4': {
            'type': 'ecommerce',
            'color': 'tech',
            'icon': '🛒',
            'services': ['상품 판매', '배송', '고객 서비스']
        },
        '5': {
            'type': 'business',
            'color': 'professional',
            'icon': '💼',
            'services': ['기본 서비스', '고급 서비스', '프리미엄 서비스']
        }
    }

    config.update(type_configs.get(business_type, type_configs['5']))

    return config

def get_color_scheme(color_name):
    """색상 스킴을 반환합니다."""
    colors = {
        'professional': {
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'accent': '#e74c3c'
        },
        'warm': {
            'primary': '#d35400',
            'secondary': '#f39c12',
            'accent': '#e67e22'
        },
        'medical': {
            'primary': '#2980b9',
            'secondary': '#3498db',
            'accent': '#1abc9c'
        },
        'tech': {
            'primary': '#34495e',
            'secondary': '#95a5a6',
            'accent': '#f1c40f'
        }
    }
    return colors.get(color_name, colors['professional'])

def generate_html_template(config):
    """HTML 템플릿을 생성합니다."""
    colors = get_color_scheme(config['color'])

    # 서비스 카드 생성
    service_cards = ""
    icons = ['⭐', '🎯', '💎']
    for i, service in enumerate(config['services']):
        icon = icons[i] if i < len(icons) else '🏢'
        service_cards += f"""
                <div class="service-card">
                    <div class="service-icon">{icon}</div>
                    <h3>{service}</h3>
                    <p>고객 만족을 위한 {service} 서비스를 제공합니다</p>
                </div>"""

    # 서비스 옵션 생성
    service_options = ""
    for service in config['services']:
        service_options += f'<option value="{service}">{service}</option>'

    template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['business_name']} - {', '.join(config['keywords'])}</title>
    <meta name="description" content="{config['business_name']}는 {', '.join(config['keywords'])}를 제공하는 전문 업체입니다.">
    <meta name="keywords" content="{', '.join(config['keywords'])}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>{config['icon']}</text></svg>" />
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Apple SD Gothic Neo', -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.6; color: {colors['primary']}; }}

        /* Header */
        header {{ position: fixed; top: 0; left: 0; right: 0; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border-bottom: 1px solid #dee2e6; padding: 1rem 0; z-index: 1000; }}
        nav {{ display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}
        .logo {{ font-size: 1.8rem; font-weight: 700; color: {colors['primary']}; }}
        .nav-menu {{ display: flex; list-style: none; gap: 2rem; }}
        .nav-item a {{ text-decoration: none; color: {colors['primary']}; font-weight: 500; transition: color 0.3s ease; }}
        .nav-item a:hover {{ color: {colors['secondary']}; }}

        /* Hero */
        .hero {{ background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%); color: white; padding: 120px 0 80px; text-align: center; }}
        .hero-content {{ max-width: 800px; margin: 0 auto; padding: 0 2rem; }}
        .hero h1 {{ font-size: 3rem; margin-bottom: 1rem; font-weight: 700; }}
        .hero p {{ font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9; }}
        .cta-button {{ background: {colors['accent']}; color: white; padding: 15px 30px; border: none; border-radius: 8px; font-size: 1.1rem; font-weight: 600; cursor: pointer; text-decoration: none; display: inline-block; transition: transform 0.3s ease; }}
        .cta-button:hover {{ transform: translateY(-2px); }}

        /* Services */
        .services {{ padding: 80px 0; background: #f8f9fa; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}
        .section-title {{ text-align: center; margin-bottom: 3rem; }}
        .section-title h2 {{ font-size: 2.5rem; color: {colors['primary']}; margin-bottom: 1rem; }}
        .services-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem; }}
        .service-card {{ background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center; transition: transform 0.3s ease; }}
        .service-card:hover {{ transform: translateY(-5px); }}
        .service-icon {{ font-size: 3rem; color: {colors['secondary']}; margin-bottom: 1rem; }}
        .service-card h3 {{ color: {colors['primary']}; margin-bottom: 1rem; }}

        /* Booking */
        .booking {{ padding: 80px 0; background: white; }}
        .booking-form {{ max-width: 600px; margin: 0 auto; }}
        .form-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem; }}
        .form-group {{ margin-bottom: 1rem; }}
        .form-group label {{ display: block; margin-bottom: 0.5rem; font-weight: 600; }}
        .form-group input, .form-group select, .form-group textarea {{ width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }}
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {{ outline: none; border-color: {colors['secondary']}; }}

        /* Contact */
        .contact {{ padding: 80px 0; background: {colors['primary']}; color: white; }}
        .contact-info {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem; }}
        .contact-item {{ text-align: center; }}
        .contact-item h3 {{ margin-bottom: 1rem; color: {colors['secondary']}; }}

        /* Footer */
        footer {{ background: #2c3e50; color: white; text-align: center; padding: 2rem 0; }}

        /* Responsive */
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
            .nav-menu {{ display: none; }}
            .services-grid {{ grid-template-columns: 1fr; }}
            .form-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">{config['icon']} {config['business_name']}</div>
            <ul class="nav-menu">
                <li class="nav-item"><a href="#home">홈</a></li>
                <li class="nav-item"><a href="#services">서비스</a></li>
                <li class="nav-item"><a href="#booking">예약</a></li>
                <li class="nav-item"><a href="#contact">연락처</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero" id="home">
        <div class="hero-content">
            <h1>{config['business_name']}</h1>
            <p>{', '.join(config['keywords'])}를 제공하는 전문 업체입니다</p>
            <a href="#booking" class="cta-button">지금 예약하기</a>
        </div>
    </section>

    <section class="services" id="services">
        <div class="container">
            <div class="section-title">
                <h2>우리의 서비스</h2>
                <p>고품질의 서비스를 제공합니다</p>
            </div>
            <div class="services-grid">{service_cards}
            </div>
        </div>
    </section>

    <section class="booking" id="booking">
        <div class="container">
            <div class="section-title">
                <h2>예약하기</h2>
                <p>간편하게 예약하실 수 있습니다</p>
            </div>
            <form class="booking-form" id="bookingForm">
                <div class="form-grid">
                    <div class="form-group">
                        <label>이름</label>
                        <input type="text" name="name" required placeholder="성함을 입력해주세요">
                    </div>
                    <div class="form-group">
                        <label>연락처</label>
                        <input type="tel" name="phone" required placeholder="연락처를 입력해주세요">
                    </div>
                </div>
                <div class="form-group">
                    <label>서비스</label>
                    <select name="service" required>
                        <option value="">선택해주세요</option>
                        {service_options}
                    </select>
                </div>
                <div class="form-group">
                    <label>희망 날짜</label>
                    <input type="date" name="date" required>
                </div>
                <div class="form-group">
                    <label>요청사항</label>
                    <textarea name="message" rows="4" placeholder="특별한 요청사항이 있으시면 적어주세요"></textarea>
                </div>
                <button type="submit" class="cta-button" style="width: 100%;">예약 신청</button>
            </form>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="container">
            <div class="section-title">
                <h2>연락처</h2>
                <p>언제든지 문의해주세요</p>
            </div>
            <div class="contact-info">
                <div class="contact-item">
                    <h3>📞 전화번호</h3>
                    <p>{config['phone']}</p>
                </div>
                <div class="contact-item">
                    <h3>📧 이메일</h3>
                    <p>{config['email']}</p>
                </div>
                <div class="contact-item">
                    <h3>📍 주소</h3>
                    <p>{config['address']}</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 {config['business_name']}. All rights reserved.</p>
            <p style="margin-top: 10px; font-size: 0.9rem; opacity: 0.7;">🔧 Generated with Auto Website Generator</p>
        </div>
    </footer>

    <script>
        // 스무스 스크롤
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});

        // 예약 폼 처리
        document.getElementById('bookingForm').addEventListener('submit', function(e) {{
            e.preventDefault();

            const formData = new FormData(this);
            const bookingData = {{
                name: formData.get('name'),
                phone: formData.get('phone'),
                service: formData.get('service'),
                date: formData.get('date'),
                message: formData.get('message'),
                status: '대기중',
                orderId: Date.now(),
                createdAt: new Date().toISOString()
            }};

            // LocalStorage에 저장
            const existingBookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            existingBookings.push({{ ...bookingData, id: Date.now() + Math.random() }});
            localStorage.setItem('bookings', JSON.stringify(existingBookings));

            alert('예약이 접수되었습니다! 곧 연락드리겠습니다.');
            this.reset();
        }});

        // 오늘 날짜를 최소값으로 설정
        document.querySelector('input[type="date"]').min = new Date().toISOString().split('T')[0];
    </script>
</body>
</html>"""

    return template

def generate_admin_template(config):
    """관리자 페이지 템플릿을 생성합니다."""
    template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['business_name']} - 관리자 페이지</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); min-height: 100vh; color: #333; }}
        .login-container {{ max-width: 450px; margin: 100px auto; padding: 40px; background: white; border-radius: 15px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); text-align: center; }}
        .login-container h2 {{ color: #2c3e50; margin-bottom: 30px; font-size: 1.8rem; }}
        .login-input {{ width: 100%; padding: 15px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }}
        .login-btn {{ background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); color: white; padding: 15px 30px; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer; width: 100%; margin-top: 20px; }}
        .dashboard {{ display: none; max-width: 1400px; margin: 0 auto; padding: 20px; }}
        .dashboard-header {{ background: white; border-radius: 15px; padding: 25px; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); display: flex; justify-content: space-between; align-items: center; }}
        .logout-btn {{ background: #e74c3c; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; padding: 25px; text-align: center; }}
        .stat-card h3 {{ font-size: 2.5rem; margin-bottom: 10px; }}
        .management-card {{ background: white; border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 25px; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        .data-table th, .data-table td {{ padding: 12px; text-align: left; border-bottom: 1px solid #dee2e6; }}
        .data-table th {{ background: #f8f9fa; color: #2c3e50; font-weight: 600; }}
        .status-badge {{ padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; }}
        .status-pending {{ background: #fff3cd; color: #856404; }}
        .status-completed {{ background: #d4edda; color: #155724; }}
    </style>
</head>
<body>
    <div class="login-container" id="loginSection">
        <h2>🔐 {config['business_name']} 관리자</h2>
        <input type="text" class="login-input" placeholder="관리자 아이디" id="username" value="admin">
        <input type="password" class="login-input" placeholder="비밀번호" id="password" value="admin123">
        <button class="login-btn" onclick="login()">로그인</button>
        <p style="margin-top: 15px; font-size: 0.9rem; color: #95a5a6;">아이디: admin / 비밀번호: admin123</p>
    </div>

    <div class="dashboard" id="dashboard">
        <div class="dashboard-header">
            <h1>📊 {config['business_name']} 관리자 대시보드</h1>
            <button class="logout-btn" onclick="logout()">로그아웃</button>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <h3 id="total-bookings">0</h3>
                <p>총 예약</p>
            </div>
            <div class="stat-card">
                <h3 id="pending-bookings">0</h3>
                <p>대기 중인 예약</p>
            </div>
            <div class="stat-card">
                <h3 id="completed-bookings">0</h3>
                <p>완료된 예약</p>
            </div>
        </div>

        <div class="management-card">
            <h3>📋 예약 관리</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>예약일</th>
                        <th>고객명</th>
                        <th>연락처</th>
                        <th>서비스</th>
                        <th>상태</th>
                    </tr>
                </thead>
                <tbody id="bookings-table">
                </tbody>
            </table>
        </div>
    </div>

    <script>
        function login() {{
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (username === 'admin' && password === 'admin123') {{
                localStorage.setItem('adminLoggedIn', 'true');
                document.getElementById('loginSection').style.display = 'none';
                document.getElementById('dashboard').style.display = 'block';
                loadBookings();
            }} else {{
                alert('❌ 아이디 또는 비밀번호가 올바르지 않습니다.');
            }}
        }}

        function logout() {{
            localStorage.removeItem('adminLoggedIn');
            document.getElementById('loginSection').style.display = 'block';
            document.getElementById('dashboard').style.display = 'none';
        }}

        function loadBookings() {{
            const bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            const tbody = document.getElementById('bookings-table');
            tbody.innerHTML = '';

            document.getElementById('total-bookings').textContent = bookings.length;
            document.getElementById('pending-bookings').textContent = bookings.filter(b => b.status === '대기중').length;
            document.getElementById('completed-bookings').textContent = bookings.filter(b => b.status === '완료').length;

            bookings.forEach(booking => {{
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${{booking.date}}</td>
                    <td>${{booking.name}}</td>
                    <td>${{booking.phone}}</td>
                    <td>${{booking.service}}</td>
                    <td><span class="status-badge status-${{booking.status === '대기중' ? 'pending' : 'completed'}}">${{booking.status}}</span></td>
                `;
            }});
        }}

        // 로그인 상태 확인
        if (localStorage.getItem('adminLoggedIn') === 'true') {{
            document.getElementById('loginSection').style.display = 'none';
            document.getElementById('dashboard').style.display = 'block';
            loadBookings();
        }}

        setInterval(loadBookings, 3000);
    </script>
</body>
</html>"""

    return template

def create_website(config):
    """웹사이트를 생성합니다."""
    # 프로젝트 폴더 생성
    project_name = config['business_name'].lower().replace(' ', '-')
    project_path = Path(f"{project_name}-website")
    project_path.mkdir(exist_ok=True)

    print(f"\n⏳ 웹사이트 생성 중...")

    # HTML 파일들 생성
    main_html = generate_html_template(config)
    admin_html = generate_admin_template(config)

    # 파일 저장
    (project_path / "index.html").write_text(main_html, encoding='utf-8')
    (project_path / "admin.html").write_text(admin_html, encoding='utf-8')

    # package.json 생성
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": f"{config['business_name']} 웹사이트",
        "main": "index.html",
        "scripts": {
            "start": "npx live-server",
            "deploy": "netlify deploy --prod"
        },
        "keywords": config['keywords'],
        "author": config['business_name'],
        "license": "MIT"
    }

    (project_path / "package.json").write_text(json.dumps(package_json, indent=2, ensure_ascii=False), encoding='utf-8')

    # README.md 생성
    readme_content = f"""# {config['business_name']} 웹사이트

{', '.join(config['keywords'])}를 제공하는 {config['business_name']}의 공식 웹사이트입니다.

## 기능
- 반응형 웹 디자인
- 예약 시스템
- 관리자 페이지
- 실시간 데이터 동기화

## 실행 방법
```bash
npm install
npm start
```

## 관리자 접속
- URL: /admin.html
- 아이디: admin
- 비밀번호: admin123

---
🔧 Generated with Auto Website Generator
"""

    (project_path / "README.md").write_text(readme_content, encoding='utf-8')

    return project_path

def main():
    """메인 함수"""
    try:
        # 사용자 입력 받기
        config = get_user_input()

        # 웹사이트 생성
        project_path = create_website(config)

        print("\n" + "=" * 50)
        print("    ✅ 웹사이트 생성이 완료되었습니다!")
        print("=" * 50)
        print()
        print(f"📁 생성된 폴더: {project_path}")
        print(f"🌐 index.html: 메인 홈페이지")
        print(f"🔧 admin.html: 관리자 페이지 (admin/admin123)")
        print()
        print("🚀 실행 방법:")
        print("1. 생성된 폴더로 이동")
        print("2. index.html 파일을 더블클릭하여 열기")
        print("3. 또는 live-server로 실행: npm install && npm start")
        print()

        # 웹사이트 바로 열기 옵션
        open_now = input("💻 지금 바로 웹사이트를 열어보시겠습니까? (y/n): ")
        if open_now.lower() == 'y':
            webbrowser.open(str(project_path / "index.html"))
            webbrowser.open(str(project_path / "admin.html"))

        # 결과 요약을 HTML 파일로 생성
        summary_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹사이트 생성 완료 - {config['business_name']}</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; background: #f8f9fa; }}
        .card {{ background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 2rem; }}
        .success {{ background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; text-align: center; }}
        .info {{ border-left: 4px solid #007bff; }}
        h1 {{ margin-bottom: 1rem; }}
        h2 {{ color: #495057; margin-bottom: 1rem; }}
        .links {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 2rem; }}
        .link-btn {{ background: #007bff; color: white; padding: 1rem; border-radius: 8px; text-decoration: none; text-align: center; transition: transform 0.3s; }}
        .link-btn:hover {{ transform: translateY(-2px); }}
        .admin-btn {{ background: #6f42c1; }}
    </style>
</head>
<body>
    <div class="card success">
        <h1>🎉 웹사이트 생성 완료!</h1>
        <p>{config['business_name']} 웹사이트가 성공적으로 생성되었습니다.</p>
    </div>

    <div class="card info">
        <h2>📋 프로젝트 정보</h2>
        <p><strong>사업체명:</strong> {config['business_name']}</p>
        <p><strong>키워드:</strong> {', '.join(config['keywords'])}</p>
        <p><strong>타입:</strong> {config['type']}</p>
        <p><strong>연락처:</strong> {config['phone']}</p>
        <p><strong>이메일:</strong> {config['email']}</p>
        <p><strong>주소:</strong> {config['address']}</p>
    </div>

    <div class="card">
        <h2>🔗 바로가기</h2>
        <div class="links">
            <a href="{project_path}/index.html" class="link-btn">🌐 메인 홈페이지</a>
            <a href="{project_path}/admin.html" class="link-btn admin-btn">🔧 관리자 페이지</a>
        </div>
        <p style="margin-top: 1rem; text-align: center; color: #6c757d;">
            관리자 로그인: admin / admin123
        </p>
    </div>

    <div class="card">
        <h2>🚀 다음 단계</h2>
        <ol>
            <li>생성된 웹사이트 확인 및 수정</li>
            <li>실제 연락처 및 주소 정보로 업데이트</li>
            <li>이미지 및 로고 추가</li>
            <li>GitHub에 업로드</li>
            <li>Netlify로 배포</li>
            <li>도메인 연결</li>
        </ol>
    </div>
</body>
</html>"""

        with open('blog_output.html', 'w', encoding='utf-8') as f:
            f.write(summary_html)

        print("📄 생성 결과가 blog_output.html에 저장되었습니다.")

    except KeyboardInterrupt:
        print("\n\n❌ 사용자에 의해 취소되었습니다.")
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()