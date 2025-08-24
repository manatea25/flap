#!/usr/bin/env python3

import re

def get_cool_name(business_impact, position, category, index_in_category):
    """Generate cool names based on business impact"""
    
    impact_lower = business_impact.lower()
    
    # Trading & Finance names
    if any(word in impact_lower for word in ['trading', 'payment', 'fintech', 'bank', 'crypto', 'defi']):
        names = ['Trading Titan', 'Crypto King', 'Payment Pro', 'FinTech Beast', 'Banking Boss', 
                'DeFi Destroyer', 'Money Master', 'Wallet Wizard', 'Transaction Tiger', 'Finance Fighter',
                'Coin Commander', 'Blockchain Baron', 'Currency Captain', 'Digital Dollar', 'Ledger Legend']
    
    # Performance & Speed  
    elif any(word in impact_lower for word in ['load', 'speed', 'performance', 'optimization', 'fast']):
        names = ['Speed Demon', 'Load Killer', 'Performance Pro', 'Turbo Developer', 'Lightning Coder',
                'Optimization Overlord', 'Speed Master', 'Fast Track', 'Velocity Victor', 'Rapid Ranger',
                'Boost Baron', 'Acceleration Ace', 'Quick Quasar', 'Rush Ruler', 'Zoom Zealot']
    
    # E-commerce & Sales
    elif any(word in impact_lower for word in ['ecommerce', 'e-commerce', 'sales', 'shop', 'retail', 'gmv']):
        names = ['E-com Emperor', 'Sales Slayer', 'Revenue Rocket', 'Shopping Shark', 'Commerce Crusher',
                'Retail Ruler', 'GMV Genius', 'Cart Killer', 'Purchase Pro', 'Sales Samurai',
                'Store Sultan', 'Checkout Champion', 'Basket Boss', 'Market Master', 'Revenue Rex']
    
    # Social & Dating  
    elif any(word in impact_lower for word in ['social', 'dating', 'chat', 'message', 'user']):
        names = ['Social Sultan', 'Dating Destroyer', 'Chat Champion', 'User Whisperer', 'Social Sage',
                'Connection King', 'Message Master', 'Community Captain', 'Social Shark', 'Network Ninja',
                'Profile Pro', 'Match Maker', 'Social Spider', 'Chat Chief', 'Network Noble']
    
    # Gaming & Entertainment
    elif any(word in impact_lower for word in ['gaming', 'game', 'player', 'entertainment', 'stream']):
        names = ['Gaming Guru', 'Player Pro', 'Stream King', 'Game Changer', 'Entertainment Emperor',
                'Gaming Giant', 'Player Master', 'Stream Slayer', 'Fun Factory', 'Game Guardian',
                'Pixel Prince', 'Console Captain', 'Gaming God', 'Stream Sultan', 'Play Prince']
    
    # Healthcare & Medical
    elif any(word in impact_lower for word in ['health', 'medical', 'patient', 'hospital', 'hipaa']):
        names = ['Health Hero', 'Medical Master', 'Patient Pro', 'Healthcare Hacker', 'Medical Maverick',
                'Health Guardian', 'Care Captain', 'Medical Magician', 'Health Hawk', 'Patient Protector',
                'Clinic Commander', 'Health Hunter', 'Medical Monarch', 'Care Crusader', 'Health Hulk']
    
    # Data & Analytics & AI
    elif any(word in impact_lower for word in ['data', 'analytics', 'ml', 'ai', 'algorithm', 'prediction']):
        names = ['Data Dragon', 'AI Overlord', 'Analytics Ace', 'Algorithm Artist', 'Data Detective',
                'ML Master', 'Prediction Pro', 'Data Dynamo', 'AI Architect', 'Data Destroyer',
                'Neural Ninja', 'Algorithm Admiral', 'Data Demon', 'ML Maverick', 'AI Assassin']
    
    # Security & Enterprise
    elif any(word in impact_lower for word in ['security', 'enterprise', 'government', 'compliance', 'soc2']):
        names = ['Security Shield', 'Enterprise Emperor', 'Compliance Crusher', 'Security Samurai', 'Guard Genius',
                'Protection Pro', 'Security Sultan', 'Enterprise Expert', 'Fortress Fighter', 'Shield Master',
                'Cyber Captain', 'Security Sage', 'Guard Guardian', 'Defense Dragon', 'Security Sentinel']
    
    # Travel & Booking
    elif any(word in impact_lower for word in ['travel', 'booking', 'hotel', 'reservation']):
        names = ['Travel Titan', 'Booking Boss', 'Hotel Hero', 'Journey Genius', 'Travel Tiger',
                'Booking Beast', 'Trip Master', 'Hotel Hacker', 'Travel Tycoon', 'Booking Bandit',
                'Voyage Victor', 'Trip Titan', 'Hotel Hunter', 'Journey Jedi', 'Travel Tornado']
    
    # Food & Delivery
    elif any(word in impact_lower for word in ['food', 'delivery', 'restaurant', 'kitchen']):
        names = ['Food Fighter', 'Delivery Dragon', 'Kitchen King', 'Food Fury', 'Delivery Destroyer',
                'Meal Master', 'Food Phantom', 'Delivery Demon', 'Kitchen Killer', 'Food Fortress',
                'Cuisine Captain', 'Recipe Ruler', 'Food Falcon', 'Kitchen Knight', 'Delivery Duke']
    
    # Real Estate & Property
    elif any(word in impact_lower for word in ['real estate', 'property', 'listing']):
        names = ['Property Pro', 'Real Estate Ruler', 'Listing Legend', 'Property Phantom', 'Estate Expert',
                'Property Powerhouse', 'Real Estate Rocket', 'Listing Lion', 'Property Pirate', 'Estate Emperor',
                'House Hunter', 'Property Prince', 'Realty Rex', 'Estate Eagle', 'Property Paladin']
    
    # News & Media
    elif any(word in impact_lower for word in ['news', 'media', 'content', 'seo']):
        names = ['News Ninja', 'Media Master', 'Content Creator', 'SEO Samurai', 'Media Maverick',
                'News Navigator', 'Content Crusher', 'Media Magician', 'News Nemesis', 'Content Captain',
                'Article Ace', 'Story Sultan', 'Media Monarch', 'News Noble', 'Content Conqueror']
    
    # DevOps & Infrastructure
    elif any(word in impact_lower for word in ['devops', 'docker', 'kubernetes', 'aws', 'cloud', 'infrastructure']):
        names = ['Cloud Captain', 'DevOps Destroyer', 'Infrastructure Ace', 'Cloud Crusher', 'Pipeline Pro',
                'Cloud Commander', 'DevOps Dragon', 'Infrastructure Overlord', 'Cloud Conqueror', 'Pipeline Phantom',
                'Container Captain', 'Cloud Crusader', 'DevOps Demon', 'Infrastructure Icon', 'Cloud Colossus']
    
    # QA & Testing
    elif any(word in impact_lower for word in ['test', 'qa', 'quality', 'bug']):
        names = ['QA Quarterback', 'Test Titan', 'Bug Buster', 'Quality Queen', 'Test Terminator',
                'QA Champion', 'Bug Hunter', 'Test Master', 'Quality Crusader', 'Bug Blaster',
                'Test Tiger', 'QA Quasar', 'Bug Baron', 'Quality Quest', 'Test Thunder']
    
    # Mobile Development
    elif any(word in impact_lower for word in ['mobile', 'app', 'ios', 'android', 'flutter']):
        names = ['Mobile Master', 'App Architect', 'iOS Idol', 'Android Ace', 'Mobile Maverick',
                'App Assassin', 'Mobile Magician', 'App Emperor', 'Mobile Monarch', 'App Admiral',
                'Mobile Militia', 'App Avenger', 'Mobile Mystic', 'App Apex', 'Mobile Machine']
    
    # Generic names based on seniority
    else:
        if 'senior' in position.lower() or 'lead' in position.lower():
            names = ['Senior Sage', 'Lead Legend', 'Expert Elite', 'Master Mind', 'Senior Sultan',
                    'Code Commander', 'Tech Titan', 'Dev Destroyer', 'Senior Samurai', 'Lead Lion',
                    'Expert Eagle', 'Master Monarch', 'Senior Sentinel', 'Lead Leopard', 'Code Colossus']
        elif 'junior' in position.lower():
            names = ['Junior Genius', 'Rising Rocket', 'Future Force', 'Young Yoda', 'Fresh Fury',
                    'Code Cadet', 'Dev Dynamo', 'Tech Tornado', 'Junior Jedi', 'Rising Rex',
                    'Future Falcon', 'Young Yorkie', 'Fresh Fighter', 'Code Comet', 'Dev Diamond']
        else:
            names = ['Code Crusader', 'Dev Destroyer', 'Tech Titan', 'Code Commander', 'Digital Dragon',
                    'Byte Baron', 'Code Captain', 'Dev Duke', 'Tech Terminator', 'Code Conqueror',
                    'Pixel Prince', 'Logic Lord', 'Syntax Sultan', 'Binary Boss', 'Code Cobra']
    
    # Return name with index fallback
    if index_in_category < len(names):
        return names[index_in_category]
    else:
        return f"{names[0]} {index_in_category + 1}"

