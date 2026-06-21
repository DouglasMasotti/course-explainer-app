from flask import render_template
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    course = courses[int(course_id) - 1]
    return render_template('course.html', course=course)

def contact_page():
    contact = {
        'name': 'Douglas Masotti',
        'email': 'dmasotti@adobe.com',
        'address': 'San Francisco, CA\nUnited States',
    }
    social_links = [
        {
            'platform': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/douglasmasotti',
            'aria_label': 'LinkedIn profile, opens in new tab',
        },
        {
            'platform': 'GitHub',
            'url': 'https://github.com/douglasmasotti',
            'aria_label': 'GitHub profile, opens in new tab',
        },
        {
            'platform': 'Twitter/X',
            'url': 'https://x.com/douglasmasotti',
            'aria_label': 'Twitter/X profile, opens in new tab',
        },
        {
            'platform': 'Instagram',
            'url': 'https://www.instagram.com/douglasmasotti',
            'aria_label': 'Instagram profile, opens in new tab',
        },
    ]
    return render_template('contact.html', contact=contact, social_links=social_links)
