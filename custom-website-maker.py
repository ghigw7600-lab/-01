#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
맞춤형 웹사이트 생성기
사용자가 원하는 비즈니스 정보를 입력하면 맞춤형 웹사이트를 생성합니다
"""

import os
import json
from datetime import datetime

class CustomWebsiteMaker:
    def __init__(self):
        self.color_schemes = {
            "restaurant": {"primary": "#c0392b", "secondary": "#e74c3c", "accent": "#ec7063"},
            "cafe": {"primary": "#d35400", "secondary": "#f39c12", "accent": "#e67e22"},
            "clinic": {"primary": "#27ae60", "secondary": "#2ecc71", "accent": "#7dcea0"},
            "fitness": {"primary": "#8e44ad", "secondary": "#9b59b6", "accent": "#bb8fce"},
            "beauty": {"primary": "#e91e63", "secondary": "#f06292", "accent": "#f8bbd9"},
            "shop": {"primary": "#2980b9", "secondary": "#3498db", "accent": "#7fb3d3"},
            "service": {"primary": "#34495e", "secondary": "#5d6d7e", "accent": "#85929e"},
            "law": {"primary": "#2c3e50", "secondary": "#34495e", "accent": "#5d6d7e"},
            "medical": {"primary": "#16a085", "secondary": "#1abc9c", "accent": "#48c9b0"},
            "tech": {"primary": "#9b59b6", "secondary": "#8e44ad", "accent": "#bb8fce"}
        }

    def get_colors(self, business_type):
        """업종에 맞는 색상 테마 선택"""
        business_lower = business_type.lower()
        for key in self.color_schemes:
            if key in business_lower:
                return self.color_schemes[key]
        return self.color_schemes["service"]

    def get_user_input(self):
        """사용자로부터 비즈니스 정보 입력받기"""
        print("=== 맞춤형 웹사이트 생성기 ===")
        print("원하시는 웹사이트 정보를 입력해주세요:")
        print()

        name = input("비즈니스 이름: ").strip()
        business_type = input("업종 (예: 카페, 병원, 미용실, 법무사무소): ").strip()

        print("주요 서비스나 특징을 입력하세요 (쉼표로 구분):")
        keywords_input = input("예: 전문상담, 24시간운영, 친환경: ").strip()
        keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]

        phone = input("전화번호: ").strip()
        email = input("이메일: ").strip()
        address = input("주소: ").strip()

        return name, business_type, keywords, phone, email, address

    def create_website(self, name, business_type, keywords, phone, email, address):
        """맞춤형 웹사이트 생성"""

        # 폴더명 생성 (특수문자 제거)
        safe_name = name.replace(' ', '-').replace(',', '').replace('/', '-')
        folder = f"{safe_name.lower()}-website"
        os.makedirs(folder, exist_ok=True)

        colors = self.get_colors(business_type)

        # 메인 웹사이트 HTML
        html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {business_type}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; }}

        .hero {{
            background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
            color: white; padding: 120px 0; text-align: center; position: relative;
        }}
        .hero::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.1);
        }}
        .hero-content {{ position: relative; z-index: 1; }}
        .hero h1 {{ font-size: 3.5rem; margin-bottom: 1rem; font-weight: 300; }}
        .hero .subtitle {{ font-size: 1.3rem; margin-bottom: 1rem; opacity: 0.9; }}
        .hero .keywords {{ font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.8; }}

        .btn {{
            background: {colors['accent']}; color: white; padding: 18px 35px; border: none;
            border-radius: 30px; text-decoration: none; display: inline-block;
            font-weight: 600; transition: all 0.3s ease; cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}
        .btn:hover {{ transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.3); }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .section {{ padding: 80px 0; }}

        .features {{ background: #f8f9fa; }}
        .features-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px; margin-top: 50px;
        }}
        .feature-card {{
            background: white; padding: 40px; border-radius: 20px; text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease;
        }}
        .feature-card:hover {{ transform: translateY(-10px); }}

        .booking {{ background: linear-gradient(135deg, {colors['secondary']} 0%, {colors['primary']} 100%); color: white; }}
        .booking-form {{
            max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.15);
            padding: 50px; border-radius: 20px; backdrop-filter: blur(10px);
        }}
        .form-group {{ margin-bottom: 25px; }}
        .form-group label {{ display: block; margin-bottom: 8px; font-weight: 600; }}
        .form-group input, .form-group select, .form-group textarea {{
            width: 100%; padding: 15px; border: none; border-radius: 10px;
            background: rgba(255,255,255,0.9); font-size: 16px;
        }}

        .contact {{ background: #2c3e50; color: white; }}
        .contact-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px; margin-top: 40px;
        }}
        .contact-item {{ text-align: center; padding: 30px; }}

        .admin-btn {{
            position: fixed; bottom: 30px; right: 30px; background: {colors['primary']};
            color: white; padding: 20px; border-radius: 60px; text-decoration: none;
            font-weight: bold; box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2.5rem; }}
            .container {{ padding: 0 15px; }}
            .section {{ padding: 60px 0; }}
        }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>{name}</h1>
                <div class="subtitle">전문 {business_type} 서비스</div>
                <div class="keywords">{' • '.join(keywords)}</div>
                <a href="#booking" class="btn">예약하기</a>
            </div>
        </div>
    </section>

    <section class="features section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 20px;">왜 {name}을 선택해야 할까요?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>전문성</h3>
                    <p>수년간의 경험과 전문 지식으로 최고의 {business_type} 서비스를 제공합니다.</p>
                </div>
                <div class="feature-card">
                    <h3>품질</h3>
                    <p>고품질의 서비스와 고객 만족을 위해 최선을 다합니다.</p>
                </div>
                <div class="feature-card">
                    <h3>신뢰성</h3>
                    <p>약속된 시간과 품질을 지키며 고객과의 신뢰를 최우선으로 합니다.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="booking" class="booking section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 40px;">예약 문의</h2>
            <form class="booking-form" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label>성함</label>
                    <input type="text" name="name" required placeholder="성함을 입력하세요">
                </div>
                <div class="form-group">
                    <label>연락처</label>
                    <input type="tel" name="phone" required placeholder="010-0000-0000">
                </div>
                <div class="form-group">
                    <label>이메일</label>
                    <input type="email" name="email" required placeholder="your@email.com">
                </div>
                <div class="form-group">
                    <label>서비스 종류</label>
                    <select name="service" required>
                        <option value="">서비스를 선택하세요</option>
                        <option value="consultation">상담</option>
                        <option value="basic">기본 서비스</option>
                        <option value="premium">프리미엄 서비스</option>
                        <option value="custom">맞춤 서비스</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>희망 날짜</label>
                    <input type="date" name="date" required>
                </div>
                <div class="form-group">
                    <label>추가 요청사항</label>
                    <textarea name="message" rows="4" placeholder="추가로 요청하실 내용이 있으시면 입력해주세요"></textarea>
                </div>
                <button type="submit" class="btn" style="width: 100%; font-size: 18px;">예약 신청하기</button>
            </form>
        </div>
    </section>

    <section class="contact section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 20px;">연락처</h2>
            <div class="contact-grid">
                <div class="contact-item">
                    <h3>전화번호</h3>
                    <p style="font-size: 1.2rem;">{phone}</p>
                </div>
                <div class="contact-item">
                    <h3>이메일</h3>
                    <p style="font-size: 1.2rem;">{email}</p>
                </div>
                <div class="contact-item">
                    <h3>주소</h3>
                    <p style="font-size: 1.2rem;">{address}</p>
                </div>
            </div>
        </div>
    </section>

    <a href="admin.html" class="admin-btn">관리자</a>

    <script>
        function submitBooking(event) {{
            event.preventDefault();

            const formData = new FormData(event.target);
            const booking = {{
                id: Date.now() + Math.random(),
                business: '{name}',
                name: formData.get('name'),
                phone: formData.get('phone'),
                email: formData.get('email'),
                service: formData.get('service'),
                date: formData.get('date'),
                message: formData.get('message'),
                status: 'pending',
                createdAt: new Date().toISOString()
            }};

            const bookings = JSON.parse(localStorage.getItem('custom_bookings') || '[]');
            bookings.push(booking);
            localStorage.setItem('custom_bookings', JSON.stringify(bookings));

            alert('예약 신청이 완료되었습니다! 곧 연락드리겠습니다.');
            event.target.reset();
        }}
    </script>
</body>
</html>"""

        # 관리자 패널 HTML
        admin = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 관리자 페이지</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f6fa; }}

        .header {{
            background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
            color: white; padding: 30px 0; text-align: center;
        }}
        .header h1 {{ font-size: 2.5rem; font-weight: 300; }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 30px 20px; }}

        .stats {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px; margin-bottom: 40px;
        }}
        .stat-card {{
            background: white; padding: 30px; border-radius: 15px; text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }}
        .stat-number {{ font-size: 2.5rem; font-weight: bold; color: {colors['primary']}; }}
        .stat-label {{ color: #666; margin-top: 10px; }}

        .bookings {{
            background: white; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }}
        .bookings-header {{ background: {colors['secondary']}; color: white; padding: 25px; text-align: center; }}
        .booking-item {{ padding: 25px; border-bottom: 1px solid #eee; }}
        .booking-name {{ font-size: 1.2rem; font-weight: bold; color: {colors['primary']}; }}
        .booking-details {{ color: #666; margin-top: 10px; }}
        .no-bookings {{ text-align: center; padding: 60px; color: #666; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{name} 관리자 페이지</h1>
        <p>예약 관리 및 통계</p>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="total">0</div>
                <div class="stat-label">총 예약</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="today">0</div>
                <div class="stat-label">오늘 예약</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pending">0</div>
                <div class="stat-label">대기중</div>
            </div>
        </div>

        <div class="bookings">
            <div class="bookings-header">
                <h2>최근 예약 목록</h2>
            </div>
            <div id="bookingsList">
                <div class="no-bookings">아직 예약이 없습니다</div>
            </div>
        </div>
    </div>

    <script>
        function loadBookings() {{
            const allBookings = JSON.parse(localStorage.getItem('custom_bookings') || '[]');
            const businessBookings = allBookings.filter(b => b.business === '{name}');

            document.getElementById('total').textContent = businessBookings.length;

            const today = new Date().toDateString();
            const todayCount = businessBookings.filter(b =>
                new Date(b.createdAt).toDateString() === today
            ).length;
            document.getElementById('today').textContent = todayCount;

            const pendingCount = businessBookings.filter(b => b.status === 'pending').length;
            document.getElementById('pending').textContent = pendingCount;

            const bookingsList = document.getElementById('bookingsList');
            if (businessBookings.length === 0) {{
                bookingsList.innerHTML = '<div class="no-bookings">아직 예약이 없습니다</div>';
            }} else {{
                bookingsList.innerHTML = businessBookings
                    .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
                    .map(booking => `
                        <div class="booking-item">
                            <div class="booking-name">${{booking.name}}</div>
                            <div class="booking-details">
                                연락처: ${{booking.phone}} | 이메일: ${{booking.email}}<br>
                                서비스: ${{booking.service}} | 희망날짜: ${{booking.date}}<br>
                                신청일: ${{new Date(booking.createdAt).toLocaleString()}}
                                ${{booking.message ? '<br>요청사항: ' + booking.message : ''}}
                            </div>
                        </div>
                    `).join('');
            }}
        }}

        loadBookings();
        setInterval(loadBookings, 5000);
    </script>
</body>
</html>"""

        # 파일 저장
        with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
            f.write(html)

        with open(f"{folder}/admin.html", "w", encoding="utf-8") as f:
            f.write(admin)

        # 정보 파일 저장
        info = {
            "business_name": name,
            "business_type": business_type,
            "keywords": keywords,
            "contact": {"phone": phone, "email": email, "address": address},
            "created": datetime.now().isoformat()
        }

        with open(f"{folder}/info.json", "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2, ensure_ascii=False)

        return folder

    def run(self):
        """맞춤형 웹사이트 생성기 실행"""
        try:
            name, business_type, keywords, phone, email, address = self.get_user_input()

            print()
            print(f"'{name}' 웹사이트를 생성하고 있습니다...")
            folder = self.create_website(name, business_type, keywords, phone, email, address)

            print()
            print("웹사이트가 성공적으로 생성되었습니다!")
            print(f"폴더: {folder}")
            print(f"홈페이지: {folder}/index.html")
            print(f"관리자 페이지: {folder}/admin.html")
            print()
            print("브라우저에서 index.html 파일을 열어 확인해보세요!")

        except KeyboardInterrupt:
            print("\n생성을 취소했습니다.")
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    maker = CustomWebsiteMaker()
    maker.run()