#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demo Website Auto Generator
Creates sample websites to demonstrate the system
"""

import os
import json
import webbrowser
from datetime import datetime
from pathlib import Path

def create_demo_websites():
    """Create demo websites for demonstration"""

    # Demo configurations
    demo_configs = [
        {
            'business_name': 'Sunny Cafe',
            'type': 'restaurant',
            'color': 'warm',
            'icon': '☕',
            'keywords': ['coffee', 'dessert', 'brunch', 'cafe'],
            'phone': '010-1234-5678',
            'email': 'info@sunnycafe.com',
            'address': 'Seoul, Gangnam-gu',
            'services': ['Premium Coffee', 'Fresh Desserts', 'Healthy Brunch']
        },
        {
            'business_name': 'SmileCare Dental',
            'type': 'medical',
            'color': 'medical',
            'icon': '🦷',
            'keywords': ['dental', 'implant', 'orthodontics', 'cleaning'],
            'phone': '010-9876-5432',
            'email': 'info@smilecare.com',
            'address': 'Seoul, Seocho-gu',
            'services': ['Dental Implants', 'Orthodontics', 'Dental Cleaning']
        },
        {
            'business_name': 'TechShop Store',
            'type': 'ecommerce',
            'color': 'tech',
            'icon': '💻',
            'keywords': ['electronics', 'gadgets', 'computers', 'phones'],
            'phone': '010-5555-6666',
            'email': 'sales@techshop.com',
            'address': 'Seoul, Yongsan-gu',
            'services': ['Product Sales', 'Express Delivery', '24/7 Support']
        }
    ]

    created_sites = []

    for i, config in enumerate(demo_configs, 1):
        print(f"Creating demo website {i}: {config['business_name']}")

        try:
            project_path = create_website(config)
            created_sites.append({
                'name': config['business_name'],
                'path': project_path,
                'type': config['type']
            })
            print(f"✅ {config['business_name']} website created successfully!")

        except Exception as e:
            print(f"❌ Error creating {config['business_name']}: {e}")

    return created_sites

def get_color_scheme(color_name):
    """Return color scheme."""
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
    """Generate HTML template."""
    colors = get_color_scheme(config['color'])

    # Generate service cards
    service_cards = ""
    icons = ['⭐', '🎯', '💎']
    for i, service in enumerate(config['services']):
        icon = icons[i] if i < len(icons) else '🏢'
        service_cards += f"""
                <div class="service-card">
                    <div class="service-icon">{icon}</div>
                    <h3>{service}</h3>
                    <p>We provide excellent {service.lower()} for customer satisfaction</p>
                </div>"""

    # Generate service options
    service_options = ""
    for service in config['services']:
        service_options += f'<option value="{service}">{service}</option>'

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['business_name']} - {', '.join(config['keywords'])}</title>
    <meta name="description" content="{config['business_name']} provides {', '.join(config['keywords'])} services.">
    <meta name="keywords" content="{', '.join(config['keywords'])}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>{config['icon']}</text></svg>" />
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Apple System', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.6; color: {colors['primary']}; }}

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

        /* Demo Badge */
        .demo-badge {{ position: fixed; top: 20px; right: 20px; background: #ff6b6b; color: white; padding: 10px 15px; border-radius: 25px; font-size: 0.9rem; font-weight: 600; z-index: 1001; box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3); }}

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
    <div class="demo-badge">🚀 Auto Generated Demo</div>

    <header>
        <nav>
            <div class="logo">{config['icon']} {config['business_name']}</div>
            <ul class="nav-menu">
                <li class="nav-item"><a href="#home">Home</a></li>
                <li class="nav-item"><a href="#services">Services</a></li>
                <li class="nav-item"><a href="#booking">Booking</a></li>
                <li class="nav-item"><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero" id="home">
        <div class="hero-content">
            <h1>{config['business_name']}</h1>
            <p>Professional {', '.join(config['keywords'])} services</p>
            <a href="#booking" class="cta-button">Book Now</a>
        </div>
    </section>

    <section class="services" id="services">
        <div class="container">
            <div class="section-title">
                <h2>Our Services</h2>
                <p>High-quality services for your needs</p>
            </div>
            <div class="services-grid">{service_cards}
            </div>
        </div>
    </section>

    <section class="booking" id="booking">
        <div class="container">
            <div class="section-title">
                <h2>Book Our Services</h2>
                <p>Easy and convenient booking process</p>
            </div>
            <form class="booking-form" id="bookingForm">
                <div class="form-grid">
                    <div class="form-group">
                        <label>Name</label>
                        <input type="text" name="name" required placeholder="Your name">
                    </div>
                    <div class="form-group">
                        <label>Phone</label>
                        <input type="tel" name="phone" required placeholder="Your phone number">
                    </div>
                </div>
                <div class="form-group">
                    <label>Service</label>
                    <select name="service" required>
                        <option value="">Select service</option>
                        {service_options}
                    </select>
                </div>
                <div class="form-group">
                    <label>Preferred Date</label>
                    <input type="date" name="date" required>
                </div>
                <div class="form-group">
                    <label>Special Requests</label>
                    <textarea name="message" rows="4" placeholder="Any special requests or notes"></textarea>
                </div>
                <button type="submit" class="cta-button" style="width: 100%;">Submit Booking</button>
            </form>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="container">
            <div class="section-title">
                <h2>Contact Us</h2>
                <p>Get in touch with us anytime</p>
            </div>
            <div class="contact-info">
                <div class="contact-item">
                    <h3>📞 Phone</h3>
                    <p>{config['phone']}</p>
                </div>
                <div class="contact-item">
                    <h3>📧 Email</h3>
                    <p>{config['email']}</p>
                </div>
                <div class="contact-item">
                    <h3>📍 Address</h3>
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
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});

        // Booking form handling
        document.getElementById('bookingForm').addEventListener('submit', function(e) {{
            e.preventDefault();

            const formData = new FormData(this);
            const bookingData = {{
                name: formData.get('name'),
                phone: formData.get('phone'),
                service: formData.get('service'),
                date: formData.get('date'),
                message: formData.get('message'),
                status: 'Pending',
                orderId: Date.now(),
                createdAt: new Date().toISOString()
            }};

            // Save to LocalStorage
            const existingBookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            existingBookings.push({{ ...bookingData, id: Date.now() + Math.random() }});
            localStorage.setItem('bookings', JSON.stringify(existingBookings));

            alert('🎉 Booking submitted successfully! This is a demo - no actual booking was made.');
            this.reset();
        }});

        // Set minimum date to today
        document.querySelector('input[type="date"]').min = new Date().toISOString().split('T')[0];
    </script>
</body>
</html>"""

    return template