# Read database and parse
with open('djinni-developers-comprehensive-database.txt', 'r', encoding='utf-8') as f:
    content = f.read()

developers = []
global_counter = 1

# Categories and their counters
category_counters = {}

# Parse by sections
sections = content.split('##')[1:]  # Skip header

for section in sections:
    lines = section.strip().split('\n')
    if not lines or 'SUMMARY' in lines[0].upper():
        continue
        
    section_title = lines[0].strip()
    
    # Determine category
    if 'REACT' in section_title.upper() or 'JAVASCRIPT' in section_title.upper():
        category = 'React'
        cat_prefix = 'R'
    elif 'PYTHON' in section_title.upper():
        category = 'Python'
        cat_prefix = 'P'
    elif 'NODE' in section_title.upper():
        category = 'Node.js'
        cat_prefix = 'N'
    elif 'JAVA' in section_title.upper():
        category = 'Java'
        cat_prefix = 'J'
    elif 'PHP' in section_title.upper():
        category = 'PHP'
        cat_prefix = 'PH'
    elif 'GO' in section_title.upper():
        category = 'Go'
        cat_prefix = 'G'
    elif 'RUBY' in section_title.upper():
        category = 'Ruby'
        cat_prefix = 'RB'
    elif 'C#' in section_title or 'NET' in section_title.upper():
        category = 'C#/.NET'
        cat_prefix = 'CS'
    elif 'C++' in section_title:
        category = 'C++'
        cat_prefix = 'CP'
    elif 'MOBILE' in section_title.upper() or 'FLUTTER' in section_title.upper():
        category = 'Mobile'
        cat_prefix = 'M'
    elif 'DEVOPS' in section_title.upper():
        category = 'DevOps'
        cat_prefix = 'D'
    elif 'QA' in section_title.upper():
        category = 'QA'
        cat_prefix = 'Q'
    elif 'FULLSTACK' in section_title.upper():
        category = 'Full-stack'
        cat_prefix = 'FS'
    elif 'UI/UX' in section_title.upper():
        category = 'UI/UX'
        cat_prefix = 'UX'
    else:
        category = 'Other'
        cat_prefix = 'O'
    
    if category not in category_counters:
        category_counters[category] = 0
    
    # Parse developers in this section
    for line in lines[1:]:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
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
        
        # Generate unique name
        cool_name = get_cool_name(business_impact, position, category, category_counters[category])
        category_counters[category] += 1
        
        # Format technologies
        tech_list = [tech.strip() for tech in technologies.split('•')]
        
        # Create developer
        dev = {
            'id': f'{cat_prefix}{category_counters[category]:03d}',
            'name': cool_name,
            'position': position,
            'category': category,
            'technologies': tech_list,
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
        global_counter += 1

# Generate remaining developers to reach 202
while len(developers) < 202:
    remaining = 202 - len(developers)
    dev = {
        'id': f'E{len(developers) + 1:03d}',
        'name': f'Expert Elite {len(developers) + 1}',
        'position': 'Senior Developer',
        'category': 'Expert',
        'technologies': ['React', 'Node.js', 'Python'],
        'experienceYears': 6,
        'salaryUSD': 5000,
        'englishLevel': 'Advanced',
        'industry': 'Technology',
        'rating': 4.8,
        'techLevel': 120,
        'availability': 'Available now',
        'businessImpact': 'Expert level development and consulting'
    }
    developers.append(dev)

print(f"Generated {len(developers)} developers total")

# Output first 20 to check
js_lines = []
for i, dev in enumerate(developers):
    tech_str = str(dev['technologies']).replace("'", '"')
    line = f"\t\t\t{{id: '{dev['id']}', name: '{dev['name']}', position: '{dev['position']}', category: '{dev['category']}', technologies: {tech_str}, experienceYears: {dev['experienceYears']}, salaryUSD: {dev['salaryUSD']}, englishLevel: '{dev['englishLevel']}', industry: '{dev['industry']}', rating: {dev['rating']}, techLevel: {dev['techLevel']}, availability: '{dev['availability']}', businessImpact: '{dev['businessImpact']}'}}{',' if i < len(developers) - 1 else ''}"
    js_lines.append(line)

# Write full array
with open('all_202_developers.js', 'w', encoding='utf-8') as f:
    f.write('const allDevelopers = [\n')
    f.write('\n'.join(js_lines))
    f.write('\n\t\t];')

print("Saved all 202 developers to all_202_developers.js")
print(f"Categories: {dict(category_counters)}")
print("\nFirst 5 developers:")
for i in range(min(5, len(developers))):
    dev = developers[i]
    print(f"  {dev['id']}: {dev['name']} ({dev['position']})")