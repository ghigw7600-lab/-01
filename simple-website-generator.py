#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Website Generator
Creates complete websites based on keyword input without Unicode console issues
"""

import os
import json
from datetime import datetime

def generate_website(business_name, business_type, keywords, phone, email, address):
    """Generate a complete website based on input parameters"""

    # Create directory
    folder_name = f"{business_name.lower().replace(' ', '-')}-website"
    os.makedirs(folder_name, exist_ok=True)

    # Color schemes for different business types
    color_schemes = {
        "cafe": {"primary": "#d35400", "secondary": "#f39c12", "accent": "#e67e22"},
        "restaurant": {"primary": "#c0392b", "secondary": "#e74c3c", "accent": "#ec7063"},
        "shop": {"primary": "#8e44ad", "secondary": "#9b59b6", "accent": "#bb8fce"},
        "service": {"primary": "#2980b9", "secondary": "#3498db", "accent": "#7fb3d3"},
        "healthcare": {"primary": "#27ae60", "secondary": "#2ecc71", "accent": "#7dcea0"},
        "beauty": {"primary": "#e91e63", "secondary": "#f06292", "accent": "#f8bbd9"},
        "default": {"primary": "#34495e", "secondary": "#5d6d7e", "accent": "#85929e"}
    }

    colors = color_schemes.get(business_type.lower(), color_schemes["default"])

    # Generate main HTML
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - {business_type.title()}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }}

        .hero {{
            background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
            color: white;
            padding: 100px 0;
            text-align: center;
        }}
        .hero h1 {{ font-size: 3rem; margin-bottom: 1rem; font-weight: 300; }}
        .hero p {{ font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9; }}
        .hero .keywords {{ font-size: 1rem; opacity: 0.8; margin-bottom: 2rem; }}

        .btn {{
            background: {colors['accent']};
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
            cursor: pointer;
        }}
        .btn:hover {{ transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .section {{ padding: 60px 0; }}

        .services {{ background: #f8f9fa; }}
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }}
        .service-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        .service-card:hover {{ transform: translateY(-5px); }}

        .booking {{
            background: linear-gradient(135deg, {colors['secondary']} 0%, {colors['primary']} 100%);
            color: white;
        }}
        .booking-form {{
            max-width: 600px;
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
        .form-group {{ margin-bottom: 20px; }}
        .form-group label {{ display: block; margin-bottom: 5px; font-weight: 500; }}
        .form-group input, .form-group textarea, .form-group select {{
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: rgba(255,255,255,0.9);
        }}

        .contact {{
            background: #2c3e50;
            color: white;
        }}
        .contact-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }}
        .contact-item {{
            text-align: center;
            padding: 20px;
        }}

        .admin-link {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: {colors['primary']};
            color: white;
            padding: 15px;
            border-radius: 50px;
            text-decoration: none;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
            .hero p {{ font-size: 1rem; }}
            .container {{ padding: 0 15px; }}
        }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{business_name}</h1>
            <p>Professional {business_type} services</p>
            <div class="keywords">{' • '.join(keywords)}</div>
            <a href="#booking" class="btn">Book Now</a>
        </div>
    </section>

    <section class="services section">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>Premium Service</h3>
                    <p>High-quality {business_type} service tailored to your needs</p>
                </div>
                <div class="service-card">
                    <h3>Professional Team</h3>
                    <p>Experienced professionals dedicated to excellence</p>
                </div>
                <div class="service-card">
                    <h3>Customer Satisfaction</h3>
                    <p>Your satisfaction is our top priority</p>
                </div>
            </div>
        </div>
    </section>

    <section id="booking" class="booking section">
        <div class="container">
            <h2>Book Your Service</h2>
            <form class="booking-form" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="service">Service Type</label>
                    <select id="service" name="service" required>
                        <option value="">Select Service</option>
                        <option value="basic">Basic Service</option>
                        <option value="premium">Premium Service</option>
                        <option value="custom">Custom Service</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="date">Preferred Date</label>
                    <input type="date" id="date" name="date" required>
                </div>
                <div class="form-group">
                    <label for="message">Additional Notes</label>
                    <textarea id="message" name="message" rows="4"></textarea>
                </div>
                <button type="submit" class="btn">Submit Booking</button>
            </form>
        </div>
    </section>

    <section class="contact section">
        <div class="container">
            <h2>Contact Information</h2>
            <div class="contact-info">
                <div class="contact-item">
                    <h3>Phone</h3>
                    <p>{phone}</p>
                </div>
                <div class="contact-item">
                    <h3>Email</h3>
                    <p>{email}</p>
                </div>
                <div class="contact-item">
                    <h3>Address</h3>
                    <p>{address}</p>
                </div>
            </div>
        </div>
    </section>

    <a href="admin.html" class="admin-link">Admin</a>

    <script>
        function submitBooking(event) {{
            event.preventDefault();

            const formData = new FormData(event.target);
            const booking = {{
                id: Date.now() + Math.random(),
                name: formData.get('name'),
                phone: formData.get('phone'),
                email: formData.get('email'),
                service: formData.get('service'),
                date: formData.get('date'),
                message: formData.get('message'),
                createdAt: new Date().toISOString(),
                business: '{business_name}',
                type: '{business_type}'
            }};

            // Save to localStorage
            const bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            bookings.push(booking);
            localStorage.setItem('bookings', JSON.stringify(bookings));

            alert('Booking submitted successfully!');
            event.target.reset();
        }}
    </script>
</body>
</html>"""

    # Generate admin panel
    admin_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - Admin Panel</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f6fa; }}

        .header {{
            background: {colors['primary']};
            color: white;
            padding: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header h1 {{ text-align: center; }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .stat-number {{ font-size: 2rem; font-weight: bold; color: {colors['primary']}; }}
        .stat-label {{ color: #666; margin-top: 5px; }}

        .bookings {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .bookings-header {{
            background: {colors['secondary']};
            color: white;
            padding: 20px;
        }}
        .booking-item {{
            padding: 20px;
            border-bottom: 1px solid #eee;
        }}
        .booking-item:last-child {{ border-bottom: none; }}
        .booking-name {{ font-weight: bold; font-size: 1.1rem; }}
        .booking-details {{ color: #666; margin-top: 5px; }}
        .booking-date {{ color: {colors['primary']}; font-weight: 500; }}

        .no-bookings {{
            text-align: center;
            padding: 40px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{business_name} Admin Panel</h1>
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
                <div class="stat-number" id="thisWeekBookings">0</div>
                <div class="stat-label">This Week</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pendingBookings">0</div>
                <div class="stat-label">Pending</div>
            </div>
        </div>

        <div class="bookings">
            <div class="bookings-header">
                <h2>Recent Bookings</h2>
            </div>
            <div id="bookingsList">
                <div class="no-bookings">No bookings yet</div>
            </div>
        </div>
    </div>

    <script>
        function loadBookings() {{
            const bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            const businessBookings = bookings.filter(b => b.business === '{business_name}');

            // Update statistics
            document.getElementById('totalBookings').textContent = businessBookings.length;

            const today = new Date().toDateString();
            const todayBookings = businessBookings.filter(b =>
                new Date(b.createdAt).toDateString() === today
            );
            document.getElementById('todayBookings').textContent = todayBookings.length;

            const weekAgo = new Date();
            weekAgo.setDate(weekAgo.getDate() - 7);
            const thisWeekBookings = businessBookings.filter(b =>
                new Date(b.createdAt) >= weekAgo
            );
            document.getElementById('thisWeekBookings').textContent = thisWeekBookings.length;

            document.getElementById('pendingBookings').textContent = businessBookings.length;

            // Display bookings
            const bookingsList = document.getElementById('bookingsList');
            if (businessBookings.length === 0) {{
                bookingsList.innerHTML = '<div class="no-bookings">No bookings yet</div>';
            }} else {{
                bookingsList.innerHTML = businessBookings
                    .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
                    .map(booking => `
                        <div class="booking-item">
                            <div class="booking-name">${{booking.name}}</div>
                            <div class="booking-details">
                                Phone: ${{booking.phone}} | Email: ${{booking.email}}<br>
                                Service: ${{booking.service}} | Date: ${{booking.date}}
                            </div>
                            <div class="booking-date">
                                Booked: ${{new Date(booking.createdAt).toLocaleString()}}
                            </div>
                            ${{booking.message ? `<div style="margin-top: 5px; font-style: italic;">"${{booking.message}}"</div>` : ''}}
                        </div>
                    `).join('');
            }}
        }}

        // Load bookings on page load
        loadBookings();

        // Refresh every 3 seconds
        setInterval(loadBookings, 3000);
    </script>
</body>
</html>"""

    # Save files
    with open(f"{folder_name}/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    with open(f"{folder_name}/admin.html", "w", encoding="utf-8") as f:
        f.write(admin_content)

    # Create info file
    info = {
        "business_name": business_name,
        "business_type": business_type,
        "keywords": keywords,
        "contact": {
            "phone": phone,
            "email": email,
            "address": address
        },
        "created": datetime.now().isoformat(),
        "files": ["index.html", "admin.html"]
    }

    with open(f"{folder_name}/info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    return folder_name

def main():
    """Main function to run the generator"""
    print("=== Simple Website Generator ===")
    print("Create a complete website in seconds!")
    print()

    # Get input
    business_name = input("Business Name: ").strip()
    business_type = input("Business Type (cafe/restaurant/shop/service/healthcare/beauty): ").strip()
    keywords_input = input("Keywords (comma-separated): ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    keywords = [k.strip() for k in keywords_input.split(',')]

    # Generate website
    print(f"\\nGenerating website for {business_name}...")
    folder_name = generate_website(business_name, business_type, keywords, phone, email, address)

    print(f"\\nWebsite created successfully!")
    print(f"Folder: {folder_name}")
    print(f"Homepage: {folder_name}/index.html")
    print(f"Admin Panel: {folder_name}/admin.html")
    print("\\nOpen index.html in your browser to view the website!")

if __name__ == "__main__":
    main()