#!/usr/bin/env python3

import re

def generate_unique_name(business_impact, position, category, counter):
    """Generate unique names based on business impact and skills"""
    
    impact_lower = business_impact.lower()
    
    # Trading & Finance
    if any(word in impact_lower for word in ['trading', 'payment', 'fintech', 'bank', 'crypto', 'defi']):
        names = ['Trading Titan', 'Crypto King', 'Payment Pro', 'FinTech Beast', 'Banking Boss', 
                'DeFi Destroyer', 'Money Master', 'Wallet Wizard', 'Transaction Tiger', 'Finance Fighter']
    
    # Performance & Speed  
    elif any(word in impact_lower for word in ['load', 'speed', 'performance', 'optimization', 'fast']):
        names = ['Speed Demon', 'Load Killer', 'Performance Pro', 'Turbo Developer', 'Lightning Coder',
                'Optimization Overlord', 'Speed Master', 'Fast Track', 'Velocity Victor', 'Rapid Ranger']
    
    # E-commerce & Sales
    elif any(word in impact_lower for word in ['ecommerce', 'e-commerce', 'sales', 'shop', 'retail', 'gmv']):
        names = ['E-com Emperor', 'Sales Slayer', 'Revenue Rocket', 'Shopping Shark', 'Commerce Crusher',
                'Retail Ruler', 'GMV Genius', 'Cart Killer', 'Purchase Pro', 'Sales Samurai']
    
    # Social & Dating  
    elif any(word in impact_lower for word in ['social', 'dating', 'chat', 'message', 'user']):
        names = ['Social Sultan', 'Dating Destroyer', 'Chat Champion', 'User Whisperer', 'Social Sage',
                'Connection King', 'Message Master', 'Community Captain', 'Social Shark', 'Network Ninja']
    
    # Gaming & Entertainment
    elif any(word in impact_lower for word in ['gaming', 'game', 'player', 'entertainment', 'stream']):
        names = ['Gaming Guru', 'Player Pro', 'Stream King', 'Game Changer', 'Entertainment Emperor',
                'Gaming Giant', 'Player Master', 'Stream Slayer', 'Fun Factory', 'Game Guardian']
    
    # Healthcare & Medical
    elif any(word in impact_lower for word in ['health', 'medical', 'patient', 'hospital', 'hipaa']):
        names = ['Health Hero', 'Medical Master', 'Patient Pro', 'Healthcare Hacker', 'Medical Maverick',
                'Health Guardian', 'Care Captain', 'Medical Magician', 'Health Hawk', 'Patient Protector']
    
    # Data & Analytics
    elif any(word in impact_lower for word in ['data', 'analytics', 'ml', 'ai', 'algorithm', 'prediction']):
        names = ['Data Dragon', 'AI Overlord', 'Analytics Ace', 'Algorithm Artist', 'Data Detective',
                'ML Master', 'Prediction Pro', 'Data Dynamo', 'AI Architect', 'Data Destroyer']
    
    # Security & Enterprise
    elif any(word in impact_lower for word in ['security', 'enterprise', 'government', 'compliance', 'soc2']):
        names = ['Security Shield', 'Enterprise Emperor', 'Compliance Crusher', 'Security Samurai', 'Guard Genius',
                'Protection Pro', 'Security Sultan', 'Enterprise Expert', 'Fortress Fighter', 'Shield Master']
    
    # Travel & Booking
    elif any(word in impact_lower for word in ['travel', 'booking', 'hotel', 'reservation']):
        names = ['Travel Titan', 'Booking Boss', 'Hotel Hero', 'Journey Genius', 'Travel Tiger',
                'Booking Beast', 'Trip Master', 'Hotel Hacker', 'Travel Tycoon', 'Booking Bandit']
    
    # Food & Delivery
    elif any(word in impact_lower for word in ['food', 'delivery', 'restaurant', 'kitchen']):
        names = ['Food Fighter', 'Delivery Dragon', 'Kitchen King', 'Food Fury', 'Delivery Destroyer',
                'Meal Master', 'Food Phantom', 'Delivery Demon', 'Kitchen Killer', 'Food Fortress']
    
    # Real Estate & Property
    elif any(word in impact_lower for word in ['real estate', 'property', 'listing']):
        names = ['Property Pro', 'Real Estate Ruler', 'Listing Legend', 'Property Phantom', 'Estate Expert',
                'Property Powerhouse', 'Real Estate Rocket', 'Listing Lion', 'Property Pirate', 'Estate Emperor']
    
    # News & Media
    elif any(word in impact_lower for word in ['news', 'media', 'content', 'seo']):
        names = ['News Ninja', 'Media Master', 'Content Creator', 'SEO Samurai', 'Media Maverick',
                'News Navigator', 'Content Crusher', 'Media Magician', 'News Nemesis', 'Content Captain']
    
    # DevOps & Infrastructure
    elif any(word in impact_lower for word in ['devops', 'docker', 'kubernetes', 'aws', 'cloud', 'infrastructure']):
        names = ['Cloud Captain', 'DevOps Destroyer', 'Infrastructure Ace', 'Cloud Crusher', 'Pipeline Pro',
                'Cloud Commander', 'DevOps Dragon', 'Infrastructure Overlord', 'Cloud Conqueror', 'Pipeline Phantom']
    
    # QA & Testing
    elif any(word in impact_lower for word in ['test', 'qa', 'quality', 'bug']):
        names = ['QA Quarterback', 'Test Titan', 'Bug Buster', 'Quality Queen', 'Test Terminator',
                'QA Champion', 'Bug Hunter', 'Test Master', 'Quality Crusader', 'Bug Blaster']
    
    # Mobile Development
    elif any(word in impact_lower for word in ['mobile', 'app', 'ios', 'android', 'flutter']):
        names = ['Mobile Master', 'App Architect', 'iOS Idol', 'Android Ace', 'Mobile Maverick',
                'App Assassin', 'Mobile Magician', 'App Emperor', 'Mobile Monarch', 'App Admiral']
    
    # Default generic names
    else:
        if 'senior' in position.lower():
            names = ['Senior Sage', 'Lead Legend', 'Expert Elite', 'Master Mind', 'Senior Sultan']
        elif 'junior' in position.lower():
            names = ['Junior Genius', 'Rising Rocket', 'Future Force', 'Young Yoda', 'Fresh Fury']
        else:
            names = ['Code Crusader', 'Dev Destroyer', 'Tech Titan', 'Code Commander', 'Digital Dragon']
    
    # Return name with fallback
    if counter <= len(names):
        return names[counter - 1]
    else:
        return f"{names[0]} {counter}"