def generate_admin_template(config):
    """Generate admin page template."""
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['business_name']} - Admin Panel</title>
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
        .demo-badge {{ position: fixed; top: 20px; right: 20px; background: #ff6b6b; color: white; padding: 10px 15px; border-radius: 25px; font-size: 0.9rem; font-weight: 600; z-index: 1001; }}
    </style>
</head>
<body>
    <div class="demo-badge">🚀 Demo Admin Panel</div>

    <div class="login-container" id="loginSection">
        <h2>🔐 {config['business_name']} Admin</h2>
        <input type="text" class="login-input" placeholder="Username" id="username" value="admin">
        <input type="password" class="login-input" placeholder="Password" id="password" value="admin123">
        <button class="login-btn" onclick="login()">Login</button>
        <p style="margin-top: 15px; font-size: 0.9rem; color: #95a5a6;">Username: admin / Password: admin123</p>
    </div>

    <div class="dashboard" id="dashboard">
        <div class="dashboard-header">
            <h1>📊 {config['business_name']} Admin Dashboard</h1>
            <button class="logout-btn" onclick="logout()">Logout</button>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <h3 id="total-bookings">0</h3>
                <p>Total Bookings</p>
            </div>
            <div class="stat-card">
                <h3 id="pending-bookings">0</h3>
                <p>Pending Bookings</p>
            </div>
            <div class="stat-card">
                <h3 id="completed-bookings">0</h3>
                <p>Completed Bookings</p>
            </div>
        </div>

        <div class="management-card">
            <h3>📋 Booking Management</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Customer</th>
                        <th>Phone</th>
                        <th>Service</th>
                        <th>Status</th>
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
                alert('❌ Invalid username or password.');
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
            document.getElementById('pending-bookings').textContent = bookings.filter(b => b.status === 'Pending').length;
            document.getElementById('completed-bookings').textContent = bookings.filter(b => b.status === 'Completed').length;

            bookings.forEach(booking => {{
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${{booking.date}}</td>
                    <td>${{booking.name}}</td>
                    <td>${{booking.phone}}</td>
                    <td>${{booking.service}}</td>
                    <td><span class="status-badge status-${{booking.status === 'Pending' ? 'pending' : 'completed'}}">${{booking.status}}</span></td>
                `;
            }});
        }}

        // Check login status
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
    """Create the website."""
    # Create project folder
    project_name = config['business_name'].lower().replace(' ', '-')
    project_path = Path(f"{project_name}-website")
    project_path.mkdir(exist_ok=True)

    # Generate HTML files
    main_html = generate_html_template(config)
    admin_html = generate_admin_template(config)

    # Save files
    (project_path / "index.html").write_text(main_html, encoding='utf-8')
    (project_path / "admin.html").write_text(admin_html, encoding='utf-8')

    # Generate package.json
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": f"{config['business_name']} website",
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

    # Generate README.md
    readme_content = f"""# {config['business_name']} Website

Official website for {config['business_name']} providing {', '.join(config['keywords'])} services.

## Features
- Responsive web design
- Booking system
- Admin panel
- Real-time data sync

## How to run
```bash
npm install
npm start
```

## Admin Access
- URL: /admin.html
- Username: admin
- Password: admin123

---
Generated with Auto Website Generator
"""

    (project_path / "README.md").write_text(readme_content, encoding='utf-8')

    return project_path

def main():
    """Main function"""
    print("🚀 Demo Website Auto Generator")
    print("=" * 50)
    print()
    print("Creating 3 demo websites...")
    print()

    created_sites = create_demo_websites()

    print("\n" + "=" * 50)
    print("    ✅ Demo Websites Created Successfully!")
    print("=" * 50)
    print()

    for site in created_sites:
        print(f"📁 {site['name']}: {site['path']}")
        print(f"   🌐 Main: {site['path']}/index.html")
        print(f"   🔧 Admin: {site['path']}/admin.html")
        print()

    # Generate summary
    summary_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Websites Created - Auto Generator</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; max-width: 1000px; margin: 0 auto; padding: 2rem; background: #f8f9fa; }}
        .card {{ background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 2rem; }}
        .success {{ background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; text-align: center; }}
        h1 {{ margin-bottom: 1rem; }}
        h2 {{ color: #495057; margin-bottom: 1rem; }}
        .sites-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
        .site-card {{ background: white; border: 2px solid #007bff; border-radius: 10px; padding: 1.5rem; text-align: center; }}
        .site-card h3 {{ color: #007bff; margin-bottom: 1rem; }}
        .links {{ display: flex; gap: 1rem; margin-top: 1rem; }}
        .link-btn {{ flex: 1; background: #007bff; color: white; padding: 0.8rem; border-radius: 8px; text-decoration: none; text-align: center; transition: transform 0.3s; }}
        .link-btn:hover {{ transform: translateY(-2px); }}
        .admin-btn {{ background: #6f42c1; }}
        .features {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 2rem; }}
        .feature {{ text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px; }}
    </style>
</head>
<body>
    <div class="card success">
        <h1>🎉 Demo Websites Created!</h1>
        <p>3 sample websites have been automatically generated to demonstrate the system.</p>
    </div>

    <div class="card">
        <h2>🌟 Generated Demo Sites</h2>
        <div class="sites-grid">"""

    for site in created_sites:
        summary_html += f"""
            <div class="site-card">
                <h3>{site['name']}</h3>
                <p>Type: {site['type'].title()}</p>
                <div class="links">
                    <a href="{site['path']}/index.html" class="link-btn">🌐 Website</a>
                    <a href="{site['path']}/admin.html" class="link-btn admin-btn">🔧 Admin</a>
                </div>
            </div>"""

    summary_html += f"""
        </div>
    </div>

    <div class="card">
        <h2>✨ Key Features Demonstrated</h2>
        <div class="features">
            <div class="feature">
                <h4>🎨 Multi-Theme Support</h4>
                <p>Different color schemes for different business types</p>
            </div>
            <div class="feature">
                <h4>📱 Responsive Design</h4>
                <p>Works perfectly on all devices</p>
            </div>
            <div class="feature">
                <h4>📋 Booking System</h4>
                <p>Integrated booking forms with validation</p>
            </div>
            <div class="feature">
                <h4>🔧 Admin Panel</h4>
                <p>Complete admin dashboard (admin/admin123)</p>
            </div>
            <div class="feature">
                <h4>💾 Data Storage</h4>
                <p>LocalStorage for booking management</p>
            </div>
            <div class="feature">
                <h4>🚀 Auto Generation</h4>
                <p>Created from keywords in seconds</p>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>🔧 How It Works</h2>
        <ol>
            <li><strong>Input Keywords:</strong> Business name, type, contact info</li>
            <li><strong>Auto Design:</strong> Color scheme and layout selection</li>
            <li><strong>Generate Files:</strong> HTML, CSS, JS all created automatically</li>
            <li><strong>Ready to Deploy:</strong> Upload to GitHub → Netlify → Live!</li>
        </ol>

        <h3 style="margin-top: 2rem;">🎯 Perfect For:</h3>
        <ul>
            <li>Small businesses needing quick web presence</li>
            <li>Restaurants, cafes, local services</li>
            <li>Medical practices, dental clinics</li>
            <li>E-commerce stores</li>
            <li>Service providers</li>
        </ul>
    </div>

    <div class="card">
        <h2>📱 Test the System</h2>
        <p>Try booking on any of the demo sites above, then check the admin panel to see real-time data sync!</p>
        <p><strong>Admin Login:</strong> admin / admin123</p>
    </div>
</body>
</html>"""

    with open('blog_output.html', 'w', encoding='utf-8') as f:
        f.write(summary_html)

    print(f"📄 Demo summary saved to: blog_output.html")

    # Open the first demo site
    if created_sites:
        webbrowser.open(str(created_sites[0]['path'] / "index.html"))
        webbrowser.open('blog_output.html')

if __name__ == "__main__":
    main()