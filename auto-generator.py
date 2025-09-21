#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

def create_website(business_name, business_type, keywords, phone, email, address):
    """Create a complete website with booking system and admin panel"""

    # Create folder
    folder_name = f"{business_name.lower().replace(' ', '-')}-website"
    os.makedirs(folder_name, exist_ok=True)

    # Main website HTML
    index_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - Professional {business_type}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .hero {{ background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; padding: 100px 0; text-align: center; }}
        .hero h1 {{ font-size: 3rem; margin-bottom: 1rem; }}
        .hero p {{ font-size: 1.2rem; margin-bottom: 2rem; }}
        .btn {{ background: #e67e22; color: white; padding: 15px 30px; border: none; border-radius: 25px; text-decoration: none; display: inline-block; cursor: pointer; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .section {{ padding: 60px 0; }}
        .services {{ background: #f8f9fa; }}
        .booking {{ background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); color: white; }}
        .booking-form {{ max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 40px; border-radius: 15px; }}
        .form-group {{ margin-bottom: 20px; }}
        .form-group label {{ display: block; margin-bottom: 5px; }}
        .form-group input, .form-group select, .form-group textarea {{ width: 100%; padding: 12px; border: none; border-radius: 8px; }}
        .contact {{ background: #2c3e50; color: white; }}
        .admin-link {{ position: fixed; bottom: 20px; right: 20px; background: #e74c3c; color: white; padding: 15px; border-radius: 50px; text-decoration: none; }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{business_name}</h1>
            <p>Professional {business_type} Services</p>
            <div style="margin: 20px 0;">Specializing in: {' • '.join(keywords)}</div>
            <a href="#booking" class="btn">Book Service</a>
        </div>
    </section>

    <section class="services section">
        <div class="container">
            <h2>Our Services</h2>
            <p>We provide excellent {business_type} services with years of experience.</p>
        </div>
    </section>

    <section id="booking" class="booking section">
        <div class="container">
            <h2>Book Your Service</h2>
            <form class="booking-form" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label>Name</label>
                    <input type="text" name="name" required>
                </div>
                <div class="form-group">
                    <label>Phone</label>
                    <input type="tel" name="phone" required>
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" required>
                </div>
                <div class="form-group">
                    <label>Service Type</label>
                    <select name="service" required>
                        <option value="">Select Service</option>
                        <option value="basic">Basic Service</option>
                        <option value="premium">Premium Service</option>
                        <option value="consultation">Consultation</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Preferred Date</label>
                    <input type="date" name="date" required>
                </div>
                <div class="form-group">
                    <label>Message</label>
                    <textarea name="message" rows="4"></textarea>
                </div>
                <button type="submit" class="btn">Submit Booking</button>
            </form>
        </div>
    </section>

    <section class="contact section">
        <div class="container">
            <h2>Contact Information</h2>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Address:</strong> {address}</p>
        </div>
    </section>

    <a href="admin.html" class="admin-link">Admin</a>

    <script>
        function submitBooking(event) {{
            event.preventDefault();
            const formData = new FormData(event.target);
            const booking = {{
                id: Date.now(),
                name: formData.get('name'),
                phone: formData.get('phone'),
                email: formData.get('email'),
                service: formData.get('service'),
                date: formData.get('date'),
                message: formData.get('message'),
                createdAt: new Date().toISOString(),
                business: '{business_name}',
                status: 'pending'
            }};

            const bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            bookings.push(booking);
            localStorage.setItem('bookings', JSON.stringify(bookings));

            alert('Booking submitted successfully!');
            event.target.reset();
        }}
    </script>
</body>
</html>"""

    # Admin panel HTML
    admin_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - Admin Panel</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Arial, sans-serif; background: #f5f6fa; }}
        .header {{ background: #2c3e50; color: white; padding: 20px 0; text-align: center; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: white; padding: 25px; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .stat-number {{ font-size: 2rem; font-weight: bold; color: #e74c3c; }}
        .bookings {{ background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .bookings-header {{ background: #3498db; color: white; padding: 20px; }}
        .booking-item {{ padding: 20px; border-bottom: 1px solid #eee; }}
        .booking-name {{ font-weight: bold; }}
        .booking-details {{ color: #666; margin-top: 5px; }}
        .no-bookings {{ text-align: center; padding: 40px; color: #666; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{business_name} Admin Panel</h1>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="total">0</div>
                <div>Total Bookings</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="today">0</div>
                <div>Today</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pending">0</div>
                <div>Pending</div>
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
        function loadData() {{
            const bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            const businessBookings = bookings.filter(b => b.business === '{business_name}');

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
                bookingsList.innerHTML = '<div class="no-bookings">No bookings yet</div>';
            }} else {{
                bookingsList.innerHTML = businessBookings
                    .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
                    .map(b => `
                        <div class="booking-item">
                            <div class="booking-name">${{b.name}}</div>
                            <div class="booking-details">
                                ${{b.phone}} | ${{b.email}}<br>
                                Service: ${{b.service}} | Date: ${{b.date}}<br>
                                Booked: ${{new Date(b.createdAt).toLocaleString()}}
                                ${{b.message ? '<br>Note: ' + b.message : ''}}
                            </div>
                        </div>
                    `).join('');
            }}
        }}

        loadData();
        setInterval(loadData, 3000);
    </script>
</body>
</html>"""

    # Save files
    with open(f"{folder_name}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    with open(f"{folder_name}/admin.html", "w", encoding="utf-8") as f:
        f.write(admin_html)

    # Create info file
    info = {
        "business_name": business_name,
        "business_type": business_type,
        "keywords": keywords,
        "contact": {"phone": phone, "email": email, "address": address},
        "created": datetime.now().isoformat()
    }

    with open(f"{folder_name}/info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    return folder_name

# Demo generation
if __name__ == "__main__":
    demos = [
        ("Smart Dental Clinic", "dental clinic", ["Implants", "Cleaning", "Orthodontics"], "010-1234-5678", "info@smartdental.com", "Seoul, Gangnam-gu"),
        ("Green Fitness Center", "fitness center", ["Personal Training", "Group Classes", "Nutrition"], "010-2345-6789", "contact@greenfitness.com", "Seoul, Mapo-gu"),
        ("Cozy Pet Hotel", "pet care", ["Pet Boarding", "Grooming", "Training"], "010-3456-7890", "hello@cozypet.com", "Seoul, Songpa-gu")
    ]

    print("=== Automated Website Generator ===")
    for name, btype, keywords, phone, email, address in demos:
        folder = create_website(name, btype, keywords, phone, email, address)
        print(f"Created: {folder}")

    print("\nAll websites generated successfully!")
    print("Each website includes:")
    print("- Responsive homepage with booking system")
    print("- Admin panel with real-time statistics")
    print("- LocalStorage data persistence")
    print("- Professional design and functionality")