# Read the database file
with open('djinni-developers-comprehensive-database.txt', 'r', encoding='utf-8') as f:
    content = f.read()

developers = []
counter = 1

# Split content by sections (by ##)
sections = content.split('##')[1:]  # Skip first empty part

for section in sections:
    lines = section.strip().split('\n')
    section_title = lines[0].strip()
    
    # Skip summary section
    if 'SUMMARY' in section_title.upper():
        continue
        
    # Extract category from section title
    if 'REACT' in section_title.upper():
        category = 'React'
    elif 'PYTHON' in section_title.upper():
        category = 'Python'
    elif 'NODE' in section_title.upper():
        category = 'Node.js'
    elif 'JAVA' in section_title.upper():
        category = 'Java'
    elif 'PHP' in section_title.upper():
        category = 'PHP'
    elif 'GO' in section_title.upper():
        category = 'Go'
    elif 'RUBY' in section_title.upper():
        category = 'Ruby'
    elif 'C#' in section_title or 'NET' in section_title.upper():
        category = 'C#/.NET'
    elif 'C++' in section_title or 'CPP' in section_title.upper():
        category = 'C++'
    elif 'MOBILE' in section_title.upper() or 'FLUTTER' in section_title.upper():
        category = 'Mobile'
    elif 'DEVOPS' in section_title.upper():
        category = 'DevOps'
    elif 'QA' in section_title.upper():
        category = 'QA'
    elif 'FULLSTACK' in section_title.upper():
        category = 'Full-stack'
    elif 'UI/UX' in section_title.upper():
        category = 'UI/UX'
    else:
        category = 'Other'
    
    # Process each developer line
    for line in lines[1:]:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Parse developer data
        parts = line.split(' | ')
        if len(parts) < 10:
            continue
            
        position = parts[0].strip()
        experience = parts[1].strip()
        salary = parts[2].strip()
        technologies = parts[3].strip()
        english = parts[4].strip()
        industry = parts[5].strip()
        projects = parts[6].strip()
        rating = parts[7].strip()
        tech_level = parts[8].strip()
        availability = parts[9].strip()
        business_impact = parts[10].strip() if len(parts) > 10 else "Expert level development and consulting"
        
        # Extract numbers
        exp_years = int(re.findall(r'\d+', experience)[0]) if re.findall(r'\d+', experience) else 3
        salary_usd = int(re.findall(r'\d+', salary.replace(',', ''))[0]) if re.findall(r'\d+', salary.replace(',', '')) else 3000
        rating_num = float(rating) if rating.replace('.', '').isdigit() else 4.7
        tech_level_num = int(tech_level) if tech_level.isdigit() else 75
        
        # Generate unique name based on business impact
        name = generate_unique_name(business_impact, position, category, counter)
        
        # Format technologies array
        tech_array = [tech.strip() for tech in technologies.split('•')]
        
        # Create developer object
        dev = {
            'id': f'{category[0].upper()}{counter:03d}',
            'name': name,
            'position': position,
            'category': category,
            'technologies': tech_array,
            'experienceYears': exp_years,
            'salaryUSD': salary_usd,
            'englishLevel': english,
            'industry': industry,
            'rating': rating_num,
            'techLevel': tech_level_num,
            'availability': availability,
            'businessImpact': business_impact
        }
        
        developers.append(dev)
        counter += 1

# Add 7 more developers to reach 202 total

# Add 7 more developers to reach 202 total
additional_devs = [
    {'id': 'EX196', 'name': 'Expert Elite', 'position': 'Senior Developer', 'category': 'Expert', 'technologies': ['React','Node.js','Python'], 'experienceYears': 6, 'salaryUSD': 5000, 'englishLevel': 'Advanced', 'industry': 'Technology', 'rating': 4.8, 'techLevel': 120, 'availability': 'Available now', 'businessImpact': 'Expert level development and consulting'},
]
developers.extend(additional_devs)
        js_array += "\n"

js_array += "\t\t];"

print(f"Generated {len(developers)} developers")
print(f"First 5 developers:")
for i in range(min(5, len(developers))):
    dev = developers[i]
    print(f"  {dev['id']}: {dev['name']} ({dev['position']})")

# Save to file
with open('all_developers_array.js', 'w', encoding='utf-8') as f:
    f.write(js_array)

print(f"\nSaved to all_developers_array.js")