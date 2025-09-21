#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 Website Maker - Automated Website Generator
Create professional websites in seconds with just a few keywords!

Usage:
python website-maker.py

Features:
- Complete responsive websites
- Booking system with LocalStorage
- Admin panel with real-time statistics
- Professional design
- No Unicode console issues
"""

import os
import json
from datetime import datetime

class WebsiteMaker:
    def __init__(self):
        self.color_schemes = {
            "restaurant": {"primary": "#c0392b", "secondary": "#e74c3c", "accent": "#ec7063"},
            "cafe": {"primary": "#d35400", "secondary": "#f39c12", "accent": "#e67e22"},
            "clinic": {"primary": "#27ae60", "secondary": "#2ecc71", "accent": "#7dcea0"},
            "fitness": {"primary": "#8e44ad", "secondary": "#9b59b6", "accent": "#bb8fce"},
            "beauty": {"primary": "#e91e63", "secondary": "#f06292", "accent": "#f8bbd9"},
            "shop": {"primary": "#2980b9", "secondary": "#3498db", "accent": "#7fb3d3"},
            "service": {"primary": "#34495e", "secondary": "#5d6d7e", "accent": "#85929e"}
        }

    def get_colors(self, business_type):
        """Get color scheme based on business type"""
        for key in self.color_schemes:
            if key in business_type.lower():
                return self.color_schemes[key]
        return self.color_schemes["service"]

    def create_website(self, name, btype, keywords, phone, email, address):
        """Generate complete website"""

        folder = f"{name.lower().replace(' ', '-').replace(',', '')}-auto"
        os.makedirs(folder, exist_ok=True)

        colors = self.get_colors(btype)

        # Main website
        html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {btype.title()}</title>
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
        .feature-icon {{
            width: 80px; height: 80px; background: {colors['primary']}; color: white;
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-size: 2rem; margin: 0 auto 20px;
        }}

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
        .contact-item h3 {{ color: {colors['accent']}; margin-bottom: 10px; }}

        .admin-btn {{
            position: fixed; bottom: 30px; right: 30px; background: {colors['primary']};
            color: white; padding: 20px; border-radius: 60px; text-decoration: none;
            font-weight: bold; box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }}
        .admin-btn:hover {{ transform: scale(1.1); }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2.5rem; }}
            .hero .subtitle {{ font-size: 1.1rem; }}
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
                <div class="subtitle">Premium {btype} Services</div>
                <div class="keywords">🌟 {' • '.join(keywords)}</div>
                <a href="#booking" class="btn">Book Now</a>
            </div>
        </div>
    </section>

    <section class="features section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 20px;">Why Choose Us</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">⭐</div>
                    <h3>Professional Excellence</h3>
                    <p>Top-quality {btype} services with years of expertise and dedication to customer satisfaction.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💎</div>
                    <h3>Premium Quality</h3>
                    <p>We use only the finest materials and latest techniques to deliver exceptional results.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🚀</div>
                    <h3>Fast & Reliable</h3>
                    <p>Quick turnaround times without compromising on quality or attention to detail.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="booking" class="booking section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 40px;">Book Your Service</h2>
            <form class="booking-form" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label>Your Name</label>
                    <input type="text" name="name" required placeholder="Enter your full name">
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" name="phone" required placeholder="010-0000-0000">
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" name="email" required placeholder="your@email.com">
                </div>
                <div class="form-group">
                    <label>Service Type</label>
                    <select name="service" required>
                        <option value="">Select a service</option>
                        <option value="consultation">Free Consultation</option>
                        <option value="basic">Basic Service</option>
                        <option value="premium">Premium Service</option>
                        <option value="custom">Custom Package</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Preferred Date</label>
                    <input type="date" name="date" required>
                </div>
                <div class="form-group">
                    <label>Additional Information</label>
                    <textarea name="message" rows="4" placeholder="Tell us about your specific needs..."></textarea>
                </div>
                <button type="submit" class="btn" style="width: 100%; font-size: 18px;">Submit Booking Request</button>
            </form>
        </div>
    </section>

    <section class="contact section">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 20px;">Get In Touch</h2>
            <div class="contact-grid">
                <div class="contact-item">
                    <h3>📞 Phone</h3>
                    <p style="font-size: 1.2rem;">{phone}</p>
                </div>
                <div class="contact-item">
                    <h3>✉️ Email</h3>
                    <p style="font-size: 1.2rem;">{email}</p>
                </div>
                <div class="contact-item">
                    <h3>📍 Location</h3>
                    <p style="font-size: 1.2rem;">{address}</p>
                </div>
            </div>
        </div>
    </section>

    <a href="admin.html" class="admin-btn">Admin</a>

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

            // Save to localStorage
            const bookings = JSON.parse(localStorage.getItem('website_bookings') || '[]');
            bookings.push(booking);
            localStorage.setItem('website_bookings', JSON.stringify(bookings));

            alert('🎉 Booking submitted successfully! We will contact you soon.');
            event.target.reset();
        }}
    </script>
</body>
</html>"""

        # Admin Panel
        admin = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Admin Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f6fa; }}

        .header {{
            background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
            color: white; padding: 30px 0; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        .header h1 {{ font-size: 2.5rem; font-weight: 300; }}
        .header p {{ opacity: 0.9; margin-top: 10px; }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 30px 20px; }}

        .stats {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px; margin-bottom: 40px;
        }}
        .stat-card {{
            background: white; padding: 30px; border-radius: 15px; text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1); transition: transform 0.3s ease;
        }}
        .stat-card:hover {{ transform: translateY(-5px); }}
        .stat-number {{ font-size: 2.5rem; font-weight: bold; color: {colors['primary']}; }}
        .stat-label {{ color: #666; margin-top: 10px; font-size: 1.1rem; }}

        .bookings {{
            background: white; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .bookings-header {{
            background: {colors['secondary']}; color: white; padding: 25px; text-align: center;
        }}
        .bookings-header h2 {{ font-size: 1.8rem; font-weight: 400; }}

        .booking-item {{
            padding: 25px; border-bottom: 1px solid #eee; transition: background 0.3s ease;
        }}
        .booking-item:hover {{ background: #f8f9fa; }}
        .booking-item:last-child {{ border-bottom: none; }}

        .booking-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .booking-name {{ font-size: 1.2rem; font-weight: bold; color: {colors['primary']}; }}
        .booking-status {{
            background: #27ae60; color: white; padding: 5px 12px; border-radius: 20px;
            font-size: 0.85rem; font-weight: 600;
        }}
        .booking-details {{ color: #666; line-height: 1.6; }}
        .booking-details strong {{ color: #333; }}

        .no-bookings {{
            text-align: center; padding: 60px; color: #666; font-size: 1.1rem;
        }}
        .no-bookings-icon {{ font-size: 3rem; margin-bottom: 20px; }}

        .refresh-btn {{
            position: fixed; bottom: 30px; right: 30px; background: {colors['primary']};
            color: white; padding: 15px; border-radius: 50px; border: none;
            cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }}
        .refresh-btn:hover {{ transform: scale(1.1); }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{name}</h1>
        <p>Admin Dashboard & Booking Management</p>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="totalBookings">0</div>
                <div class="stat-label">Total Bookings</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="todayBookings">0</div>
                <div class="stat-label">Today's Bookings</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="weekBookings">0</div>
                <div class="stat-label">This Week</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pendingBookings">0</div>
                <div class="stat-label">Pending</div>
            </div>
        </div>

        <div class="bookings">
            <div class="bookings-header">
                <h2>Recent Booking Requests</h2>
            </div>
            <div id="bookingsList">
                <div class="no-bookings">
                    <div class="no-bookings-icon">📅</div>
                    <div>No booking requests yet</div>
                    <div style="margin-top: 10px; font-size: 0.9rem;">Bookings will appear here automatically</div>
                </div>
            </div>
        </div>
    </div>

    <button class="refresh-btn" onclick="loadBookings()" title="Refresh Data">🔄</button>

    <script>
        function loadBookings() {{
            const allBookings = JSON.parse(localStorage.getItem('website_bookings') || '[]');
            const businessBookings = allBookings.filter(b => b.business === '{name}');

            // Update statistics
            document.getElementById('totalBookings').textContent = businessBookings.length;

            const today = new Date().toDateString();
            const todayCount = businessBookings.filter(b =>
                new Date(b.createdAt).toDateString() === today
            ).length;
            document.getElementById('todayBookings').textContent = todayCount;

            const weekAgo = new Date();
            weekAgo.setDate(weekAgo.getDate() - 7);
            const weekCount = businessBookings.filter(b =>
                new Date(b.createdAt) >= weekAgo
            ).length;
            document.getElementById('weekBookings').textContent = weekCount;

            const pendingCount = businessBookings.filter(b => b.status === 'pending').length;
            document.getElementById('pendingBookings').textContent = pendingCount;

            // Display bookings
            const bookingsList = document.getElementById('bookingsList');
            if (businessBookings.length === 0) {{
                bookingsList.innerHTML = `
                    <div class="no-bookings">
                        <div class="no-bookings-icon">📅</div>
                        <div>No booking requests yet</div>
                        <div style="margin-top: 10px; font-size: 0.9rem;">Bookings will appear here automatically</div>
                    </div>
                `;
            }} else {{
                bookingsList.innerHTML = businessBookings
                    .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
                    .map(booking => `
                        <div class="booking-item">
                            <div class="booking-header">
                                <div class="booking-name">${{booking.name}}</div>
                                <div class="booking-status">${{booking.status.toUpperCase()}}</div>
                            </div>
                            <div class="booking-details">
                                <strong>Contact:</strong> ${{booking.phone}} | ${{booking.email}}<br>
                                <strong>Service:</strong> ${{booking.service}} | <strong>Date:</strong> ${{booking.date}}<br>
                                <strong>Requested:</strong> ${{new Date(booking.createdAt).toLocaleString()}}
                                ${{booking.message ? `<br><strong>Message:</strong> "${{booking.message}}"` : ''}}
                            </div>
                        </div>
                    `).join('');
            }}
        }}

        // Load data immediately
        loadBookings();

        // Auto-refresh every 5 seconds
        setInterval(loadBookings, 5000);
    </script>
</body>
</html>"""

        # Save files
        with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
            f.write(html)

        with open(f"{folder}/admin.html", "w", encoding="utf-8") as f:
            f.write(admin)

        return folder

    def run_demo(self):
        """Run demonstration with sample websites"""
        print("Website Maker - Automated Website Generator")
        print("=" * 50)
        print()

        demo_sites = [
            ("Elite Law Firm", "legal services", ["Corporate Law", "Litigation", "Real Estate"], "02-1234-5678", "contact@elitelaw.co.kr", "Seoul, Gangnam-gu"),
            ("Gourmet Bakery", "bakery cafe", ["Artisan Bread", "Custom Cakes", "Fresh Pastries"], "010-2345-6789", "orders@gourmetbakery.com", "Busan, Haeundae-gu"),
            ("Tech Repair Shop", "electronics repair", ["iPhone Repair", "Laptop Service", "Data Recovery"], "031-3456-7890", "info@techrepair.kr", "Incheon, Yeonsu-gu")
        ]

        for i, (name, btype, keywords, phone, email, address) in enumerate(demo_sites, 1):
            print(f"Creating website {i}/3: {name}")
            folder = self.create_website(name, btype, keywords, phone, email, address)
            print(f"Created: {folder}")
            print()

        print("All demo websites created successfully!")
        print()
        print("Each website includes:")
        print("- Responsive homepage with professional design")
        print("- Booking system with form validation")
        print("- Real-time admin panel with statistics")
        print("- LocalStorage data persistence")
        print("- Mobile-friendly responsive layout")
        print()
        print("To view: Open the index.html file in any browser")
        print("To manage: Open the admin.html file for booking management")

if __name__ == "__main__":
    maker = WebsiteMaker()
    maker.run_demo()